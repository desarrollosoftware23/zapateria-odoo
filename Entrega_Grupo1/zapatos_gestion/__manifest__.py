{
    'name': 'Gestión de Zapatería',
    'version': '1.0',
    'summary': 'Módulo independiente para la gestión de calzado',
    'description': 'Control de inventario avanzado conectado directamente al módulo zapatos.',
    'author': 'Mateo',
    'category': 'Sales',
    'license': 'LGPL-3',
    'depends': ["base", "zapatos"], 
    'data': [
        'security/ir.model.access.csv',
        'views/zapato_gestion_views.xml',
    ],
    'installable': True,
    'application': True,
}