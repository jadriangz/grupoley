# -*- coding: utf-8 -*-
{
    'name': "Approvals Pricelist",

    'summary': """
        Este módulo crea un flujo para la aprobación de tarifas
    """,

    'description': """
        Con este módulo se añade un flujo de aprobación en las tarifas para la venta en donde
        solo los administradores podran aprobar o rechazar la tarifa.       
    """,

    'author': "Soporte Grupo Ley",

    'website': "todoo.grupoley.com.mx",

    'category': 'Sales',

    'version': '14.0.1',

    'depends': ['base','sale_management','contacts'],

    'data': [
        'views/approval_pricelist.xml',
        'views/res_partner.xml',
    ],

    'demo': [
    ],
}
