# -*- coding: utf-8 -*-
{
    'name': "Mostrar Cuenta Para FCE AFIP Argentina",

    'summary': """
        Muestra el campo desplegable en la pestaña Otra Informacion
        para seleccionar la cuenta bancaria a informar en la FCE de
        AFIP Argentina
    """,

    'description': """
        Muestra el campo desplegable en la pestaña Otra Informacion
        para seleccionar la cuenta bancaria a informar en la FCE de
        AFIP Argentina
    """,

    'author': "TRIX.Hosting",
    'website': "https://trix.hosting",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'account',
    ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
        # 'demo/demo.xml',
    # ],
}