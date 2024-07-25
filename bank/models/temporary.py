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
        stock_quant = request.env['stock.quant'].search([('product_id', '=', product.product_variant_id.id)],
                                                        order='id asc', limit=1)
        value = 0
        for i in stock_quant:
            value += i.inventory_quantity_auto_apply
        new_item = stock_quant.inventory_quantity_auto_apply if stock_quant else 0
        stock_change_qty = request.env['stock.change.product.qty'].search(
            [('product_id', '=', product.product_variant_id.id)], order='id asc', limit=1)
        new_item2 = stock_change_qty.new_quantity if stock_change_qty else 0

        print(f"Inventory Quantity: {new_item}")
        print(f"New Quantity: {new_item2}")

        result = request.env['product.template'].search([])
        print(result)
        if product.qty_available > 0:
            return request.render('website_tasks.product_details', {
                'product': product,
            })

