# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class ticket_merge(models.Model):
#     _name = 'ticket_merge.ticket_merge'
#     _description = 'ticket_merge.ticket_merge'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
