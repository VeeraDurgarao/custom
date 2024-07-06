from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    bag_charges_ids = fields.Many2many('bag.charges', string="Bag Types")
