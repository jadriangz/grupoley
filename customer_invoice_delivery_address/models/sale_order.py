from odoo import api, models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # Sobreescribimos el metodo de nuestro modelo sale.order para que nos filtre las direcciones
    # correspondientes a cada cliente
    @api.model
    @api.onchange('partner_id')
    def onchange_partner_id(self):

        # Llamamos al metodo padre para no romper su función
        super(SaleOrder, self).onchange_partner_id()

        # Creamos listas donde se guardaran las direcciones del cliente
        partners_invoice = []
        partners_shipping = []

        domain = {}

        # Recorremos nuestro modelo en busca de los registros necesarios
        for record in self:
            if record.partner_id:
                if record.partner_id.child_ids:
                    for partner in record.partner_id.child_ids:
                        if partner.type == 'invoice':
                            partners_invoice.append(partner.id)
                        if partner.type == 'delivery':
                            partners_shipping.append(partner.id)
                if partners_invoice:
                    domain['partner_invoice_id'] =  [('id', 'in', partners_invoice)]
                else:
                    domain['partner_invoice_id'] =  []
                if partners_shipping:
                    domain['partner_shipping_id'] = [('id', 'in', partners_shipping)]
                else:
                    domain['partner_shipping_id'] =  []
            else:
                domain['partner_invoice_id'] =  [('type', '=', 'invoice')]
                domain['partner_shipping_id'] =  [('type', '=', 'delivery')]

        return {'domain': domain}