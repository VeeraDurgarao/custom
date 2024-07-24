# from odoo import fields, models, api, _
#
# class NewModel(models.Model):
#     _name = "new.model"
#
#     modules = fields.Many2one('ir.module.module', string="Modules")
#     filter_fields = fields.Many2one('ir.model.fields', string="Filter Fields",compute="_compute_modules")
#     @api.depends('modules')
#     def _compute_modules(self):
#         if self.modules:
#             domain = [
#                 ('model', '=', self.modules.name),
#                 ('model_id', '=', 'Sales Order')
#             ]
#         else:
#             domain = []
#         return {'domain': {'filter_fields': domain}}
#
#
#
#     relation_field = fields.One2many('relation.model','connect',string="relation")
# from odoo import fields, models, api
#
#
# class NewModel(models.Model):
#     _name = "new.model"
#     model_id1 = fields.Many2one('ir.model', string='Model',
#                                 help="The model this field belongs to", )
#
#     filter_fields = fields.Many2one(
#         'ir.model.fields',
#         string="Filter Fields"
#     )
#
#     @api.onchange('model_id1')
#     def _onchange_modules(self):
#         if self.model_id1:
#             domain = [
#                 ('relation', '=', self.model_id1.model),
#                 ('ttype', '=', 'many2one')
#             ]
#             print("++++++++++++++++++++++++",domain)
#         # else:
#     domain = []
# return {'domain': {'filter_fields': domain}}
# domain = [('ttype', '=', 'many2one')],
# print("++++++++++++++++++", domain)
# self.filter_fields = self.env['ir.model.fields'].search(domain)
# print(">>>>>>>>>>>>>>>>>>>>>>", self.filter_fields)

# else:
# many2one_fields = self.env['ir.model.fields'].browse([])
# print(many2one_fields)

# return {'domain': {'filter_fields': [('id', 'in', many2one_fields.ids)]}}

# relation_field = fields.One2many('relation.model', 'connect', string="relation")

# <xpath expr="//field[@name='partner_shipping_id']" position="attributes">
#     <attribute name="domain">['&amp;',('parent_id','=',partner_id),('type','=','delivery')]</attribute>
#     <attribute name="attrs">{'no_create': True}</attribute>
# </xpath>
# Assuming you have model_id1 already set with a specific ir.model record

# First, import necessary modules
from odoo import models, fields, api

from odoo import models, fields, api
from odoo import models, fields, api

class YourClass(models.Model):
    _name = 'new.model'

    model_id1 = fields.Many2one('ir.model', string='Model',
                                help="The model this field belongs to")
    filter_fields = fields.Many2one('ir.model.fields', string="Filter Fields",
                                    domain="[('ttype', '=', 'many2one'), ('model', '=', model_id1)]")

    @api.onchange('model_id1')
    def onchange_model_id1(self):
        if self.model_id1:
            selected_model = self.model_id1.model
            if selected_model:
                model_fields = self.env['ir.model.fields'].search([
                    ('model', '=', selected_model),
                    ('ttype', '=', 'many2one'),
                ])
                field_ids = model_fields.ids
                print("Model Fields:", model_fields)
                print("Field IDs:", field_ids)

                return {
                    'domain': {
                        'filter_fields': [('id', 'in', field_ids)] if field_ids else []
                    }
                }
            else:
                return {
                    'domain': {
                        'filter_fields': []
                    }
                }
        else:
            return {
                'domain': {
                    'filter_fields': []
                }
            }

    # @api.onchange('model_id1')
    # def _onchange_model_id1(self):
    #     if self.model_id1:
    #         # Fetch all many2one fields of the selected model
    #         fields_domain = [
    #             ('model', '=', self.model_id1.id),
    #             ('ttype', '=', 'many2one')
    #         ]
    #         return {'domain': {'filter_fields': fields_domain}}
    #     else:
    #         # Reset the domain if no model is selected
    #         return {'domain': {'filter_fields': []}}

    relation_field = fields.One2many('relation.model', 'connect', string="relation")
