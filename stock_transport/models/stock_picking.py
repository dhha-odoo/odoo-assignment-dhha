# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api


class VolumeInherit(models.Model):
    #  this stock_picking is a transfer part in inventory
    _inherit = "stock.picking"
    _description = "stock picking volume adding"

    volume = fields.Integer("Volume", compute="_compute_volume")

    @api.depends('move_line_ids.product_id.volume')
    def _compute_volume(self):
        for record in self:
            record.volume = sum(line.product_id.volume *
                                line.quantity for line in record.move_line_ids)
