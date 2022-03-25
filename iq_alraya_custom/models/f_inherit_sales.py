# -*- coding: utf-8 -*-

from odoo import models, fields, api


class iq_inherit_sales(models.Model):
    _inherit = 'sale.order'
    
 
    def _get_sale_default_branch(self):
        print("1111111sale_branches")
        user_obj = self.env['res.users']
        iq_so_branch = user_obj.browse(self.env.user.id).f_defaultso_branch.id
        return iq_so_branch
    
    
    
    iq_so_branch = fields.Many2one('iq.so.branches',string='Section',required=True,default=_get_sale_default_branch)
    iq_cost = fields.Float( string='Cost')
    iq_so_type = fields.Selection([('customer','On Customer'),('compnay','On Company')],string='Apply Cost')
    
    
    
    
    
    
    
    
    
    @api.onchange('iq_so_branch')
    def iq_check_branch(self):
        print("11111")
        ldl= []
        zo=self.env['iq.so.branches'].search([('active','=',True)])
        print("zzzzzzz2222",zo)
        for x in zo :
                if x.id in self.env.user.f_so_branch.ids :
                    ldl.append(x.id)
                
        domain_on_types=[('id' ,'in',ldl)]
            
            
        return {'domain': {'iq_so_branch': domain_on_types}}
    
    
    def _prepare_invoice(self):
        res = super(iq_inherit_sales, self)._prepare_invoice()
        res['iq_so_branch'] = self.iq_so_branch.id
        res['iq_so_cost'] = self.iq_cost
        return res
    
    
  