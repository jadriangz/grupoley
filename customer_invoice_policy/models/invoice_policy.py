# -*- coding: utf-8 -*-

from odoo import fields, models, api, _

class CustomerInvoice(models.Model):
    _inherit = 'res.partner'

    x_invoice_policy = fields.Selection([
        ('order', 'Ordered quantities'),
        ('delivery', 'Delivered quantities')], string='Invoicing Policy',
        help='Ordered Quantity: Invoice quantities ordered by the customer.\n'
             'Delivered Quantity: Invoice quantities delivered to the customer.',
        default='delivery')

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    # Depende de la politica de facturación del cliente o del producto
    @api.depends('qty_invoiced', 'qty_delivered', 'product_uom_qty', 'order_id.state')
    def _get_to_invoice_qty(self):

        super(SaleOrderLine, self)._get_to_invoice_qty()
        for line in self:
            if line.order_id.state in ['sale', 'done']:
                if line.order_partner_id.x_invoice_policy == 'order' or line.product_id.invoice_policy == 'order':
                    line.qty_to_invoice = line.product_uom_qty - line.qty_invoiced
                else:
                    line.qty_to_invoice = line.qty_delivered - line.qty_invoiced
            else:
                line.qty_to_invoice = 0