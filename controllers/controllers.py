# -*- coding: utf-8 -*-
from odoo import http

# class Fiches(http.Controller):
#     @http.route('/fiches/fiches/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fiches/fiches/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fiches.listing', {
#             'root': '/fiches/fiches',
#             'objects': http.request.env['fiches.fiches'].search([]),
#         })

#     @http.route('/fiches/fiches/objects/<model("fiches.fiches"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fiches.object', {
#             'object': obj
#         })