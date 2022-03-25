# -*- coding: utf-8 -*-

from odoo import models, fields, api


class iq_inherit_po(models.Model):
    _inherit = 'purchase.order'
    
   
    def _get_po_default_branch(self):
        user_obj = self.env['res.users']
        iq_po_branch = user_obj.browse(self.env.user.id).f_defaultpo_branch.id
        return iq_po_branch
    
    
    
    iq_po_branch = fields.Many2one('iq.po.branches',string='Section',required=True,default=_get_po_default_branch)
    iq_cost_wo = fields.Float( string='Workers Cost')
    iq_cost_en = fields.Float( string='Internal Transfer Cost')
    iq_cost_ex = fields.Float( string='External Transfer Cost')
    iq_cost_tx = fields.Float( string='Taxes Cost')
    iq_cost = fields.Float( string='Cost')
    iq_total_original_cost = fields.Float(string="Total Original Price", required=False, compute="_iq_total_original_cost")
    
    iq_po_branch_cat1 = fields.Many2one('iq.po.branches.cat1',string='Transport Type')
    iq_po_branch_cat2 = fields.Many2one('iq.po.branches.cat2',string='Port Name')
    iq_is_import = fields.Boolean(compute="get_type",string="Is Import")
    
    
    def get_type(self):
        self.iq_is_import = self.iq_po_branch.iq_is_import
    
    
    
    
    
    
    
    
    @api.onchange('iq_po_branch')
    def iq_check_branch(self):
        print("11111")
        ldl= []
        zo= self.env['iq.po.branches'].search([('active','=',True)])
        print("zzzzzzz",zo)
        for x in zo :
                if x.id in self.env.user.f_po_branch.ids :
                    ldl.append(x.id)
                
        domain_on_types=[('id' ,'in',ldl)]
        
        self.iq_is_import = self.iq_po_branch.iq_is_import
        
            
            
        return {'domain': {'iq_po_branch': domain_on_types}}
    
    
    
    
    def _prepare_invoice(self):
        res = super(iq_inherit_po, self)._prepare_invoice()
        res['iq_po_branch'] = self.iq_po_branch.id
        res['iq_cost_wo'] = self.iq_cost_wo
        res['iq_cost_en'] = self.iq_cost_en
        res['iq_cost_ex'] = self.iq_cost_ex
        res['iq_cost_tx'] = self.iq_cost_tx
        res['iq_cost'] = self.iq_cost
        res['iq_total_original_cost'] = self.iq_total_original_cost
        return res
    
    
    def _iq_total_original_cost(self):
        for price_line in self :
            prices_sum = 0
            for coun in price_line.order_line :
                prices_sum = prices_sum + (coun.iq_original_price_unit*coun.product_qty)
            price_line.iq_total_original_cost = prices_sum
            
            
            
    @api.onchange('iq_cost')
    def onchange_iq_cost(self):
        if self.amount_total != 0:
            cost_iq_meas = self.iq_cost/self.amount_total
            for rec in self.order_line:
                if cost_iq_meas != 0 :
                    rec.price_unit = (rec.price_unit*cost_iq_meas ) +rec.price_unit
                # else:
                rec.iq_original_price_unit = rec.product_id.standard_price
                
                
    @api.onchange('iq_cost_tx')
    def onchange_tx_cost(self):
        if self.amount_total != 0:
            cost_iq_meas = self.iq_cost_tx/self.amount_total
            for rec in self.order_line:
                if cost_iq_meas != 0 :
                    rec.price_unit = (rec.price_unit*cost_iq_meas ) +rec.price_unit
                # else:
                rec.iq_original_price_unit = rec.product_id.standard_price
                
                
                
    @api.onchange('iq_cost_ex')
    def onchange_ex_cost(self):
        if self.amount_total != 0:
            cost_iq_meas = self.iq_cost_ex/self.amount_total
            for rec in self.order_line:
                if cost_iq_meas != 0 :
                    rec.price_unit = (rec.price_unit*cost_iq_meas ) +rec.price_unit
                # else:
                rec.iq_original_price_unit = rec.product_id.standard_price
                
                
                
    @api.onchange('iq_cost_en')
    def onchange_iq_en_cost(self):
        if self.amount_total != 0:
            cost_iq_meas = self.iq_cost_en/self.amount_total
            for rec in self.order_line:
                if cost_iq_meas != 0 :
                    rec.price_unit = (rec.price_unit*cost_iq_meas ) +rec.price_unit
                # else:
                rec.iq_original_price_unit = rec.product_id.standard_price
                
                
                
    @api.onchange('iq_cost_wo')
    def onchange_iq_cost_wo(self):
        if self.amount_total != 0:
            cost_iq_meas = self.iq_cost_wo/self.amount_total
            for rec in self.order_line:
                if cost_iq_meas != 0 :
                    rec.price_unit = (rec.price_unit*cost_iq_meas ) +rec.price_unit
                # else:
                rec.iq_original_price_unit = rec.product_id.standard_price
                
                            
            
class iq_inherit_po_lines(models.Model):
    _inherit = 'purchase.order.line'

    iq_original_price_unit = fields.Float('Original Unit Price',  digits='Product Price', default=0.0)
    
    
    @api.onchange('product_id')
    def onchange_method(self):
        #self.price_unit = self.product_id.lst_price
        self.iq_original_price_unit = self.product_id.standard_price
        
        
        
    def _prepare_account_move_line(self, move=False):
        print("11111111111111")
        res = super(iq_inherit_po_lines, self)._prepare_account_move_line()
        res['iq_original_price_unit'] = self.iq_original_price_unit
   
        return res
        
        
        
        
            
            
