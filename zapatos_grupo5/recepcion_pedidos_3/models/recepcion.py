from odoo import models, fields, api
from odoo.exceptions import ValidationError


class RecepcionPedido(models.Model):
    _name = 'recepcion.pedido'
    _description = 'Recepción de Pedido'
    _order = 'fecha_recepcion desc, id desc'

    name = fields.Char(
        string='ID de recepción',
        required=True,
        copy=False,
        readonly=True,
        default='Nuevo',
    )
    pedido_id = fields.Many2one(
        'pedido.pedido',
        string='ID de pedido',
        required=True,
        domain="[('estado', '=', 'pendiente')]",
    )

    zapato_id = fields.Many2one(
        'zapatos.zapato',
        string='Zapato solicitado',
        related='pedido_id.zapato_id',
        store=True,
        readonly=True,
    )
    proveedor = fields.Char(
        string='Nombre del proveedor',
        related='pedido_id.proveedor',
        store=True,
        readonly=True,
    )
    fecha_pedido = fields.Date(
        string='Fecha de pedido',
        related='pedido_id.fecha_pedido',
        store=True,
        readonly=True,
    )
    cantidad_solicitada = fields.Integer(
        string='Cantidad solicitada',
        related='pedido_id.cantidad_solicitada',
        store=True,
        readonly=True,
    )
    fecha_recepcion = fields.Date(
        string='Fecha de recepción',
        default=fields.Date.context_today,
        required=True,
    )
    cantidad_recibida = fields.Integer(
        string='Cantidad recibida',
        default=0,
        required=True,
    )
    estado_recepcion = fields.Selection(
        selection=[
            ('completo', 'Completo'),
            ('incompleto', 'Incompleto'),
        ],
        string='Estado de recepción',
        compute='_calcular_estado_recepcion',
        store=True,
    )
    observacion = fields.Text(string='Observación')
    estado = fields.Selection(
        selection=[
            ('borrador', 'Borrador'),
            ('registrado', 'Registrado'),
        ],
        string='Estado',
        default='borrador',
    )

    @api.depends('cantidad_recibida', 'cantidad_solicitada')
    def _calcular_estado_recepcion(self):
        for recepcion in self:
            if recepcion.cantidad_recibida >= recepcion.cantidad_solicitada and recepcion.cantidad_recibida > 0:
                recepcion.estado_recepcion = 'completo'
            else:
                recepcion.estado_recepcion = 'incompleto'

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', 'Nuevo') == 'Nuevo':
                vals['name'] = self.env['ir.sequence'].next_by_code('recepcion.pedido') or 'Nuevo'
        return super(RecepcionPedido, self).create(vals_list)

    @api.constrains('cantidad_recibida')
    def _verificar_cantidad_recibida(self):
        for recepcion in self:
            if recepcion.cantidad_recibida < 0:
                raise ValidationError('La cantidad recibida no puede ser negativa.')

    @api.constrains('fecha_recepcion', 'fecha_pedido')
    def _verificar_fechas(self):
        for recepcion in self:
            if recepcion.fecha_recepcion and recepcion.fecha_pedido:
                if recepcion.fecha_recepcion < recepcion.fecha_pedido:
                    raise ValidationError(
                        'La fecha de recepción no puede ser anterior a la fecha del pedido.'
                    )

    def accion_registrar(self):
        for recepcion in self:
            if not recepcion.pedido_id:
                raise ValidationError('Debe seleccionar un pedido antes de registrar.')
            if recepcion.cantidad_recibida <= 0:
                raise ValidationError('Debe ingresar una cantidad recibida mayor a cero.')
            if not recepcion.fecha_recepcion:
                raise ValidationError('Debe indicar la fecha de recepción.')
            recepcion.zapato_id.stock += recepcion.cantidad_recibida
            recepcion.pedido_id.estado = 'recibido'
            recepcion.estado = 'registrado'

    def accion_borrador(self):
        self.write({'estado': 'borrador'})
