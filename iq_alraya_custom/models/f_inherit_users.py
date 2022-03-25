# -*- coding: utf-8 -*-

from odoo import models, fields, api


class iq_inherit_users(models.Model):
    _inherit = 'res.users'



    iq_defaultpjournal = fields.Many2one('account.journal' ,string='Default Journal')
    f_po_branch = fields.Many2many('iq.po.branches' ,string='Allowed Purchase Section')
    f_so_branch = fields.Many2many('iq.so.branches',string='Allowed Sale Section')
    
    
    f_defaultpo_branch = fields.Many2one('iq.po.branches' ,string='Default Purchase Section')
    f_defaultso_branch = fields.Many2one('iq.so.branches',string='Default Sale Section')
    
    f_recevielotnotfiy = fields.Boolean(string='Enable LOT Notification')
    
    
    
    iq_journals = fields.Many2many('account.journal' ,string='Allowed Journals')

    
    
    
    
    
    
    
  
    
   
