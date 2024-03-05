# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api

class FleetInherit(models.Model):
    _inherit = "fleet.vehicle.model.category"
    _description = "fleet vehical model category inherit"

    _sql_constraints = [
        ('positive_max_values', 'CHECK(max_weight > 0 AND max_volume > 0)',
         ('Max weight and max volume must be greater than 0!'))
    ]

    max_weight = fields.Integer(
        string="Max Weight (kg)", copy=False, default=10)

    max_volume = fields.Integer(
        string="Max Volume (m³)", copy=False, default=10)

    # desplay the name for cars
    @api.depends('name', 'max_weight', 'max_volume')
    def _compute_display_name(self):
        for rec in self:
            rec.display_name = f"{rec.name} ({rec.max_weight} kg, {rec.max_volume} m³)"
