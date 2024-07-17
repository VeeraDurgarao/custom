{
    'name': 'pos tasks',
    'version': '1.0',
    'depends': ['base','sale', 'web','point_of_sale',],
    'data': [
        'views/connect_backend.xml',
        'views/location.xml',
        'views/pos_config.xml',
    ],
'assets': {
        'point_of_sale._assets_pos': [
            'pos_tasks/static/src/js/addnote.js',
            'pos_tasks/static/src/js/clear.js',
            'pos_tasks/static/src/js/discount.js',
            'pos_tasks/static/src/js/location_button.js',
            'pos_tasks/static/src/js/location_screen.js',
            'pos_tasks/static/src/js/sundry_customer.js',

            'pos_tasks/static/src/xml/addnote.xml',
            'pos_tasks/static/src/xml/clear.xml',
            'pos_tasks/static/src/xml/discount.xml',
            'pos_tasks/static/src/xml/location_button.xml',
            'pos_tasks/static/src/xml/location_screen.xml',
            'pos_tasks/static/src/xml/sundry_customer.xml',

        ],
    },
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',

}
