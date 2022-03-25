# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class iq_alraya_custom(models.Model):
#     _name = 'iq_alraya_custom.iq_alraya_custom'
#     _description = 'iq_alraya_custom.iq_alraya_custom'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
