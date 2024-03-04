# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'fleet_module',
    'version': '1.0',
    'category': 'Fleet',
    'author': 'odoo',
    'depends': ['base', 'fleet', 'stock', 'stock_picking_batch', 'stock_delivery'],
    'summary': 'bridge module for fleet module',
    'auto_install': True,
    'installable': True,
    'data': [
        'security/ir.model.access.csv',

        'data/dock.xml',

        'views/fleet_category.xml',
        'views/inventory_inherit.xml',
        'views/stock_picking_volume.xml',
    ],
    'license': 'LGPL-3',
}
