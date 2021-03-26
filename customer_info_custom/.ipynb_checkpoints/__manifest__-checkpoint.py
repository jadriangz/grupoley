# -*- coding: utf-8 -*-
{
    'name': "Customer Info Custom",

    'summary': """
        Módulo que nos ayuda a organnizar la información de nuestro cliente
    """,

    'description': """
        Módulo que nos permite mostrar en un orden diferente nuestra viste del cliente para un mejor manejo
    """,

    'author': "Soporte Grupo Ley",

    'website': "todoo.grupoley.com.mx",

    'category': 'CRM',

    'version': '14.0.1',

    'depends': ['base','contacts','l10n_mx_edi'],

    'data': [
        'views/res_partner_view.xml',
    ],

    'demo': [
    ],
}
