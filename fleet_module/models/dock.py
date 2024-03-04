# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api


class Dock(models.Model):
    _name = "stock.dock"
    _description = "dock"

    name = fields.Char("Dock Name")
