{
    'name': 'Recepción de Pedidos',
    'version': '18.0.1.0.0',
    'summary': 'Registro y control de la recepción de pedidos de zapatos',
    'description': """
Módulo para registrar la recepción de pedidos.
Se relaciona directamente con el pedido y hereda sus datos principales,
permite registrar la cantidad recibida, identifica si el pedido llegó
completo o incompleto, actualiza el inventario del catálogo de zapatos
y cambia el estado del pedido una vez registrada la recepción.
    """,
    'author': 'Grupo - Universidad UTE',
    'category': 'Inventory',
    'depends': ['base', 'zapatos'],
    'data': [
        'security/ir.model.access.csv',
        'data/secuencias.xml',
        'views/pedido_views.xml',
        'views/recepcion_views.xml',
        'views/menus.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
