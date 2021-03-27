# -*- coding: utf-8 -*-
{
    'name': "helpdesk_customers",

    'summary': """
        Modulo para modificar el funcionamiento del reportaje en la mesa de ayuda
    """,

    'description': """
        Módulo para modificar la agrupación en los reporte de tickets dentro de mesa de ayuda, con la
        finalidad de tener una mejor visibilidad al momento de realizar informes para auiditoría.
    """,

    'author': "Erick Enrique Abrego Gonzalez",
    'website': "https://todoo.grupoley.com.mx/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Helpdesk',
    'version': '14.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','helpdesk','contacts'],

    # always loaded
    'data': [
        #'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
