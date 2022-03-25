# -*- coding: utf-8 -*-
# from odoo import http


# class IqAlrayaCustom(http.Controller):
#     @http.route('/iq_alraya_custom/iq_alraya_custom/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/iq_alraya_custom/iq_alraya_custom/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('iq_alraya_custom.listing', {
#             'root': '/iq_alraya_custom/iq_alraya_custom',
#             'objects': http.request.env['iq_alraya_custom.iq_alraya_custom'].search([]),
#         })

#     @http.route('/iq_alraya_custom/iq_alraya_custom/objects/<model("iq_alraya_custom.iq_alraya_custom"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('iq_alraya_custom.object', {
#             'object': obj
#         })
