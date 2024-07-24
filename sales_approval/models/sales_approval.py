from odoo import models, fields,api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # I try to inherite the sale.order that order inside i try add one value inside the status bar

    def sale_approval(self):
        self.state='sale'

        #whenever click on the approval button that status bar is showing saleorder

    state = fields.Selection(
        selection_add=[('to_approve', "To Approve")],
        #seletion_add it is mainly used on the already created state. that partcular state inside we add new value we are using this one.
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


from odoo import models, api


# class StockPicking(models.Model):
#     _inherit = "sale.order"
#
#     @api.model
#     def _get_view(self, view_id=None, view_type='form', **options):
#         arch, view = super(StockPicking, self)._get_view(view_id, view_type, **options)
#         current_user = self.env.user
#         user_group = current_user.has_group('sales_approval.group_sale_manager_record_access')
#         if view_type == 'form' and not(user_group):
#             for node in arch.xpath("//field"):
#                 node.set('readonly', '1')
#         return arch, view

