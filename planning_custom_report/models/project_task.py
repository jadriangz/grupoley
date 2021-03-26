from odoo import models, fields, api
from datetime import datetime


class ProjectTask(models.Model):
    # Heredamos del modelo para poder agregar nuevos campos
    _inherit = 'project.task'

#                                Declaración de nuevos campos agregados al modelo heredado
# ------------------------------------------------------------------------------------------------------------------------

    x_in_validation = fields.Boolean(related="stage_id.x_in_validation", string="Validation Stage",
                                     readonly=True, store=True)

    x_validation_date = fields.Datetime(string="Validation Date", compute="_get_validation_date",
                                        readonly=True, store=True)

# ------------------------------------------------------------------------------------------------------------------------


#                                                  Métodos
# -----------------------------------------------------------------------------------------------------------------------

    # Método que nos ayuda a calcular la fecha en que una tarea llega a la etapa de validación
    @api.depends('stage_id.x_in_validation')
    def _get_validation_date(self):
        for task in self:
            task.ensure_one()
            if task.stage_id.x_in_validation:
                self.x_validation_date = datetime.now()
            else:
                self.x_validation_date = None

# -----------------------------------------------------------------------------------------------------------------------


