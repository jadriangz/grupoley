# -*- coding: utf-8 -*-
{
    'name': "Planning Custom Report",

    'summary': """
        Módulo que nos permite modificar el reporte de partes de hora con planificación.
    """,

    'description': """
        Módulo que nos permite modificar el reporte de partes de hora con planificación dentro del módulo de
        proyecto agregando campos que facilitan la toma de decisiones.
    """,

    'author': "Soporte Grupo Ley",

    'website': "todoo.grupoley.com.mx",

    'category': 'Project',

    'version': '14.0.1',

    'depends': ['base','project','planning','timesheet_grid','project_forecast','project_timesheet_forecast'],

    'data': [
        'report/timesheet_planning_report.xml',
        'views/planning_slot_report.xml',
        'views/project_task_type.xml',
        'views/project_task.xml',
    ],

    'demo': [
    ],
}
