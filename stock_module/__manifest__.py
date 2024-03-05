# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'stock_module',
    'version': '1.0',
    'category': 'Fleet Extend',
    'author': 'odoo',
    'depends': ['stock'],
    'summary': 'bridge module for custom module',
    'auto_install': True,
    'installable': True,
    'data': [
        'views/res_settings.xml',
    ],
    'license': 'LGPL-3',
}
