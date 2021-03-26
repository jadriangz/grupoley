# -*- coding: utf-8 -*-
{
    'name': "stock_delivery_report",

    'summary': """
        Módulo para crear reportes de vales de entrega con multiples ordenes de compra
    """,

    'description': """
        Este módulo agrupa las ordenes de compra con un folio con la finalidad de poder agruparlas y poder imprimir un solo vale de entrada dependiendo
        de dicho folio
    """,

    'author': "Soporte Grupo Ley",

    'website': "https://todoo.grupoley.com.mx",


    'category': 'Inventory',

    'version': '14.0.1',

    'depends': ['base','stock','purchase_order_report'],

    'data': [
        'views/stock_picking.xml',
        'reports/report.xml',
        'reports/delivery_slip_report.xml',
    ],

    'demo': [
    ],
}
