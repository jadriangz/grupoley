# -*- coding: utf-8 -*-

{
    'name': 'Invoicing Policy For Customer',

    'version': '14.0.1',

    'summary': 'Asigna las politicas de facturación en la vista de clientes',

    'description': 'Políticas de facturación visibles en el módulo de contactos para modificar el flujo definido '
                   'por productos',

    'category': 'Sales',

    'author': 'Soporte Grupo Ley',

    'website': "todoo.grupoley.com.mx",

    'depends': ['base', 'sale_management', 'stock', 'account'],

    'data': [
        'views/customer_invoice_policy_view.xml',
    ],
}


