from odoo import http
from odoo.exceptions import ValidationError
from odoo.http import request


class ProductCategoryController(http.Controller):

    @http.route('/category/', type="http", auth='public', website=True, csrf=False)
    def product_categories_page(self, **kw):
        categories = request.env['product.category'].sudo().search([])
        return http.request.render('website_tasks.product_categories_page', {'categories': categories})

    @http.route('/category/<model("product.category"):category>', type='http', auth="public", website=True)
    def category_page(self, category, **kwargs):
        products = request.env['product.template'].sudo().search([('categ_id', '=', category.id)])
        return http.request.render('website_tasks.category_page_template', {
            'category': category,
            'products': products,
        })

    @http.route('/product/<model("product.template"):product>', type='http',
                auth="public", website=True)
    def product_details(self, product, **kwargs):
        # result = request.env['product.template'].search([])
        # print(result.qty_available)
        if product.qty_available > 0:
            return request.render('website_tasks.product_details', {
                'product': product,
            })

