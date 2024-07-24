from odoo import fields, models, api, _
class relation(models.Model):
    _name = "relation.model"

    connect = fields.Many2one('new.model', string="Connection")

    many_to_one = fields.Char(string="Many To Many")
    create_delete = fields.Boolean(string="Create Delete")

    # model_id1 = fields.Many2one('ir.model', string='Model',
    #                            required=True,
    #                            index=True, ondelete='cascade',
    #                            help="The model this field belongs to",)

