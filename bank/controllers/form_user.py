import base64
from odoo import http
from odoo.http import request


@http.route('/bank/form/create', type='http', auth="public", website=True)
def market_form_create(self):
    investors_ids = request.env['res.users'].sudo().search([])
    values = {
        'records': investors_ids,
        'first_name': 'demo23'  # You may want to dynamically set this based on your logic
    }
    return http.request.render("bank.tmp_form_data", values)


@http.route('/bank/form/thankyou', type='http', auth="public", website=True)
def market_form_submit(self, **kwargs):
    file = request.httprequest.files.getlist('upload_document')[0]
    d = file.read()
    encode_file = base64.b64encode(d)

    # Create a record in 'customer.bank'
    record = request.env['customer.bank'].sudo().create({
        'name': kwargs.get('first_name'),
        'dob': kwargs.get('dob'),
        # Add more fields as needed
    })

    return http.request.render("bank.template_market_form_submit", {"stocks": record})

    # 'title': kwargs.get('title'),


# 'name': kwargs.get('first_name'),
# 'dob': kwargs.get('dob'),
# 'mobile_number': kwargs.get('mobile_number'),
# 'email': kwargs.get('email'),
# 'email_sent': kwargs.get('email_sent'),
# 'user_id': kwargs.get('user_id'),
# 'upload_document': encode_file,