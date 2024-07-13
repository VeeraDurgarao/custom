from odoo import http
from odoo.http import request

class CustomModuleControllers(http.Controller):

    @http.route('/odoo/login_page', type='http', auth="public", website=True)
    def my_page(self, **kwargs):
        return http.request.render("bank.temporary_form",{})
    @http.route('/odoo/form_submit', type='http', auth="public", website=True)
    def form_submit(self, **kwargs):
        return http.request.render("bank.template_form_submit", {})