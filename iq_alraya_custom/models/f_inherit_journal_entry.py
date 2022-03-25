
# -*- coding: utf-8 -*-

from odoo import models, fields, api

class iq_AccountMoveEntryInherit(models.Model):

    _inherit = 'account.move'
    
    
    


    @api.onchange('line_ids', 'line_ids.account_id')
    def _get_price(self):
        print("11111")
        if self.move_type == 'entry':
            for x in self.line_ids:
                self.currency_id = x.account_id.currency_id.id
            
        
        
        


class iq_AccountMovejournalEntryInherit(models.Model):

    _inherit = 'account.move.line'
    
    @api.onchange('account_id')
    def _get_currency_id(self):
        
        print("111111",self.move_id,self.move_id.move_type,self.move_id.currency_id.id,"account",self.account_id.currency_id.id)
        if self.move_id.move_type == 'entry':
            self.currency_id = self.account_id.currency_id.id
            self.move_id.currency_id = self.account_id.currency_id.id
            print(self.move_id.currency_id,"ciuu")
    
    
    
    