from odoo import models, api

class PlanningSlot(models.Model):
    _inherit = 'planning.slot'

    @api.model
    def custom_button_action(self):
        # Custom server-side logic goes here
        return True
# class StockPicking(models.Model):
#     _inherit = "sale.order"
#
#     @api.model
#     def _get_view(self, view_id=None, view_type='form', **options):
#         arch, view = super()._get_view(view_id, view_type, **options)
#         active_company = self.env.user
#         print(active_company)
#         # user.has_group('hr_employee.NewGroup'):
#         if view_type == 'form' and active_company.has_group('sales_approval.group_sale_manager_record_access'):
#             for node in arch.xpath("//field"):
#                 node.set('string', 'Order Reference')
#         return arch, view
