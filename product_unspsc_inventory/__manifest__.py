# -*- coding: utf-8 -*-
{
    'name': "Product UNSPSC Inventory",

    'summary': """
        Este módulo nos permite agregar una vista de lista que nos muestre los códigos del SAT junto
        con sus productos
    """,

    'description': """
        Este módulo crea una vista de lista en donde se observan los codigos del SAT para cada categoría de
        nuestro producto y así poder modificar si es necesario.
    """,

    'author': "Soporte Grupo Ley",
    'website': "todoo.grupoley.com.mx",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Stock',
    'version': '14.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','stock','product_unspsc','l10n_mx_edi'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/product_unspsc_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
