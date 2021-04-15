# -*- coding: utf-8 -*-
import ast

from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    is_promo = fields.Boolean(default=False, string="¿es promo?")

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def recompute_coupon_lines(self):
        for order in self:
            order._remove_invalid_reward_lines()
            order._custom_create_new_no_code_promo_reward_lines()
            order._custom_update_existing_reward_lines()

    def _custom_create_new_no_code_promo_reward_lines(self):
        '''Apply new programs that are applicable'''
        self.ensure_one()
        order = self
        programs = order._get_applicable_no_code_promo_program()
        programs = programs._keep_only_most_interesting_auto_applied_global_discount_program()
        for program in programs:
            # VFE REF in master _get_applicable_no_code_programs already filters programs
            # why do we need to reapply this bunch of checks in _check_promo_code ????
            # We should only apply a little part of the checks in _check_promo_code...
            error_status = program._check_promo_code(order, False)
            #if not error_status.get('error') or program.reward_type == 'discount':
            if program.promo_applicability == 'on_next_order':
                order._create_reward_coupon(program)
            #elif program.discount_line_product_id.id not in self.order_line.mapped('product_id').ids:
            elif program.reward_type == 'discount':
                self._get_custom_reward_values_discount(program)
            elif program.reward_type == 'product':
                self.write({'order_line': [(0, False, value) for value in self._get_custom_reward_line_values(program)]})
            order.no_code_promo_program_ids |= program

    def _get_custom_reward_line_values(self, program):
        self.ensure_one()
        self = self.with_context(lang=self.partner_id.lang)
        program = program.with_context(lang=self.partner_id.lang)
        if program.reward_type == 'product':
            return [self._get_custom_reward_values_product(program)]

    def _get_custom_reward_values_product(self, program):
        #price_unit = self.order_line.filtered(lambda line: program.reward_product_id == line.product_id)[0].price_reduce
        price_unit = 0.01

        order_lines = (self.order_line - self._get_reward_lines()).filtered(lambda x: program._get_valid_products(x.product_id))
        max_product_qty = sum(order_lines.mapped('product_uom_qty')) or 1
        total_qty = sum(self.order_line.filtered(lambda x: x.product_id == program.reward_product_id).mapped('product_uom_qty'))
        # Remove needed quantity from reward quantity if same reward and rule product
        if program._get_valid_products(program.reward_product_id):
            # number of times the program should be appliedd
            #program_in_order = max_product_qty // (program.rule_min_quantity + program.reward_product_quantity)
            program_in_order = max_product_qty // (program.rule_min_quantity)
            # multipled by the reward qty
            reward_product_qty = program.reward_product_quantity * program_in_order
            # do not give more free reward than products
            reward_product_qty = min(reward_product_qty, total_qty)
            if program.rule_minimum_amount:
                order_total = sum(order_lines.mapped('price_total')) - (program.reward_product_quantity * program.reward_product_id.lst_price)
                reward_product_qty = min(reward_product_qty, order_total // program.rule_minimum_amount)
        else:
            reward_product_qty = min(max_product_qty, total_qty)

        reward_qty = min(int(int(max_product_qty / program.rule_min_quantity) * program.reward_product_quantity), reward_product_qty)
        # Take the default taxes on the reward product, mapped with the fiscal position
        taxes = self.fiscal_position_id.map_tax(program.reward_product_id.taxes_id)
        return {
            'product_id': program.discount_line_product_id.id,
            'price_unit': price_unit,
            'product_uom_qty': reward_qty,
            'is_reward_line': True,
            'name': "(" + program.display_name +  ") " + "Free Product" + " - " + program.reward_product_id.name,
            'product_uom': program.reward_product_id.uom_id.id,
            'tax_id': [(4, tax.id, False) for tax in taxes],
            'is_promo': True
        }

    def _custom_update_existing_reward_lines(self):
        '''Update values for already applied rewards'''
        def update_line(order, lines, values):
            '''Update the lines and return them if they should be deleted'''
            lines_to_remove = self.env['sale.order.line']
            # Check commit 6bb42904a03 for next if/else
            # Remove reward line if price or qty equal to 0
            if values['product_uom_qty'] and values['price_unit']:
                lines.write(values)
            else:
                if program.reward_type != 'free_shipping':
                    # Can't remove the lines directly as we might be in a recordset loop
                    lines_to_remove += lines
                else:
                    values.update(price_unit=0.0)
                    lines.write(values)
            return lines_to_remove

        self.ensure_one()
        order = self
        applied_programs = order._get_applied_programs_with_rewards_on_current_order()

        for program in applied_programs:
            values = order._get_custom_reward_line_values(program)
            lines = order.order_line.filtered(lambda line: line.product_id == program.discount_line_product_id)
            if not lines:
                return False
            if program.reward_type == 'discount' and program.discount_type == 'percentage':
                lines_to_remove = lines
                # Values is what discount lines should really be, lines is what we got in the SO at the moment
                # 1. If values & lines match, we should update the line (or delete it if no qty or price?)
                # 2. If the value is not in the lines, we should add it
                # 3. if the lines contains a tax not in value, we should remove it
                for value in values:
                    value_found = False
                    for line in lines:
                        # Case 1.
                        if not len(set(line.tax_id.mapped('id')).symmetric_difference(set([v[1] for v in value['tax_id']]))):
                            value_found = True
                            # Working on Case 3.
                            lines_to_remove -= line
                            lines_to_remove += update_line(order, line, value)
                            continue
                    # Case 2.
                    if not value_found:
                        order.write({'order_line': [(0, False, value)]})
                # Case 3.
                lines_to_remove.unlink()
            else:
                update_line(order, lines, values[0]).unlink()

    def _get_custom_reward_values_discount(self, program):
        order = self
        lines = order.order_line.filtered(lambda p: p.is_promo == False)
        for line in lines:
            if order._is_valid_product(program, line):
                line.update({'discount': program.discount_percentage})

        return line

    def _is_valid_product(self, program, product):
        domain = ast.literal_eval(program.rule_products_domain) + [('id', '=', product.product_id.id)]
        return bool(self.env['product.product'].search_count(domain))