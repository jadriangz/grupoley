# -*- coding: utf-8 -*-

from odoo import models, fields, api


class purchase_order_report(models.Model):
    _inherit = 'purchase.order'

    # Creación de nuestro campo agrupador
    x_order_folio = fields.Char('Order Folio', required=True,
                                help='This field help to group different purchase orders in one delivery slip')



