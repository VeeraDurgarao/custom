from odoo import fields, models


class Demo(models.TransientModel):
    _name = "demo.demo"

    help = fields.Char(string="Help", help="what you want")
    Report_issue = fields.Text(string="Report", help="what is your problem")

    def submit(self):
        temp = self.env.context.get('active_id')
        print(temp)
        temp1 = self.env['recycle.account'].browse(temp)
        temp1.write({
            'help':self.help,
            'Report_issue':self.Report_issue
        })
