from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


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

from odoo import fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    is_discount_limit = fields.Boolean(
        string='Durgarao',
        help='Check this field for enabling discount limit'
    )
    discount_limit = fields.Float(
        string='Value',
        help='The discount limit amount in percentage' ,config_parameter = 'sale_discount_limit.is_discount_limit'
    )
    # config_parameter = 'sale_discount_limit.discount_limit',
    # @api.constrains('discount_limit')
    # def limit(self):
    #     for i in self:
    #         if i.discount_limit <= 0 or i.discount_limit > 100:
    #             raise ValidationError('Please enter below 100 percentage and above 0')

    Percentage = fields.Integer(string="Percentage", config_parameter='Percentage')
    location = fields.Many2many(string='Location',related='pos_config_id.location_ids',readonly=False)

    # @api.constrains('Percentage')
    # def limit(self):
    #     for i in self:
    #         if i.Percentage <= 0 or i.Percentage > 100:
    #             raise ValidationError('Please enter below 100 percentage and above 0')


    custom_field = fields.Many2one('res.partner',string="Custom Field")


from odoo import models, fields

class PosConfig(models.Model):
    _inherit = 'pos.config'

    location_ids = fields.Many2many('res.location', string='Locations')

    # def action_confirm(self):
    #     """ Function to confirm the book order"""
    #     self.write({
    #         'state': 'confirmed',
    #     })
    #     return self.location_ids

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

