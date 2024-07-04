from odoo import fields, models,api
from odoo.exceptions import ValidationError


from odoo import models, fields
from odoo.exceptions import ValidationError

class Demo(models.TransientModel):
    _name = "demo.demo"
    name = fields.Char(string="Name")
    help_text = fields.Char(string="Help", help="What you want",required=True)
    report_issue = fields.Text(string="Report", help="What is your problem")
    # @api.constrains('help_text', 'report_issue')
    # def _check_fields(self):
    #     for record in self:
    #         if not record.help_text:
    #             raise ValidationError("The 'Help' field is required.")
    #         if not record.report_issue:
    #             raise ValidationError("The 'Report' field is required.")
    #         if not (record.help_text and record.report_issue):
    #             raise ValidationError("Please fill in all fields.")

    def submit(self):
        if not (self.help_text):
            raise ValidationError("Please fill in all fields.")

        temp = self.env.context.get('active_id')
        print(temp)
        temp1 = self.env['recycle.account'].browse(temp)
        temp1.write({
            'help':self.help_text,
            'Report_issue':self.report_issue
        })
