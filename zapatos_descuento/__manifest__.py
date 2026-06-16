{
    'name': 'Zapatos Descuento',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Módulo para aplicar descuentos automáticos en la venta de zapatos',
    'description': 'Implementa una regla de negocio que calcula automáticamente un precio de oferta con 15% de descuento cuando el inventario de un zapato es mayor a 30 unidades.',
    'author': 'JZAdy',
    'depends': ['zapatos'],
    'data': [
        'views/descuento_views.xml',
        'security/ir.model.access.csv'
    ],
    'installable': True,
} 