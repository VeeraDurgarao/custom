from odoo import fields, models, api, _

class Connection(models.Model):
    _name = "connection.order"

    cus_name =fields.Char(string="Name")
    partner = fields.Char(string="Customer Name")
    template = fields.Char(string="template")
    sequence = fields.Char(string="Number")
    date = fields.Datetime(string="Date")
#
#
#
# class orderSale(models.Model):
#     _inherit = 'sale.order'
#     @api.model
#     def create(self, vals):
#         name1 = self.env['res.partner'].browse(vals.get('partner_id')).name
#         res = super(orderSale, self).create(vals)
#         answer = True
#         if answer:
#             self.env['connection.order'].create({
#                 'partner': name1,
#                 'cus_name': vals.get('custom_name'),
#                 'template': vals.get('sale_order_template_id'),
#                 'date': vals.get('validity_date')
#             })
#         return res
#         res = super(orderSale, self).create(vals)
#         answer = True
#         order_date = self.env['sale.order'].search([])
#         for order in order_date:
#             self.env['connection.order'].create({
#                 'sequence':order.name,
#                 'partner':order.partner_id.name,
#                 'cus_name':order.custom_name,
#                 'date':order.validity_date,
#                 'template':order.sale_order_template_id.name,
#             })
#         print(order_date)

class Email(models.Model):
    _inherit = 'sale.order'

    @api.model
    def create(self,vals):
        print(f"Happy Birthday Again")
        res = super(Email,self).create(vals)
        mail_template = self.env.ref('bank.sale_order_main_template')
        mail_template.send_mail(self.id,force_send=True)

        return res


