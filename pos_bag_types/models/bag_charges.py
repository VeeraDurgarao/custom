from odoo import fields, models, api


class BagCharges(models.Model):
    _name = 'bag.charges'

    related_product_id = fields.Many2one('product.product', string='Related Product')
    name = fields.Char(string='Bag Name')
    bag_price = fields.Float(string="Bag Price")

    @api.onchange('related_product_id')
    def on_change_name_bag_price(self):
        self.name = self.related_product_id.name
        self.bag_price = self.related_product_id.standard_price
