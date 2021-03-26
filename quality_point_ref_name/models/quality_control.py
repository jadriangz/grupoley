# -*- coding: utf-8 -*-

from odoo import models, fields, api


class quality_point_ref_name(models.Model):
    _inherit = "quality.point"

    @api.depends('name', 'title')
    def name_get(self):
        result = []
        for record in self:
            name = record.name + ' - ' + record.title if record.title else record.name
            result.append((record.id, name))
        return result