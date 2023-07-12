# -*- coding: utf-8 -*-
# from odoo import http


# class TicketMerge(http.Controller):
#     @http.route('/ticket_merge/ticket_merge/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ticket_merge/ticket_merge/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ticket_merge.listing', {
#             'root': '/ticket_merge/ticket_merge',
#             'objects': http.request.env['ticket_merge.ticket_merge'].search([]),
#         })

#     @http.route('/ticket_merge/ticket_merge/objects/<model("ticket_merge.ticket_merge"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ticket_merge.object', {
#             'object': obj
#         })
