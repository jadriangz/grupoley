from odoo import fields, models, api

class AccountAnalyticLine(models.Model):
    # Heredamos del modelo para poder agregar nuevos campos
    _inherit = 'account.analytic.line'

#                                Declaración de nuevos campos agregados al modelo heredado
#-----------------------------------------------------------------------------------------------------------------------

    x_achived_task_in_time = fields.Boolean(string='Task Achived In Time', group_operator='bool_or',
                                            compute='_get_achived_task_in_time', store=True, readonly=True,
                                            help='Task that was achived in time')

    x_achived_task_with_overtime = fields.Boolean(string='Task Achived With Overtime', group_operator='bool_or',
                                                  compute='_get_achived_task_with_overtime', store=True, readonly=True,
                                                  help='Task that was achived with overtime')

    x_date_end = fields.Datetime(string='End Date', related='task_id.date_end', readonly=True, store=True,
                                 help='Ending date of the task')

    x_initial_planned_hours = fields.Float(string='Initial Planned Hours', related="task_id.planned_hours",
                                           readonly=True, store=True)

    x_in_validation = fields.Boolean(string="In Validation", group_operator="bool_or",
                                     related="task_id.x_in_validation", store=True, readonly=True,
                                     help="Tasks in this stage are considered in validation")

    x_is_closed = fields.Boolean(string='Closing Stage', group_operator="bool_or",
                                 related="task_id.is_closed", store=True, readonly=True,
                                 help="Tasks in this stage are considered as closed.")

    x_validation_date = fields.Datetime(string="Validation Date", related='task_id.x_validation_date',
                                        store=True, readonly=True, help="Date when the task reached validation stage")

# -----------------------------------------------------------------------------------------------------------------------



#                                                  Métodos
# -----------------------------------------------------------------------------------------------------------------------

    # Método para calcular si la tarea se realizo en tiempo, teniendo en cuenta las horas iniciales planeadas
    @api.depends('task_id.planned_hours', 'task_id.x_in_validation',
                 'task_id.is_closed', 'task_id.effective_hours')
    def _get_achived_task_in_time(self):
        for task in self:
            task.ensure_one()
            if task.task_id.remaining_hours >= 0 and task.task_id.x_in_validation == True:
                task.x_achived_task_in_time = True
            elif task.task_id.remaining_hours >= 0 and task.task_id.is_closed == True:
                task.x_achived_task_in_time = True
            else:
                task.x_achived_task_in_time = False


    # Método para calcular si la tarea se realizó con retraso, teniendo en cuenta las horas iniciales planeadas
    @api.depends('task_id.planned_hours', 'task_id.x_in_validation',
                 'task_id.is_closed', 'task_id.effective_hours')
    def _get_achived_task_with_overtime(self):
        for task in self:
            task.ensure_one()
            if (task.task_id.remaining_hours < 0 and task.task_id.x_in_validation == True):
                task.x_achived_task_with_overtime = True
            elif task.task_id.remaining_hours < 0 and task.task_id.is_closed == True:
                task.x_achived_task_with_overtime = True
            else:
                task.x_achived_task_with_overtime = False

# -----------------------------------------------------------------------------------------------------------------------