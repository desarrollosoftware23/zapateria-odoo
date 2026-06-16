{
    'name': 'zapatos_clientes',
    'version': '1.0',
    'summary': 'Módulo de clientes para zapatería',
    'description': 'Gestión de clientes vinculados a zapatos.',
    'author': 'Anderson',
    'category': 'Sales',
    'license': 'LGPL-3',
    'depends': ['zapatos'],
    'data': [
        'security/ir.model.access.csv',
        'views/zapatos_clientes_views.xml',
    ],
    'installable': True,
    'application': True,
}
