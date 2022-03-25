# -*- coding: utf-8 -*-

from odoo import models, fields, api


class iq_po_branches(models.Model):
    _name = 'iq.po.branches'
    _rec_name = 'iq_name'
    
    iq_name = fields.Char('Name')
    active = fields.Boolean(default=True)
    iq_is_import = fields.Boolean(string="Is Import")
    
    
class iq_po_branches_cat1(models.Model):
    _name = 'iq.po.branches.cat1'
    _rec_name = 'iq_name'
    
    iq_name = fields.Char('Name')
    active = fields.Boolean(default=True)
    
    
class iq_po_branches_cat2(models.Model):
    _name = 'iq.po.branches.cat2'
    _rec_name = 'iq_name'
    
    iq_name = fields.Char('Name')
    active = fields.Boolean(default=True)
    
    
    
    
class iq_so_branches(models.Model):
    _name = 'iq.so.branches'
    _rec_name = 'iq_name'
    
    iq_name = fields.Char('Name')
    active = fields.Boolean(default=True)
