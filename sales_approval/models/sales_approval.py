from odoo import models, fields,api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def sale_approval(self):
        self.state='sale'

    state = fields.Selection(
        selection_add=[('to_approve', "To Approve")],
    )

    def action_confirm(self):
        param_obj = self.env['ir.config_parameter'].sudo()
        config_limit = param_obj.get_param('sale_limit')

        for order in self:
            if order.amount_total > float(config_limit):
                order.state = 'to_approve'
            else:
                super(SaleOrder,order).action_confirm()
        return True


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    sale_limit = fields.Float(string="Sale Limit",config_parameter='sale_limit')



class imageAdd(models.Model):
    _inherit = 'sale.order.line'

    image = fields.Binary(string="Image",related="product_template_id.image_1920")

class StockMoveImage(models.Model):
    _inherit = 'stock.move'
    image = fields.Binary(string="Image", related="product_id.image_1920")

class StockMoveImage(models.Model):
    _inherit = 'account.move.line'
    image = fields.Binary(string="Image", related="product_id.image_1920")


