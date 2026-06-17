{
    'name': 'Zapatos - Proveedores y Categorias',
    'version': '1.0',
    'summary': 'Extension del modulo zapatos',
    'author': 'Marlon Garcia',
    'license': 'LGPL-3',

    'depends': ['zapatos'],

    'data': [
        'security/ir.model.access.csv',

        'views/proveedor_views.xml',
        'views/categoria_views.xml',
        'views/zapato_inherit_views.xml',
        'views/menus.xml',
    ],

    'installable': True,
    'application': True,
}