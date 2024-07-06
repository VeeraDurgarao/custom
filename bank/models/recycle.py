from odoo import api, fields, models,_
from odoo.exceptions import ValidationError

class BankRecycleAccount(models.Model):
    _name = "recycle.account"
    _inherit = 'bank.account','mail.thread'
    _description = "New bankAccount"

    help = fields.Char(string="Help", help="what you want")
    Report_issue = fields.Text(string="Report", help="what is your problem")

    # Retrieve information about the 'name' and 'description' fields of the 'product.product' model

    seq_no = fields.Text(string="Ref No", required=True, readonly=True, default=lambda self: _('NEW'))

    def check_orm(self):
        recordss = self.search([('account_Type', '=', 'savings')])
        print("id1", recordss)

    @api.model
    def read_records_sql(self, *args, **kwargs):
        pass
        # self.env.cr.execute("""
        #         SELECT name FROM recycle_account WHERE account_Type = 'savings'
        #     """)
        # results = self.env.cr.fetchall()
        # for row in results:
        #     print(row[0])

    # @api.model
    # def create(self, vals):
    #     record = super(BankRecycleAccount, self).create(vals)
    #     return record
    #
    # def action_send_email(self):
    #     template_id = self.env.ref('custom_module.email_template_recycle_account').id
    #     if not template_id:
    #         raise ValidationError(_('Email template not found'))
    #     self.env['mail.template'].browse(template_id).send_mail(self.id, force_send=True)


    # ORM CREATE METHOD
    @api.model
    def create(self, vals):

        if vals.get('seq_no', _('NEW')) == _('NEW'):
            vals['seq_no'] = self.env['ir.sequence'].next_by_code('recycle.account') or _('NEW')
        return super(BankRecycleAccount, self).create(vals)
from odoo import models, fields, api

# class Partner(models.Model):
#     _inherit = 'res.partner'
#
#     commission = fields.Float(string="Commission", compute='_compute_commission', store=True)
#
#     @api.depends('sale_order_ids.commission')
#     def _compute_commission(self):
#         for partner in self:
#             partner.commission = sum(partner.sale_order_ids.mapped('commission'))



# EXTENSION INHERITANCE
class StockMoveNew(models.Model):
    _inherit = 'sale.order'

    custom_name = fields.Char(string="Custom Name")
    commission = fields.Float(string="Commission", default=0)
    invisible = fields.Char(string='Invisible')
    flag = fields.Boolean(string='Flag', default=False)

    @api.onchange('partner_id')
    def _compute_customer_detail(self):
        if self.partner_id:
            self.flag = False
        else:
            self.flag = True

    @api.model
    def create(self, vals):
        res = super(StockMoveNew, self).create(vals)
        partner_name = self.env['res.partner'].browse(vals.get('partner_id')).name if vals.get('partner_id') else False
        user_name = self.env['res.partner'].browse(vals.get('user_id')).name if vals.get('user_id') else False
        # amount_total = res.amount_total

        commissionorder_line = {
            'order_no': vals.get('name'),
            'name': vals.get('custom_name'),
            'partner_id': vals.get('partner_id'),
            'user_id': vals.get('user_id'),
            'commission': vals.get('commission', 0),
            # 'amount_total': amount_total,
            'create_date': vals.get('create_date'),
        }
        self.env['commissionorder.line'].create(commissionorder_line)

        return res
    @api.depends('amount_total')
    def compute_commission(self):
        for order in self:
            commission_percentage = 5 #(order.commission)
            order.commission = order.amount_total * (commission_percentage / 100)



    def action_confirm(self):

        for order in self:
            for line in order.order_line:
                if line.product_uom_qty <= 0:
                    raise ValidationError(
                        "Please enter a quantity value for all order lines before confirming the order.")
        return super(StockMoveNew, self).action_confirm()



    def _get_order_lines_to_report(self):
        if self._context.get('my_report'):
            print(" \m\\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nhn\self<>>>>>>", self._context.get('order_lines'))
            order_line = self.env['sale.order.line'].browse(self._context.get('order_lines'))
            return order_line
            # return self._cont//ext.get('order_lines')
        else:
            return super(StockMoveNew, self)._get_order_lines_to_report()

class StockMove(models.Model):
    _inherit = 'stock.picking'
    custom_name = fields.Char(string="Custom Name")




# related='sale_id.custom_name',

class StockOrderLineNew(models.Model):
    _inherit = 'sale.order.line'
    # extra = fields.Integer(string="Extra Tax")

#     def _prepare_procurement_values(self, group_id=False):
#         values = super(StockOrderLineNew, self)._prepare_procurement_values(group_id)
#         values.update({
#             'extra': self.extra
#         })
#         return values
# class StockRule(models.Model):
#     _inherit = 'stock.rule'
#
#     def _get_custom_move_fields(self):
#         fields = super(StockRule, self)._get_custom_move_fields()
#         fields += ['extra']
#         return fields\
# class posOrders_new(models.Model):
#     _inherit="pos.order"
#
#     note = fields.Char(string="Durgarao Note")
#
#     @api.model
#     def custom_note(self,ui_order):
#         return {
#             'note' : ui_order['note']
#         }
# from odoo import models, fields, api
#
# class posOrders_new(models.Model):
#     _inherit = "pos.order"
#
#     note = fields.Char(string="Durgarao Note")
#
#     @api.model
#     def _order_fields(self, ui_order):
#         order_fields = super(posOrders_new, self)._order_fields(ui_order)
#         order_fields['note'] = ui_order.get('note', '')
#         return order_fields
#
#     def get_discount(self):
#         # print("hello")
#         disc = self.env['res.config.settings'].search([])
#         for a in disc:
#             print(a.discount_limit)
#             return a.discount_limit

from odoo import models, fields, api

class posOrders_new(models.Model):
    _inherit = "pos.order"

    note = fields.Char(string="Durgarao Note")
    total_amount = fields.Float(string="Total Amount")
    employe = fields.Char(string="Employee Name")
    confirmation = fields.Boolean(string="Confirmation")
    location = fields.Char(string="Location")
    screen = fields.Char(string='location')

    @api.model
    def _order_fields(self, ui_order):
        order_fields = super(posOrders_new, self)._order_fields(ui_order)
        order_fields['note'] = ui_order.get('note', '')
        # order_fields['total_amount'] = ui_order.get('amount_total', '')
        emp = ui_order.get('employee_id', '')
        order_fields['location'] = ui_order.get('location_pos')
        order_fields['screen'] = ui_order.get('screen_new')
        value = self.env['hr.employee'].browse(emp)
        print(value.name)
        order_fields['employe'] = value.name
        # order_fields['employe'] = ui_order.get('cashier')
        # print(ui_order.get('cashier'))
        return order_fields

    def confirm(self):

        return self.write({
            'confirmation':True
        })


    def get_discount(self):
        param_obj = self.env['ir.config_parameter'].sudo()
        discount_limit = param_obj.get_param('Percentage', default=0.0)
        return float(discount_limit)



class StockMovePickingNew(models.Model):
    _inherit = 'stock.move'
    extra = fields.Integer(string="Extra Tax")
related='sale_line_id.extra',

class new(models.Model):
    _inherit = "sale.order.line"

    _sql_constraints = [
        ('order_product_unique', 'unique(order_id, product_id)', 'The product must be unique per sale order.')
    ]


