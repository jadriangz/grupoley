# -*- coding: utf-8 -*-

from odoo import models, fields, api

class product_pricelist_log(models.Model):
    _name = 'product.pricelist.item'
    _inherit = ['product.pricelist.item', 'mail.thread', 'mail.activity.mixin']

    applied_on = fields.Selection([
        ('3_global', 'All Products'),
        ('2_product_category', 'Product Category'),
        ('1_product', 'Product'),
        ('0_product_variant', 'Product Variant')], "Apply On", tracking=True)

    min_quantity = fields.Float(
        'Min. Quantity', tracking=True)

    date_start = fields.Datetime('Start Date', tracking=True)

    date_end = fields.Datetime('End Date', tracking=True)

    compute_price = fields.Selection([
        ('fixed', 'Fixed Price'),
        ('percentage', 'Percentage (discount)'),
        ('formula', 'Formula')], tracking=True)

    base = fields.Selection([
        ('list_price', 'Sales Price'),
        ('standard_price', 'Cost'),
        ('pricelist', 'Other Pricelist')], "Based on", tracking=True)

    fixed_price = fields.Float('Fixed Price', tracking=True)

    price_round = fields.Float(
        'Price Rounding', tracking=True)

    price_discount = fields.Float('Price Discount', tracking=True)

    price_min_margin = fields.Float(
        'Min. Price Margin', tracking=True)

    price_max_margin = fields.Float(
        'Max. Price Margin', tracking=True)

    price_surcharge = fields.Float(
        'Price Surcharge', tracking=True)















