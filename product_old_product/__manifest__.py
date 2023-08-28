# -*- coding: utf-8 -*-
# Copyright 2017 InfoTerra (<>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Old Product Create',
    'version': '11.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'sunil madhad',
    'website': '',
    'category': 'Web',
    'depends': ['stock'],
    'data': [
        'security/ir.model.access.csv',
        "data/ir_cron_old_product.xml",
        'views/old_product_view.xml',
    ],
    'installable': True,
}
