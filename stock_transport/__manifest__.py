# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'stock_transport',
    'version': '1.0',
    'category': 'Fleet',
    'author': 'odoo',
    'depends': ['fleet', 'stock_picking_batch' , 'stock_delivery'],
    'summary': 'bridge module for fleet module and stock module',
    'auto_install': True,
    'installable': True,
    'data': [
        'security/ir.model.access.csv',

        'data/stock_dock_data.xml',

        'views/fleet_vehicle_model_category_views.xml',
        'views/stock_picking_batch_views.xml',
        'views/stock_picking_views.xml',
    ],
    'license': 'LGPL-3',
}
