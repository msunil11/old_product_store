# -*- coding: utf-8 -*-
# Copyright 2017 InfoTerra (<>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Old Product Create',
    'version': '11.0',
    'license': 'AGPL-3',
    'author': 'sunil madhad',
    'website': '',
    4 'price': 0,
    'currency': 'EUR',
    'maintainer': 'sunil',
    'support': 'sm26111997jm@gmail.com',
    'license': 'OPL-1',
    'category': 'Phone',
    'summary': 'sunil madhad Odoo',
    'description': 'sunil Odoo',
    'category': 'Product',
    'depends': ['stock'],
    'data': [
        'security/ir.model.access.csv',
        "data/ir_cron_old_product.xml",
        'views/old_product_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': ['static/description/logo.png'],
}











