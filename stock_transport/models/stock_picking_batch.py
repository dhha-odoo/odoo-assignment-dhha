# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api
from datetime import timedelta


class InventoryInherit(models.Model):
    _inherit = "stock.picking.batch"
    _description = "inventory module inherit"

    dock_id = fields.Many2one("stock.dock", string="Dock")

    vehicle_id = fields.Many2one("fleet.vehicle", string="vehicle")

    vehicle_category_id = fields.Many2one("fleet.vehicle.model.category",
                                          string="Vehicle Category", compute="_compute_vehicle_category", store=True)

    weight_percentage = fields.Float(compute="_compute_parcentage")

    volume_percentage = fields.Float(compute="_compute_parcentage")

    total_weight = fields.Float(compute="_compute_parcentage")

    total_volume = fields.Float(compute="_compute_parcentage")

    date_deadline = fields.Date(compute="_date_deadline")

    @api.depends('picking_ids', 'move_line_ids', 'move_line_ids.product_id.weight', 'move_line_ids.product_id.volume', 'vehicle_category_id')
    def _compute_parcentage(self):
        '''
        This method is used to compute  weight_percentage , volume_percentage in % 
        and total_weight , total_volume in kg , m³.
        '''
        for record in self:
            total_weight = sum(line.product_id.weight *
                               line.quantity for line in record.move_line_ids)
            total_volume = sum(line.product_id.volume *
                               line.quantity for line in record.move_line_ids)

            record.total_weight, record.total_volume = total_weight, total_volume

            max_weight = record.vehicle_category_id.max_weight or 1.0
            max_volume = record.vehicle_category_id.max_volume or 1.0

            record.weight_percentage = (total_weight / max_weight) * \
                100 if record.vehicle_category_id else 0.0
            record.volume_percentage = (total_volume / max_volume) * \
                100 if record.vehicle_category_id else 0.0

    # computed date_deadline
    @api.depends('scheduled_date')
    def _date_deadline(self):
        for record in self:
            record.date_deadline = record.scheduled_date + \
                timedelta(days=5) if record.scheduled_date else False

    # computed vehicle_category
    @api.depends('vehicle_id')
    def _compute_vehicle_category(self):
        for record in self:
            record.vehicle_category_id = record.vehicle_id.category_id if record.vehicle_id else False

    @api.depends('total_weight', 'total_volume')
    def _compute_display_name(self):
        '''
        overriding _compute_display_name for display on gantt chart. 
        '''
        for rec in self:
            rec.display_name = f"{rec.name} : ({rec.total_weight} kg, {rec.total_volume} m³)"
