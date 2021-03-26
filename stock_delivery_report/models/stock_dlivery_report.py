# -*- coding: utf-8 -*-

from odoo import models, fields, api


class stock_delivery_report(models.Model):
    _inherit = "stock.picking"
    
    # Creación del folio que servira para agrupar diferentes ordenes de compra
    x_order_folio = fields.Char('Order Folio', related="purchase_id.x_order_folio",
                                help='This field help to group different purchase orders in one delivery slip')

    



    
