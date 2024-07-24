from odoo import http
from odoo.http import request
import json


class SaleOrderController(http.Controller):

    #In this code return automatically created one recordline in sale.order by using api controllers inside the postman
    #in this code no xml only python code and also we are enter body inside this code
    # {
    #     "partner_id": 1,
    #     "order_lines": [
    #         {
    #             "product_id": 1,
    #             "quantity": 2,
    #             "price_unit": 100
    #         },
    #         {
    #             "product_id": 2,
    #             "quantity": 1,
    #             "price_unit": 200
    #         }
    #     ]
    # }

    @http.route('/create_sale_order', type='json', auth='public', methods=['POST'], csrf=False)
    def create_sale_order(self, **kwargs):
        try:
            # Extract data from the request
            data = json.loads(request.httprequest.data)

            # Define sale order values
            order_vals = {
                'partner_id': data.get('partner_id'),
                'order_line': [(0, 0, {
                    'product_id': line.get('product_id'),
                    'product_uom_qty': line.get('quantity'),
                    'price_unit': line.get('price_unit'),
                }) for line in data.get('order_lines', [])]
            }

            # Create the sale order
            sale_order = request.env['sale.order'].sudo().create(order_vals)

            return {'status': 'success', 'sale_order_id': sale_order.id}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}

# from odoo import http
# from odoo.http import request
#
# class veera(http.Controller):

#in this code is return all orders inside the sale.orders by using api controllers it is showing on website

    # @http.route('/bank/create_sale_order/', type='http', auth="public", website=True)
    # def patient_app_data(self, **post):
    #     # return http.request.render("bank.temporary_data",{})
    #     appointment_data = request.env['sale.order'].sudo().search([])
    #     appointmentss = {
    #         'records': appointment_data,
    #     }
    #     return http.request.render("bank.temporary_data", appointmentss)

# controllers/main.py
# from odoo import http
# from odoo.http import request
#
# class CustomEmailController(http.Controller):
#
#     # In this code is automatically created one email template by using api controllers
#
#     @http.route('/website/form/<string:bank>', type='json', auth='public', methods=['POST'], website=True)
#     def create_email(self, **kwargs):
#         values = json.loads(request.httprequest.data)
#         print(values)
#         if values:
#             request.env['mail.mail'].sudo().create(values.get('data_value'))
#             return {'status': 'success', 'message': 'Email created successfully'}
#         return {'status': 'error', 'message': 'Missing values'}
