from odoo import models, fields

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    Percentage = fields.Integer(string="Discount", config_parameter='Percentage')
    location = fields.Many2many(string='Location',related='pos_config_id.location_ids',readonly=False)
class PosConfig(models.Model):
    _inherit = 'pos.config'
    location_ids = fields.Many2many('res.location', string='Locations')

    def get_locations(self):
        result = []
        data = self.env['pos.config'].search([])
        for rec in data:
            for i in rec.location_ids:
                # result.append(i.name)
                result.append({
                    'name': i.name,
                    'address': i.address,
                    'pin_code': i.pin_code,
                })
        print(result)
        return result

