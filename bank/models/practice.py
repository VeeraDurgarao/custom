
from odoo import fields,models,api,_
from datetime import date, datetime, timedelta
class scheduleActions(models.Model):
    _name = "practice.model"
    _description = "practice"

    customer = fields.Many2one("res.partner",string="customer")
    partner_name = fields.Char(string='Customer Name',related = "customer.name")
    expiration = fields.Datetime(string="Expiration")
    Date = fields.Datetime(string="Date")
    payment_term_id = fields.Many2one(
        comodel_name='account.payment.term',
        string="Payment Terms")
    customer_details = fields.Html(string=' ', compute='_compute_customer_detail')
    # quotation_template = fields.Many2one("sale.order.template",string="Quotation Template")
    quotation_template = fields.Many2one("product.template",string="Quotation Template")
    quotation = fields.One2many("product.product",'practice_id',string="Product")

    # amount = fields.Integer(string="Amount")
    ref_no = fields.Text(string="Ref No", readonly=True, default=lambda self: _('NEW'))
    # ORM CREATE METHOD
    @api.model
    def create(self, vals):
        if vals.get('ref_no', _('NEW')) == _('NEW'):
            vals['ref_no'] = self.env['ir.sequence'].next_by_code('practice.model') or _('NEW')
        return super(scheduleActions, self).create(vals)

    @api.depends('customer')
    def _compute_customer_detail(self):
        for record in self:
            if record.customer:
                record.customer_details = f"<p>{record.customer.name}<br/>{record.customer.email}<br/>{record.customer.phone}</p>"
            else:
                record.customer_details = "<p>No customer selected</p>"

    @api.onchange('customer')
    def _onchange_customer(self):
        if self.customer:
            self.Date = datetime.today()
            self.expiration = datetime.today() + timedelta(days=7)

    def sendmail(self):
        pass
    def confirm(self):
        pass
    def preview(self):
        pass