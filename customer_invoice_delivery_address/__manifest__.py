# -*- coding: utf-8 -*-
{
    'name': "Customer Invoice/Delivery Address",

    'summary': """
        Nos muestra solo las direcciones que se tienen asiganadas al cliente en un pedido de venta.
    """,

    'description': """
        Módulo que nos ayuda a mostrar solo las direcciones de facturación y de entrega que se le tienen asiganadas
        al cliente
    """,

    'author': "Soporte Grupo Ley",

    'website': "todoo.grupoley.com.mx",

    'category': 'CRM',

    'version': '14.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale_management','contacts','account'],

    # always loaded
    'data': [
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
