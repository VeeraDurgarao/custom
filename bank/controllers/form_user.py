import base64

from odoo import http
from odoo.http import request
class CustomModuleControllers(http.Controller):

    @http.route('/odoo/login_page', type='http', auth="public", website=True)
    def my_page(self, **kwargs):
        return http.request.render("bank.temporary_form", {})

    @http.route('/odoo/form_submit', type='http', auth="public", website=True, csrf=False)
    def form_submit(self, **kwargs):
        print(request.env.user.name)
        if request.env.user.name == 'Public user':
            request.env['public.user'].sudo().create({
                'name': request.env.user.name,
                'email': kwargs.get('email'),
                'password': kwargs.get('password'),
            })
        else:
            request.env['private.user'].sudo().create({
                'name': request.env.user.name,
                'email': kwargs.get('email'),
                'password': kwargs.get('password'),
            })
            # return request.redirect('/odoo/login_page')
        return http.request.render("bank.template_form_submit", {})

    from odoo import http
    from odoo.http import request

    class WebsiteController(http.Controller):

        @http.route('/myhome/submited', type='http', auth="public", website=True,csrf=False)
        def search_sale_order(self, **durgarao):
            order_number = durgarao.get('orderNumber')
            if order_number:
                SaleOrder = request.env['sale.order']
                sale_order = SaleOrder.sudo().search([('name', '=', order_number)], limit=1)
                return request.render('bank.sale_order_template', {
                    'sale_order': sale_order
                })


            return request.redirect('/')


