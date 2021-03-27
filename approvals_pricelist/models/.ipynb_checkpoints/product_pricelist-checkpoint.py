from odoo import fields, models, api

class ProductPricelist(models.Model):
    _inherit = 'product.pricelist'


    date_approve = fields.Datetime('Confirmation Date', readonly=1, index=True, copy=False)

    state = fields.Selection([
        ('draft', 'New'),
        ('authorize', 'To Approve'),
        ('approved', 'Approved')
    ], string='Status', readonly=True, index=True, copy=False, default='draft')


    def button_confirm(self):
        for pricelist in self:
            if pricelist.state not in ['draft']:
                continue
            if pricelist.user_has_groups('sales_team.group_sale_manager'):
                pricelist.button_approve()
            else:
                pricelist.write({'state':'authorize'})

    def button_approve(self):
        self.write({'state': 'approved', 'date_approve': fields.Datetime.now()})
        return {}




