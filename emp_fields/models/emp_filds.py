# -*- coding: utf-8 -*-

from odoo import models, fields, api


class employee_fields(models.Model):
    _inherit = 'hr.employee'
    elhadaf = fields.Char(string="الهدف", required=False, )
    perc_hadaf = fields.Char(string="نسبة الهدف(%)", required=False, )
    sales_total = fields.Char(string="مبلغ المبيعات", required=False, )
    perc_sales_total = fields.Char(string="نسبة المبيعات(%)", required=False, )
    estehsal = fields.Char(string="مبلغ الاستحصال", required=False, )
    perc_estehsal =fields.Selection(string=" نسبة الاستحصال(%)", selection=[('25%', '25%'), ('50%', '50%'),('75%', '75%'),('1%', '1%'),('2%', '2%') ], required=False, )
    job_name = fields.Text(string="المسمي الوظيفي", required=False, )
    elahad = fields.Char(string="العهد", required=False, )
    instrument_no = fields.Char(string="Instrument No", required=False, )
    amount = fields.Char(string="amount", required=False, )
    notes = fields.Text(string="الملاحظات", required=False, )
    wosolat_ids = fields.One2many(comodel_name="wosolat.wosolat", inverse_name="emp_ids", string="دفتر الوصولات", required=False, )
    solaf_ids = fields.One2many(comodel_name="solaf.solaf", inverse_name="emp_ids", string="السلف", required=False, )
    emp_address = fields.Char(string="Address", required=False, )
    emp_country_id = fields.Many2one('res.country', string='Country')
    passport_no = fields.Integer(string="Passport No", required=False, )
    emp_date_of_birth = fields.Date(string=" Date Of Birth", required=False, )
    emp_place_of_birth = fields.Char(string=" Blace Of Birth", required=False, )
    emp_country_of_birth = fields.Many2one('res.country', string='Country Of Birth')




class wosolat(models.Model):
    _name = 'wosolat.wosolat'
    from1 = fields.Float(string="من",  required=False, )
    to1 = fields.Float(string="الي",  required=False, )
    date1 = fields.Date(string=" تاريخ الاستلام", required=False, )
    emp_ids = fields.Many2one(comodel_name="hr.employee", string="", required=False, )

class solaf(models.Model):
    _name = 'solaf.solaf'
    solaf = fields.Char(string="  مبلغ السلفة", required=False, )
    kest = fields.Char(string="القسط الشهري", required=False, )

    date1 = fields.Date(string=" تاريخ تسليم السلفة", required=False, )
    date2 = fields.Date(string=" تاريخ إنتهاء السلفة", required=False, )
    emp_ids = fields.Many2one(comodel_name="hr.employee", string="", required=False, )