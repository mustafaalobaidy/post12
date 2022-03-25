# -*- coding: utf-8 -*-
{
    'name': "iq_alraya_custom",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','web','hr','sale','purchase','stock','product','account','mail','sale_stock','product_expiry'],

    # always loaded
    'data': [
         'security/ir.model.access.csv',

         'views/f_branches_so_po.xml',
          'views/f_inherit_users.xml',
         'views/f_inherit_account.xml',
         'views/f_inherit_po.xml',
         'views/f_inherit_sales.xml',
         'views/templates.xml',
         'security/f_inherit_so_po_rules.xml',
         'views/f_lot_wizard_expiry.xml',
         'views/f_report_expiry_lot.xml',
         'views/views.xml',
         'views/f_inherit_sale_picking.xml',
          'security/f_inherit_payment_entry.xml',
          'views/f_inherit_account_payemnt.xml',
          'views/f_inherit_stock_picking.xml',
          'views/f_inherit_production_date.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
