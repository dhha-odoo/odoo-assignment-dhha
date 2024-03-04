# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api


class FleetInherit(models.Model):
    _inherit = "fleet.vehicle.model.category"
    _description = "fleet vehical model category inherit"

    max_weight = fields.Integer("Max Weight", copy=False, default=10)

    max_volume = fields.Integer("Max Volume", copy=False, default=10)

    @api.depends('name', 'max_weight', 'max_volume')
    def _compute_display_name(self):
        for rec in self:
            rec.display_name = f"{rec.name} ({rec.max_weight} kg, {rec.max_volume} m³)"
