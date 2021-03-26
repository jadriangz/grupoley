from odoo import tools
from odoo import fields, models, api


class TimesheetPlanningReport(models.Model):
    # Heredamos del modelo para poder agregar nuevos campos y lo sobreescribimos
    _name = "project.timesheet.forecast.report.analysis"
    _inherit = "project.timesheet.forecast.report.analysis"


#                                Declaración de nuevos campos agregados al modelo heredado
# -----------------------------------------------------------------------------------------------------------------------

    x_achived_task_in_time = fields.Boolean(string='Task Achived In Time', readonly=True,
                                            group_operator='bool_or', help='Task that was achived')

    x_achived_task_with_overtime = fields.Boolean(string='Task Achived With Overtime', readonly=True,
                                                  group_operator='bool_or', help='Task that was achived with overtime')

    x_date_end = fields.Datetime('End Date', readonly=True)

    x_initial_planned_hours = fields.Float('Initial Planned Hours', readonly=True, group_operator="max")

    x_in_validation = fields.Boolean(string="In Validation", readonly=True, group_operator="bool_or")

    x_is_closed = fields.Boolean(string="Is Closed", readonly=True, group_operator="bool_or")

    x_validation_date = fields.Datetime('Validation Date', readonly=True)

# -----------------------------------------------------------------------------------------------------------------------

#                                                  Métodos
# -----------------------------------------------------------------------------------------------------------------------

    # Sobreexcribimos el metodo init con el cual podremos crear nuestra vista dinámicamente
    def init(self):
        tools.drop_view_if_exists(self.env.cr, self._table)
        self.env.cr.execute("""
            CREATE or REPLACE VIEW %s as (
                (
                    SELECT
                        d::date AS entry_date,
                        F.employee_id AS employee_id,
                        F.task_id AS task_id,
                        F.project_id AS project_id,
                        F.allocated_hours / NULLIF(F.working_days_count, 0) AS number_hours,
                        0.0 AS effective_hours,
                        F.allocated_hours / NULLIF(F.working_days_count, 0) AS planned_hours,
                        F.allocated_hours / NULLIF(F.working_days_count, 0) AS difference,
                        F.x_date_end::date AS x_date_end,
                        F.x_validation_date::date AS x_validation_date,
                        F.x_in_validation AS x_in_validation, 
                        F.x_is_closed AS x_is_closed,
                        0.0 AS x_initial_planned_hours,
                        NULL AS x_achived_task_in_time,
                        NULL AS x_achived_task_with_overtime,
                        'forecast' AS line_type,
                        F.id AS id
                    FROM generate_series(
                        (SELECT min(start_datetime) FROM planning_slot)::date,
                        (SELECT max(end_datetime) FROM planning_slot)::date,
                        '1 day'::interval
                    ) d
                        LEFT JOIN planning_slot F ON d::date >= F.start_datetime::date AND d::date <= F.end_datetime::date
                        LEFT JOIN hr_employee E ON F.employee_id = E.id
                        LEFT JOIN resource_resource R ON E.resource_id = R.id
                        
                    WHERE
                        EXTRACT(ISODOW FROM d.date) IN (
                            SELECT A.dayofweek::integer+1 FROM resource_calendar_attendance A WHERE A.calendar_id = R.calendar_id
                        )
                ) UNION (
                    SELECT
                        A.date AS entry_date,
                        E.id AS employee_id,
                        A.task_id AS task_id,
                        A.project_id AS project_id,
                        A.unit_amount AS number_hours,
                        A.unit_amount AS effective_hours,
                        0.0 AS planned_hours,
                        -A.unit_amount AS difference,
                        A.x_date_end::date AS x_date_end,
                        A.x_validation_date::date AS x_validation_date,
                        A.x_in_validation AS x_in_validation, 
                        A.x_is_closed AS x_is_closed,
                        A.x_initial_planned_hours AS x_initial_planned_hours,
                        A.x_achived_task_in_time AS x_achived_task_in_time,
                        A.x_achived_task_with_overtime AS x_achived_task_with_overtime,
                        'timesheet' AS line_type,
                        -A.id AS id
                    FROM account_analytic_line A, hr_employee E
                    WHERE A.project_id IS NOT NULL
                        AND A.employee_id = E.id
                )                             
            )
        """ % (self._table,))

# -----------------------------------------------------------------------------------------------------------------------
