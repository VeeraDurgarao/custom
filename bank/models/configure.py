from odoo import fields, models, api, _
class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    contract_type = fields.Selection(
        [('monthly', 'Monthly'), ('half_yearly', '6 Months'),
         ('yearly', 'Yearly')],
        string="Contract Type",
        config_parameter='employee_contract.contract_type',
        help="Select contract types from the selection field")
    employee = fields.Many2one('employee.bank',string="Employee")
    interest = fields.Integer(string="Interest",config_parameter='interest')


