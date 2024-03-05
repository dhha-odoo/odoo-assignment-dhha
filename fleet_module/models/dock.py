# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import fields, models

class Dock(models.Model):
    _name = "stock.dock"
    _description = "Dock"

    name = fields.Char("Dock Name", required=True)

    _sql_constraints = [
        ('unique_name', 'UNIQUE(name)', ('Dock name must be unique!')),
    ]
