# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api
from datetime import timedelta


class InventoryInherit(models.Model):
    _inherit = "stock.picking.batch"
    _description = "inventory inherit"

    dock_id = fields.Many2one("stock.dock", string="Dock")
    vehicle_id = fields.Many2one("fleet.vehicle")
    vehicle_category = fields.Many2one("fleet.vehicle.model.category",
                                       string="Vehicle Category", compute="_compute_vehicle_category", store=True)
    weight = fields.Float(string="Weight", readonly=True,
                          compute="_compute_weight", store=True)
    volume = fields.Float(string="Volume", readonly=True,
                          compute="_compute_weight", store=True)
    total_weight_display = fields.Float(readonly=True)
    total_volume_display = fields.Float(readonly=True)
    deadline = fields.Date(
        string="Scheduled Date + 5 Days", compute="_deadline", store=True)

    @api.depends('picking_ids', 'move_line_ids', 'move_line_ids.product_id.weight', 'move_line_ids.product_id.volume', 'vehicle_category')
    def _compute_weight(self):
        for record in self:
            total_weight = sum(line.product_id.weight *
                               line.quantity for line in record.move_line_ids)
            total_volume = sum(line.product_id.volume *
                               line.quantity for line in record.move_line_ids)

            record.total_weight_display, record.total_volume_display = total_weight, total_volume

            max_weight = record.vehicle_category.max_weight or 1.0
            max_volume = record.vehicle_category.max_volume or 1.0

            record.weight = (total_weight / max_weight) * \
                100 if record.vehicle_category else 0.0
            record.volume = (total_volume / max_volume) * \
                100 if record.vehicle_category else 0.0

    @api.depends('scheduled_date')
    def _deadline(self):
        for record in self:
            record.deadline = record.scheduled_date + \
                timedelta(days=5) if record.scheduled_date else False

    @api.depends('vehicle_id')
    def _compute_vehicle_category(self):
        for record in self:
            record.vehicle_category = record.vehicle_id.category_id if record.vehicle_id else False

    @api.depends('name', 'weight', 'volume')
    def _compute_display_name(self):
        for rec in self:
            rec.display_name = f"{rec.name}: {rec.weight} kg, {rec.volume} m³"
