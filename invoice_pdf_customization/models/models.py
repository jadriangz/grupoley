# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class invoice_pdf_customization(models.Model):
#     _name = 'invoice_pdf_customization.invoice_pdf_customization'
#     _description = 'invoice_pdf_customization.invoice_pdf_customization'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
class AccountInvoice(models.Model):
    _inherit = 'account.move'

    def calculate_cfdi_values_pdf(self):
        self.ensure_one()
        invoice = self.sudo()
        cfdi_values = {}
        for line in invoice.invoice_line_ids:
            if not line.product_id:
                continue
            cfdi_values[line.id] = {}
            cfdi_values[line.id]['wo_discount'] = line.price_unit * (1 - (line.discount / 100.0))
            cfdi_values[line.id]['total_wo_discount'] = invoice.currency_id.round(line.price_unit * line.quantity)
            cfdi_values[line.id]['discount_amount'] = invoice.currency_id.round(
                cfdi_values[line.id]['total_wo_discount'] - line.price_subtotal)
            cfdi_values[line.id]['price_subtotal_unit'] = invoice.currency_id.round(cfdi_values[line.id]['total_wo_discount'] / line.quantity)
            cfdi_values[line.id]['discount_amount_price_list'] = (line.product_id.list_price - line.price_unit) * line.quantity

            if line.price_unit == 0.010000:
                cfdi_values[line.id]['discount_amount_price_list'] = 0.0
        return cfdi_values

    def get_footer_values(self):
        invoice = self.sudo()
        response = {}
        promissory_note = """POR ESTE PAGARE ME(NOS) OBLIGO(AMOS) A PAGAR INCONDICIONALMENTE, A LA ORDEN DE INDUSTRIAS 
        GUACAMAYA SA DE CV, EL DÍA """+str(self.invoice_date)+""", EN ESTA CIUDAD, O EN CUALQUIER OTRA QUE SEA(MOS) 
        REQUERIDO(OS) A ELECCION DEL TENEDOR DE ESTE PAGARE EL DIA DEL VENCIMIENTO INDICADO, LA CANTIDAD DE, 
        """+str(self.amount_residual)+""" ( """+ invoice._l10n_mx_edi_cfdi_amount_to_text() +"""" ), VALOR RECIBIDO 
        EN MERCANCIA. """

        reiterate =  """(NUESTRA) ENTERA SATISFACCION, SI NO FUERE PUNTUALMENTE CUBIERTO A SU VENCIMIENTO, PAGARE 
        INTERESES MORATORIOS HASTA SU LIQUIDACION TOTAL A RAZON DEL % MENSUAL CULIACÁN SINALOA, A """+str(self.invoice_date)

        response['promissory_note'] = promissory_note
        response['reiterate'] = reiterate

        return response

