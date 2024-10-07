{
    'name': "Odoo Library",
    'version': '17.0.1.0.0',
    'author': 'Alis',
    'website': 'https://www.alis.com',
    'category': 'Customization',
    'license': 'OPL-1',
    'depends': ['base'],
    'external_dependencies': {
        'python': [],
    },
    'data': [
        'security/ir.model.access.csv',
        'wizard/library_add_reader_wizard_views.xml',

        'views/library_menu.xml',
        'views/library_book_views.xml',
    ],
    'demo': [
        'demo/res_partner_demo.xml',
        'demo/library.book.csv',
    ],
    'installable': True,
    'auto_install': False,
    'images': ['static/description/icon.png'],
}
