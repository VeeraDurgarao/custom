{
    'name': 'Bank Management',
    'version': '1.0',
    'summary': 'Bank Management System',
    'depends': ['base', 'mail', 'sale', 'stock', 'planning', 'web', 'hr_expense','website','web_gantt'],
    'data': ['security/ir.model.access.csv',
             'security/recycle_account_groups.xml',
             # 'security/recycle_account_record_rules.xml',
             'data/CusSeq.xml',
             'data/EmailTemplate.xml',
             'data/schedule_action.xml',
             'data/CustomerEmailTemplate.xml',
             'data/monthly_excel_report.xml',
             'wizard/demo.xml',
             'wizard/print.xml',
             'wizard/xlReport.xml',
             'reports/bank.template.xml',
             'reports/sale.commision-qweb.xml',
             'reports/customerPDF.xml',
             'views/customer.xml',
             'views/employee.xml',
             'views/account.xml',
             'views/loan.xml',
             'views/menu_view.xml',
             'views/transaction1.xml',
             'views/query.xml',
             'views/sale_report.xml',
             'views/branch.xml',
             'views/kanbana.xml',
             'views/recycle.xml',
             'views/sale_order_commission_view.xml',
             'views/sale_line_oreder_commission.xml',
             'views/sale_inheritate_menu.xml',
             'views/practice.xml',
             ],
    'assets': {
        'web.assets_backend': [
            'bank/static/src/view/js/planning_button.js',
            'bank/static/src/view/js/practice.js',
            'bank/static/src/view/js/expense_button.js',
            'bank/static/src/view/js/custome_module_button.js',
            # 'bank/static/src/view/js/custom_controller.js',
            'bank/static/src/view/js/control.js',
            'bank/static/src/view/js/icon.js',
            'bank/static/src/view/js/manifest.js',
            'bank/static/src/view/xml/temp.xml',
            'bank/static/src/view/xml/expense_button.xml',
            'bank/static/src/view/xml/dummy.xml',
            'bank/static/src/view/xml/custome_module_button.xml',
            # 'bank/static/src/view/xml/custom_controller.xml',
            'bank/static/src/view/xml/temp123.xml',
'bank/static/src/view/js/public_widget.js',
            'bank/static/src/view/xml/js_template.xml',



        ],
        'web.assets_frontend': [
            'bank/static/src/view/js/purchases_example.js',
            'bank/static/src/view/js/first.js',




        ]
    },

    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',

}
