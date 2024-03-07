# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    # whenever this boolean var is true then automatically stock transport is install
    module_stock_transport = fields.Boolean("Dispatch Management System")
