from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Pedido(models.Model):
    _name = 'pedido.pedido'
    _description = 'Pedido de Zapatos'
    _order = 'fecha_pedido desc, id desc'

    name = fields.Char(
        string='ID de pedido',
        required=True,
        copy=False,
        readonly=True,
        default='Nuevo',
    )
    zapato_id = fields.Many2one(
        'zapatos.zapato',
        string='Zapato solicitado',
        required=True,
    )
    proveedor = fields.Char(string='Nombre del proveedor', required=True)
    fecha_pedido = fields.Date(
        string='Fecha de pedido',
        default=fields.Date.context_today,
        required=True,
    )
    cantidad_solicitada = fields.Integer(
        string='Cantidad solicitada',
        default=1,
        required=True,
    )
    estado = fields.Selection(
        selection=[
            ('pendiente', 'Pendiente'),
            ('recibido', 'Recibido'),
        ],
        string='Estado del pedido',
        default='pendiente',
    )

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', 'Nuevo') == 'Nuevo':
                vals['name'] = self.env['ir.sequence'].next_by_code('pedido.pedido') or 'Nuevo'
        return super(Pedido, self).create(vals_list)

    @api.constrains('cantidad_solicitada')
    def _verificar_cantidad(self):
        for pedido in self:
            if pedido.cantidad_solicitada <= 0:
                raise ValidationError('La cantidad solicitada debe ser mayor a cero.')
