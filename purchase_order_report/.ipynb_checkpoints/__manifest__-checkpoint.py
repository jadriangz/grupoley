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

    'category': 'Purchase',

    'version': '14.0.1',

    'depends': ['base','purchase','mrp'],

    'data': [
        'views/purchase_order.xml',
    ],

    'demo': [
        'demo/demo.xml',
    ],
}
