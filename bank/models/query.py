from odoo import fields, models, api

class QueryBank(models.Model):
    _name = "query.bank"
    _description = "Bank customer"

    name = fields.Char(string="Name", required=True, translate=True)
    account_number = fields.Char(string="Account Number", required=True)
    location = fields.Char(string="Location")
    assets = fields.Integer(string='Assets')
    status = fields.Selection([("done", 'Done'), ("draft", "Draft")], string="Status", default="draft")
    #
    # def _select(self):
    #     return "name"
    #
    # def _from(self):
    #     return "customer_bank"
    #
    # def _query(self):
    #     return f"""
    #         SELECT {self._select()}
    #         FROM {self._from()}
    #     """
    #
    # @property
    # def _table_query(self):
    #     return self._query()


class NewOrder(models.Model):
    _inherit = 'sale.order'
    # sale.order inside user add new products that product is 'stored'
    #  that particular product quantity is stored on the above field

    total_quantity = fields.Integer(string="Total Quantity")

    # def get_views(self, views, options=None):
    #     if self.check_access_rights('read', raise_exception=False):
    #         return super().get_views(views, options)
    #     res = self.env['hr.employee.public'].get_views(views, options)
    #     res['models'].update({'hr.employee': res['models']['hr.employee.public']})
    #     return res

    @api.model
    def create(self, vals):
        # print(self)
        value = 0
        new_order = super(NewOrder, self).create(vals)
        # print(self)
        for order_line in new_order.order_line:
            # print(order_line.price_unit)
            for line in order_line:
                type = line.product_template_id.detailed_type
                if type == 'product':
                    value += line.product_uom_qty
        new_order['total_quantity'] = value
        return new_order

    def write(self, vals):
        # print(self)
        result = super(NewOrder, self).write(vals)
        # print(result)
        if 'order_line' in vals:
            for order in self:
                total_qty = 0
                for line in order.order_line.filtered(lambda x: x.product_id.type == 'product'):
                    total_qty += line.product_uom_qty
                order.total_quantity = total_qty
        return result

    # copy partially change name in duplicate record set
    def copy(self, default=None):
        print(default)
        default = dict(default or {})
        res = super().copy(default)
        res['custom_name'] = 'Durgarao'
        return res



