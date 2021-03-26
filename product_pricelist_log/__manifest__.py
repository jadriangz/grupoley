# -*- coding: utf-8 -*-
{
    'name': "Product Pricelist Log",

    'summary': """
        Este módulo nos permite tener un log de los cambios hechos a nuestras tarifas
    """,

    'description': """
        Este módulo nos permite observar los cambios hechos en nuestras tarifas dentro de cada prodcuto.
    """,

    'author': "Soporte Grupo Ley",
    'website': "todoo.grupoley.com.mx",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Inventory',
    'version': '14.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail','sale'],

    # always loaded
    'data': [
        'views/product_pricelist_log_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
