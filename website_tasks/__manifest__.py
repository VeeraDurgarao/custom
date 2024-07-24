{
    'name': 'Custom Website Product Categories',
    'summary': 'Display all product categories on a custom webpage',
    'description': """
        This module creates a new webpage to display all product categories.
    """,
    'author': 'Durgarao',
    'category': 'Website',
    'version': '1.0',
    'depends': ['base', 'website_sale','website'],
    'data': [
        'views/product_category.xml',
    ],
    'installable': True,
    'application': True,
}
