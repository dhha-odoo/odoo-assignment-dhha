# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api


class InventoryInherit(models.Model):
    _inherit = "stock.picking.batch"
    _description = "inventory inherit"

    dock_id = fields.Many2one("stock.dock", string="Dock")

    vehicle = fields.Many2one("fleet.vehicle")

    vehicle_category = fields.Many2one("fleet.vehicle.model.category",
                                       string="Vehicle Category")

    weight = fields.Float(string="Weight", readonly=True,
                          compute="_compute_weight")

    volume = fields.Float(string="Volume", readonly=True,
                          compute="_compute_volume")

    @api.depends('vehicle_category')
    def _compute_weight(self):
        for record in self:
            total_weight = 0.0
            total_volume = 0.0
            avg_weight = 0.0
            avg_volume = 0.0
            if record.vehicle_category:
                max_weight = record.vehicle_category.max_weight
                max_volume = record.vehicle_category.max_volume
                for pick in record:
                    for line in pick.move_line_ids:
                        total_weight += line.product_id.weight * line.quantity
                        total_volume += line.product_id.volume * line.quantity
                        # print(line.product_id.volume)
                        # breakpoint()

                # Calculate the average weight percentage
                if max_weight > 0:
                    avg_weight = (total_weight / max_weight) * 100
                else:
                    avg_weight = 0.0

                # Calculate the average volume percentage
                if max_volume > 0:
                    avg_volume = (total_volume / max_volume) * 100
                else:
                    avg_volume = 0.0

                record.weight = avg_weight
                record.volume = avg_volume
            else:
                record.weight = 0.0
                record.volume = 0.0

    # def _compute_height(self):
    #     for record in self:
    #         # Calculate height progress based on your criteria
    #         # For example, let's assume the maximum height is 10 and height is 5
    #         record.height = (10000 / 10) * 100
