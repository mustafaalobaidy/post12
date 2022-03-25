
# -*- coding: utf-8 -*-

from odoo import models, fields, api


class iq_AccountMoveInherit(models.Model):

    _inherit = 'account.move'

    iq_employee = fields.Many2one('hr.employee', 'Employee' )
    iq_user = fields.Many2one('res.users', 'User' )
    iq_emp_dep = fields.Many2one('hr.department',related='iq_employee.department_id' )
    iq_amount = fields.Float('Amount' )
    iq_date = fields.Date('Date' )
    iq_contact = fields.Char('Contact Name')
    
    #sales
    iq_so_branch = fields.Many2one('iq.so.branches',string='SO Section')
    iq_so_cost = fields.Float( string='SO Cost')
    
    
    #purchase
    iq_po_branch = fields.Many2one('iq.po.branches',string='PO Section')
    iq_cost_wo = fields.Float( string='Workers Cost')
    iq_cost_en = fields.Float( string='Internal Transfer Cost')
    iq_cost_ex = fields.Float( string='External Transfer Cost')
    iq_cost_tx = fields.Float( string='Taxes Cost')
    iq_cost = fields.Float( string='PO Cost')
    iq_total_original_cost = fields.Float(string="Total Original Price", required=False, compute="_iq_total_original_cost")
    
    
    def _iq_total_original_cost(self):
        for price_line in self :
            prices_sum = 0
            for coun in price_line.invoice_line_ids :
                prices_sum = prices_sum + (coun.iq_original_price_unit*coun.quantity)
            price_line.iq_total_original_cost = prices_sum
            
            
  
            
            
    @api.onchange('iq_cost')
    def onchange_iq_cost(self):
        if self.amount_total != 0:
            cost_iq_meas = self.iq_cost/self.amount_total
            for rec in self.invoice_line_ids:
                if cost_iq_meas != 0 :
                    rec.price_unit = (rec.price_unit*cost_iq_meas ) +rec.price_unit
                # else:
                rec.iq_original_price_unit = rec.product_id.standard_price
                
                
    @api.onchange('iq_cost_tx')
    def onchange_tx_cost(self):
        if self.amount_total != 0:
            cost_iq_meas = self.iq_cost_tx/self.amount_total
            for rec in self.invoice_line_ids:
                if cost_iq_meas != 0 :
                    rec.price_unit = (rec.price_unit*cost_iq_meas ) +rec.price_unit
                # else:
                rec.iq_original_price_unit = rec.product_id.standard_price
                
                
                
    @api.onchange('iq_cost_ex')
    def onchange_ex_cost(self):
        if self.amount_total != 0:
            cost_iq_meas = self.iq_cost_ex/self.amount_total
            for rec in self.invoice_line_ids:
                if cost_iq_meas != 0 :
                    rec.price_unit = (rec.price_unit*cost_iq_meas ) +rec.price_unit
                # else:
                rec.iq_original_price_unit = rec.product_id.standard_price
                
                
                
    @api.onchange('iq_cost_en')
    def onchange_iq_en_cost(self):
        if self.amount_total != 0:
            cost_iq_meas = self.iq_cost_en/self.amount_total
            for rec in self.invoice_line_ids:
                if cost_iq_meas != 0 :
                    rec.price_unit = (rec.price_unit*cost_iq_meas ) +rec.price_unit
                # else:
                rec.iq_original_price_unit = rec.product_id.standard_price
                
                
                
    @api.onchange('iq_cost_wo')
    def onchange_iq_cost_wo(self):
        if self.amount_total != 0:
            cost_iq_meas = self.iq_cost_wo/self.amount_total
            for rec in self.invoice_line_ids:
                if cost_iq_meas != 0 :
                    rec.price_unit = (rec.price_unit*cost_iq_meas ) +rec.price_unit
                # else:
                rec.iq_original_price_unit = rec.product_id.standard_price
            
            
            
class iq_AccountMoveLINESInherit(models.Model):

    _inherit = 'account.move.line'
    
    
    
    iq_original_price_unit = fields.Float('Original Unit Price',  digits='Product Price', default=0.0)
    
    
    @api.onchange('product_id')
    def onchange_method(self):
        #self.price_unit = self.product_id.lst_price
        self.iq_original_price_unit = self.product_id.standard_price
            
            
            
    
    
    
    
    