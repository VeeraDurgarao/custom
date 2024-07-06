{
    'name': 'POS Bag Types',
    'version': '1.0',
    'category': 'Sales/Point of Sale',
    'sequence': 6,
    'summary': 'Simple POS Demo',
    'description': """
    """,
    'depends': ['point_of_sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/bag_charges.xml',
        'views/config.xml',
    ],

    'installable': True,
    'assets': {
        'point_of_sale.assets': [
            'pos_bag_types/static/src/js/**/*',
        ],
        'web.assets_qweb': [
            'pos_bag_types/static/src/xml/**/*',
        ],
    },
    'license': 'LGPL-3',
}
