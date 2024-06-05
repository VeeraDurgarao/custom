from odoo import models, api

class PlanningSlot(models.Model):
    _inherit = 'planning.slot'

    @api.model
    def custom_button_action(self):
        # Custom server-side logic goes here
        return True
