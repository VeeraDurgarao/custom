{
    'name': 'Practice module',
    'version': '1.0',
    'depends': ['base','sale', 'web',],
    'data': ['security/ir.model.access.csv',
        'views/many_to_one.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',

}
