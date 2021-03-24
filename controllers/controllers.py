# -*- coding: utf-8 -*-
from odoo import http

# class ThInvoicePartnerBankId(http.Controller):
#     @http.route('/th_invoice_partner_bank_id/th_invoice_partner_bank_id/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/th_invoice_partner_bank_id/th_invoice_partner_bank_id/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('th_invoice_partner_bank_id.listing', {
#             'root': '/th_invoice_partner_bank_id/th_invoice_partner_bank_id',
#             'objects': http.request.env['th_invoice_partner_bank_id.th_invoice_partner_bank_id'].search([]),
#         })

#     @http.route('/th_invoice_partner_bank_id/th_invoice_partner_bank_id/objects/<model("th_invoice_partner_bank_id.th_invoice_partner_bank_id"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('th_invoice_partner_bank_id.object', {
#             'object': obj
#         })