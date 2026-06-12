{
    'name': 'transporte',
    'version': '1.0',
    'summary': 'Negocio de transporte publico',
    'description': 'Modulo padre para el negocio de transporte publico',
    'author': 'Grupo_7',
    'category': 'Sales',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/transporte_views.xml',
    ],
    'installable': True,
    'application': True,
}