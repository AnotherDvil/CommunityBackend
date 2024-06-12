# -*- coding: utf-8 -*-
# from odoo import http


# class Community(http.Controller):
#     @http.route('/community/community', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/community/community/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('community.listing', {
#             'root': '/community/community',
#             'objects': http.request.env['community.community'].search([]),
#         })

#     @http.route('/community/community/objects/<model("community.community"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('community.object', {
#             'object': obj
#         })
