# -*- coding: utf-8 -*-

from odoo import models, fields, api
import requests
import datetime
import hmac
import hashlib
import base64
import json

from odoo.exceptions import UserError


class PaymentProviderCybersource(models.Model):
    _inherit = 'payment.provider'

    code = fields.Selection(
        selection_add=[('aps', "Cybersource")]
    )
    aps_merchant_ids = fields.Char(
        string="APS Merchant Identifier",
        help="The code of the merchant account to use with this provider.",
    )
    aps_api_key_id = fields.Char(
        string="APS Api Access",
        help="The access code associated with the merchant account.",
        groups='base.group_system',
    )
    aps_secret_key = fields.Char(
        string="APS secret key",
        groups='base.group_system',
    )




class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def capture_payment_cybersource(self):
        self.ensure_one()
        order = self

        url = "https://apitest.cybersource.com/pts/v2/payments"
        payload = {
            "clientReferenceInformation": {
                "code": "TC50171_3"
            },
            "paymentInformation": {
                "card": {
                    "number": "4111111111111111",
                    "expirationMonth": "12",
                    "expirationYear": "2031"
                }
            },
            "orderInformation": {
                "amountDetails": {
                    "totalAmount": self.amount_total,
                    "currency": "USD"
                },
                "billTo": {
                    "firstName": "John",
                    "lastName": "Doe",
                    "address1": "1 Market St",
                    "locality": "san francisco",
                    "administrativeArea": "CA",
                    "postalCode": "94105",
                    "country": "US",
                    "email": "admin@example.com",  # Replace with a valid email address
                    "phoneNumber": "4158880000"
                }
            }
        }

        # Prepare the headers
        # merchant_id = "brainvire8228_1720525512"
        # key_id = '07a3a924-deb1-426e-9abc-27a5d52bfb4b'
        # secret_key = 'LwVpApiEBGnirIvYripMfvXVk/SQ1H0Iaq4wHWUXgm0='
        merchant_id = "durgarao8228_1720677730"
        key_id = '214b048e-90ab-41c6-bc6b-91893867149b'
        secret_key = 'B0628Et5LcHrRO2d5Oc4l7QwNzKPW78yAScRqhBaM6E='
        timestamp = datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
        digest = base64.b64encode(hashlib.sha256(json.dumps(payload).encode('utf-8')).digest()).decode('utf-8')

        signature_header = f"host: apitest.cybersource.com\nv-c-date: {timestamp}\nrequest-target: post /pts/v2/payments\ndigest: SHA-256={digest}\nv-c-merchant-id: {merchant_id}"

        signature = base64.b64encode(
            hmac.new(base64.b64decode(secret_key), signature_header.encode('utf-8'), hashlib.sha256).digest()
        ).decode('utf-8')

        signature = f'keyid="{key_id}", algorithm="HmacSHA256", headers="host v-c-date request-target digest v-c-merchant-id", signature="{signature}"'

        headers = {
            'host': "apitest.cybersource.com",
            'v-c-date': timestamp,
            'digest': f"SHA-256={digest}",
            'v-c-merchant-id': merchant_id,
            'signature': signature,
            'Content-Type': 'application/json'
        }

        response = requests.post(url, json=payload, headers=headers)
        print(response)

        if response.status_code == 201:
            # self.message_post(body="Payment successfully captured via CyberSource.")
            sale = self.action_confirm()
            print("->>>>>>self", self)
            # print("->>>>>>sale", sale)
            #
            invoice = self._create_invoices()
            print("->>>>>>invoice", invoice)
            # invoice.action_post()
            # # # invoice.send_email_to_customer()
            # payment_transaction = self.env['payment.transaction'].create({
            #     'amount': self.amount_total,
            #     'acquirer_reference': response.json().get('id'),
            #     'currency_id': self.currency_id.id,
            #     'reference': self.name,
            #     'sale_order_ids': [(6, 0, [self.id])]
            # })
            # payment_transaction._set_transaction_done()
        else:
            self.message_post(body=f"Failed to capture payment: {response.text}")

        return True
# class Cybersource(models.Model):
#     _inherit = "payment.provider"
#
#     aps_merchant_ids = fields.Char(string="APS Merchant Identifier")
#     aps_api_key_id = fields.Char(string="APS Api Access")
#     aps_secret_key = fields.Char(string="APS secret key")


# class SaleOrder(models.Model):
#     _inherit = "sale.order"
#
#     def get_digest(self, payload):
#         hashobj = hashlib.sha256()
#         hashobj.update(json.dumps(payload).encode('utf-8'))
#         hash_data = hashobj.digest()
#         digest = base64.b64encode(hash_data).decode('utf-8')
#         return digest
#
#     def get_signature(self, method, resource, timestamp, digest, api_key_id, secret_key, merchant_id):
#         host = "apitest.cybersource.com"
#         headers_to_sign = [
#             f"(request-target): {method.lower()} {resource}",
#             f"host: {host}",
#             f"date: {timestamp}",
#             f"digest: SHA-256={digest}",
#             f"v-c-merchant-id: {merchant_id}"
#         ]
#         signature_str = "\n".join(headers_to_sign).encode('utf-8')
#         decoded_secret_key = base64.b64decode(secret_key)
#         hash_value = hmac.new(decoded_secret_key, signature_str, hashlib.sha256)
#         signature = base64.b64encode(hash_value.digest()).decode('utf-8')
#
#         auth_header = f'keyid="{api_key_id}", algorithm="HmacSHA256", headers="(request-target) host date digest v-c-merchant-id", signature="{signature}"'
#         return auth_header
#
#     def action_capture_in_cybersource(self):
#         self.ensure_one()
#         if not self.partner_id.email:
#             raise UserError('Customer email is required to process the payment.')
#
#         # Cybersource credentials and endpoint
#         merchant_id = 'namanjain2002_1720527590'
#         api_key_id = 'e0ecf9b4-23a1-42b8-a79e-d852600f5e5a'
#         secret_key = "LGGe3+rS8fJvtKXwatUNuO6EOUy4WRvDPo/uZ/2lslI="
#         cybersource_url = 'https://apitest.cybersource.com/pts/v2/payments'
#
#         # Payment data
#         payment_data = {
#             "clientReferenceInformation": {
#                 "code": "TC50171_3"
#             },
#             "paymentInformation": {
#                 "card": {
#                     "number": "4111111111111111",
#                     "expirationMonth": "12",
#                     "expirationYear": "2031"
#                 }
#             },
#             "orderInformation": {
#                 "amountDetails": {
#                     "totalAmount": "102.21",
#                     "currency": "USD"
#                 },
#                 "billTo": {
#                     "firstName": "John",
#                     "lastName": "Doe",
#                     "address1": "1 Market St",
#                     "locality": "san francisco",
#                     "administrativeArea": "CA",
#                     "postalCode": "94105",
#                     "country": "US",
#                     "email": "test@cybs.com",
#                     "phoneNumber": "4158880000"
#                 }
#             }
#         }
#
#         # Generate the HTTP signature headers
#         timestamp = time.strftime('%a, %d %b %Y %H:%M:%S GMT', time.gmtime())
#         digest = self.get_digest(payment_data)
#         resource = "/pts/v2/payments"
#         method = "POST"
#         signature = self.get_signature(method, resource, timestamp, digest, api_key_id, secret_key, merchant_id)
#
#         headers = {
#             'v-c-merchant-id': merchant_id,
#             'date': timestamp,
#             'host': 'apitest.cybersource.com',
#             'digest': f'SHA-256={digest}',
#             'signature': signature,
#             'content-Type': 'application/json'
#         }
#
#         try:
#             response = requests.post(cybersource_url, headers=headers, data=json.dumps(payment_data))
#
#             if response.status_code == 201:
#                 self.message_post(body="Payment successfully captured in Cybersource.")
#                 self.action_confirm()
#
#                 # Update the invoicing policy for the products to 'Ordered Quantities'
#                 for line in self.order_line:
#                     if line.product_id.type in ['consu', 'product']:
#                         line.product_id.write({'invoice_policy': 'order'})
#                     else:
#                         line.product_id.write({'invoice_policy': 'prepaid'})
#
#                 invoice = self._create_invoices()
#                 invoice.action_post()
#                 payment_transaction = self.env['payment.transaction'].create({
#                     'amount': self.amount_total,
#                     'acquirer_reference': response.json().get('id'),
#                     'currency_id': self.currency_id.id,
#                     'acquirer_id': self.env.ref('payment.payment_acquirer_cybersource').id,
#                     'reference': self.name,
#                     'sale_order_ids': [(6, 0, [self.id])]
#                 })
#                 payment_transaction._set_transaction_done()
#             else:
#                 raise UserError(f"Failed to capture payment in Cybersource: {response.text}")
#
#         except Exception as e:
#             raise UserError(f"Failed to connect to Cybersource API: {str(e)}")

# class SaleOrder(models.Model):
#     _inherit = "sale.order"
#
#     def get_digest(self, payload):
#         hashobj = hashlib.sha256()
#         hashobj.update(json.dumps(payload).encode('utf-8'))
#         hash_data = hashobj.digest()
#         digest = base64.b64encode(hash_data)
#         return digest
#
#     def get_signature(method, resource, time, digest, api_key_id=None):
#         # Getting HTTP Signature
#         header_list = ([])
#
#         # Key id is the key obtained from EBC
#         header_list.append("keyid=\"" + str(api_key_id) + "\"")
#         header_list.append(", algorithm=\"HmacSHA256\"")
#
#         postheaders = "host date request-target digest v-c-merchant-id"
#         header_list.append(", headers=\"" + postheaders + "\"")
#
#         signature_list = ([])
#
#         # This method adds the host header
#         signature_list.append("host: " + request_host + "\n")
#
#         # This method adds the date header
#         signature_list.append("date: " + time + "\n")
#
#         # This method adds the request target
#         signature_list.append("request-target: ")
#
#         request_target = method + " " + resource
#         signature_list.append(request_target + "\n")
#
#         # This method adds the digest header only for post
#         signature_list.append("digest: SHA-256=" + digest + "\n")
#
#         # This method adds the v-c-merchant-id header
#         signature_list.append("v-c-merchant-id: " + 'namanjain2002_1720527590')
#         print("->>>>>>>signature_list", signature_list)
#
#         sig_value = "".join(signature_list)
#
#         sig_value_string = str(sig_value)
#         sig_value_utf = bytes(sig_value_string, encoding='utf-8')
#
#         secret = base64.b64decode('LGGe3+rS8fJvtKXwatUNuO6EOUy4WRvDPo/uZ/2lslI=')
#
#         hash_value = hmac.new(secret, sig_value_utf, hashlib.sha256)
#
#         signature = base64.b64encode(hash_value.digest()).decode("utf-8")
#
#         header_list.append(", signature=\"" + signature + "\"")
#         token = ''.join(header_list)
#         print("->>>>>>>>token", token)
#         return token
#
#     def action_capture_in_cybersource(self):
#         self.ensure_one()
#         if not self.partner_id.email:
#             raise UserError('Customer email is required to process the payment.')
#
#         # Cybersource credentials and endpoint
#         merchant_id = 'namanjain2002_1720527590'
#         api_key_id = 'e0ecf9b4-23a1-42b8-a79e-d852600f5e5a'
#         secret_key = "LGGe3+rS8fJvtKXwatUNuO6EOUy4WRvDPo/uZ/2lslI="
#         cybersource_url = 'https://apitest.cybersource.com/pts/v2/payments'
#
#         # Payment data
#         payment_data = {
#             "clientReferenceInformation": {
#                 "code": "TC50171_3"
#             },
#             "paymentInformation": {
#                 "card": {
#                     "number": "4111111111111111",
#                     "expirationMonth": "12",
#                     "expirationYear": "2031"
#                 }
#             },
#             "orderInformation": {
#                 "amountDetails": {
#                     "totalAmount": "102.21",
#                     "currency": "USD"
#                 },
#                 "billTo": {
#                     "firstName": "John",
#                     "lastName": "Doe",
#                     "address1": "1 Market St",
#                     "locality": "san francisco",
#                     "administrativeArea": "CA",
#                     "postalCode": "94105",
#                     "country": "US",
#                     "email": "test@cybs.com",
#                     "phoneNumber": "4158880000"
#                 }
#             }
#         }
#
#         # Generate the HTTP signature headers
#         timestamp = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
#         request_target = "post /pts/v2/payments"
#         digest = self.get_digest(payment_data)  # Using the get_digest function
#         headers_to_sign = [
#             f"(request-target): {request_target}",
#             f"host: apitest.cybersource.com",
#             f"date: {timestamp}",
#             f"digest: SHA-256={digest.decode('utf-8')}"  # Decode Base64 to string
#         ]
#         signature_str = "\n".join(headers_to_sign).encode('utf-8')
#         signature = self.get_signature(method, resource, time, digest, api_key_id=None)
#
#         headers = {
#             'v-c-merchant-id': merchant_id,
#             'v-c-date': "Wed, 10 Jul 2024 12:24:26 GMT",
#             'host': 'apitest.cybersource.com',
#             'digest': f'SHA-256={digest.decode("utf-8")}',
#             'signature': f'keyid="{api_key_id}", algorithm="HmacSHA256", headers="(request-target) host date digest", signature="{signature}"',
#             'content-Type': 'application/json',
#             "authorization": "HmacSHA256"
#         }
#
#         try:
#             print("->>>>>>>cybersource_url", cybersource_url)
#             print("->>>>>>>headers", headers)
#             print("->>>>>>>data", json.dumps(payment_data))
#             # Send the request to Cybersource
#             response = requests.request("POST", cybersource_url, headers=headers, data=json.dumps(payment_data))
#             print("->>>>>>>response", response)
#
# if response.status_code == 201:
#     self.message_post(body="Payment successfully captured in Cybersource.")
#     self.action_confirm()
#     invoice = self._create_invoices()
#     invoice.action_post()
#     payment_transaction = self.env['payment.transaction'].create({
#         'amount': self.amount_total,
#         'acquirer_reference': response.json().get('id'),
#         'currency_id': self.currency_id.id,
#         'acquirer_id': self.env.ref('payment.payment_acquirer_cybersource').id,
#         'reference': self.name,
#         'sale_order_ids': [(6, 0, [self.id])]
#     })
#     payment_transaction._set_transaction_done()
# else:
#     raise UserError(f"Failed to capture payment in Cybersource: {response.text}")
#
#         except Exception as e:
#             raise UserError(f"Failed to connect to Cybersource API: {str(e)}")
