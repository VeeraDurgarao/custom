from odoo import models, fields, api

class posOrders_new(models.Model):
    _inherit = "pos.order"

    note = fields.Char(string="Durgarao Note")
    screen = fields.Char(string='location')

    @api.model
    def _order_fields(self, ui_order):
        order_fields = super(posOrders_new, self)._order_fields(ui_order)
        order_fields['note'] = ui_order.get('note', '')
        order_fields['screen'] = ui_order.get('screen_new')
        return order_fields

    def get_discount(self):
        param_obj = self.env['ir.config_parameter'].sudo()
        discount_limit = param_obj.get_param('Percentage', default=0.0)
        return float(discount_limit)

