# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'stock_fleet_module',
    'version': '1.0',
    'category': 'Fleet Extend',
    'author': 'odoo',
    'depends': ['stock'],
    'summary': 'bridge module between stock transport module and inventory(stock)',
    'auto_install': True,
    'installable': True,
    'data': [
        'views/res_config_settings_views_inherit.xml',
    ],
    'license': 'LGPL-3',
}
