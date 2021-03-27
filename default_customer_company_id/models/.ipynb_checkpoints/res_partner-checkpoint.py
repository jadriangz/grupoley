# -*- coding: utf-8 -*-

from odoo import models, fields, api

class default_customer_company_id(models.Model):
    _inherit = 'res.partner'

    company_id = fields.Many2one('res.company', string='Company',
                                 default=lambda self: self.env.company)


