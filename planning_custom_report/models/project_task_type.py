from odoo import api, fields, models

class ProjectTaskType(models.Model):
    _inherit = 'project.task.type'

    x_in_validation = fields.Boolean(string="Validation Stage", store=True, copied=True,
                                     help="Task in this stage are in validation before its close")