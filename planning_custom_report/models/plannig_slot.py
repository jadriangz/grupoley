from odoo import api, fields, models


class PlanningSlot(models.Model):
    # Heredamos del modelo para poder agregar nuevos campos
    _inherit = 'planning.slot'

#                                Declaración de nuevos campos agregados al modelo heredado
#------------------------------------------------------------------------------------------------------------------------

    x_date_end = fields.Datetime(string="End Date", related="task_id.date_end", store=True, readonly=True)

    x_in_validation = fields.Boolean(string="In Validation", group_operator="bool_or",
                                     related="task_id.x_in_validation", store=True, readonly=True,
                                     help="Tasks in this stage are considered in validation")

    x_is_closed = fields.Boolean(string='Closing Stage', group_operator="bool_or" ,
                                 related="task_id.is_closed", store=True, readonly=True,
                                 help="Tasks in this stage are considered as closed.")

    x_validation_date = fields.Datetime(string="Validation Date", related='task_id.x_validation_date',
                                        store=True, readonly=True)

# -----------------------------------------------------------------------------------------------------------------------