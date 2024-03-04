# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api


class FleetInherit(models.Model):
    _inherit = "stock.picking"
    _description = "stock picking volume"

    volume = fields.Integer("Volume")

    @api.depends('vehicle_category')
    def _compute_weight(self):
        for record in self:
            for pick in record:
                for line in pick.move_line_ids:
                    record.volume = line.product_id.volume
