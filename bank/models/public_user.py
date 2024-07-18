from odoo import models, fields
class publicUser(models.Model):
    _name = 'public.user'

    name = fields.Char(string="Name")
    email = fields.Char(string="Email")
    password = fields.Char(string="Password")


class formUser(models.Model):
    _name = 'private.user'
    _inherit = "public.user"