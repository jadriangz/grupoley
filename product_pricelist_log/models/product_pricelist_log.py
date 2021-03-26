# -*- coding: utf-8 -*-

from odoo import models, fields, api

class product_pricelist_log(models.Model):
    _name = 'product.pricelist.item'
    _inherit = ['product.pricelist.item', 'mail.thread', 'mail.activity.mixin']

    applied_on = fields.Selection([
        ('3_global', 'All Products'),
        ('2_product_category', 'Product Category'),
        ('1_product', 'Product'),
        ('0_product_variant', 'Product Variant')], "Apply On", track_visibility="always")

    min_quantity = fields.Float(
        'Min. Quantity', track_visibility="always")

    date_start = fields.Datetime('Start Date', track_visibility="always")

    date_end = fields.Datetime('End Date', track_visibility="always")

    compute_price = fields.Selection([
        ('fixed', 'Fixed Price'),
        ('percentage', 'Percentage (discount)'),
        ('formula', 'Formula')], track_visibility="always")

    base = fields.Selection([
        ('list_price', 'Sales Price'),
        ('standard_price', 'Cost'),
        ('pricelist', 'Other Pricelist')], "Based on", track_visibility="always")

    fixed_price = fields.Float('Fixed Price', track_visibility="always")

    price_round = fields.Float(
        'Price Rounding', track_visibility="always")

    price_discount = fields.Float('Price Discount', track_visibility="always")

    price_min_margin = fields.Float(
        'Min. Price Margin', track_visibility="always")

    price_max_margin = fields.Float(
        'Max. Price Margin', track_visibility="always")

    price_surcharge = fields.Float(
        'Price Surcharge', track_visibility="always")















