# -*- coding: utf-8 -*-

from odoo import api, models, _
from odoo.exceptions import ValidationError, UserError, RedirectWarning

class DeliverySlipCustomReport(models.Model):
    _name = 'report.stock_delivery_report.report_multiple_delivery_slip'
    _description = 'Multiples purchase orders and one delivery slip'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['stock.picking'].browse(docids)

        # Folio que nos ayudara a filtrar nuestros registros
        folio_filter = ""

        # Asignamos el valor a nuestro filtro desde nuestro registro seleccionado
        for i, record in enumerate(docs):
            # Si se seleccionó solo un registro
            if i == 0:
                folio_filter = record.x_order_folio
            # Si se seleccionó más de un registro
            elif i > 0:
                raise UserError(_("It is not possible to generate the report, only a delivery slip must be selected"))
            else:
                pass

        # Agrupamos los registros por medio del folio
        records = self.env['stock.picking'].search([('x_order_folio','=',folio_filter)])

        return {
            'docs':docs,
            'records': records,
        }