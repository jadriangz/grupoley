# -*- coding: utf-8 -*-
{
    'name': "purchase_order_report",

    'summary': """
        Módulo para agregar un campo folio a la vista formulario del módulo de compras
    """,

    'description': """
        Este módulo añade un campo nuevo llamado "Folio de orden" para poder agrupar diferentes ordenes de compra
    """,

    'author': "Soporte Grupo Ley",
    'website': "http://todoo.grupoley.com.mx",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Purchase',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','purchase'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
