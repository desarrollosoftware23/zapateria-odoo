from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ZapatosPadre(models.Model):
    _inherit = 'zapatos.zapato'

    garantias_meses = fields.Integer(string='Garantías en meses')

    devolucion_ids = fields.One2many('zapateria.devolucion','zapato_id',string='Devoluciones')

    garantia_ids = fields.One2many('zapateria.garantia','zapato_id',string='Garantías')


            
    @api.constrains('garantias_meses')
    def _check_garantias(self):
        for record in self:
            if record.garantias_meses <= 0:
                raise ValidationError("La garantía no puede ser negativa.")

class Devolucion(models.Model):
    _name = 'zapateria.devolucion'
    _description = 'Devoluciones'

    codigo = fields.Char(string='Código',required=True,readonly=True, default='Nuevo',copy=False)

    fecha = fields.Date(string='Fecha')

    motivo = fields.Text(string='Motivo',required=True)

    estado = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('aprobada', 'Aprobada'),
        ('rechazada', 'Rechazada') ], string='Estado')

    zapato_id = fields.Many2one('zapatos.zapato',string='Zapato',required=True)

    _sql_constraints = [
        (
            'codigo_unico',
            'unique(codigo)',
            'Ya existe una devolución con ese código.'
        )
    ]

    @api.constrains('motivo')
    def _check_motivo(self):
        for record in self:
            if not record.motivo or len(record.motivo.strip()) < 10:
                raise ValidationError("El motivo debe tener al menos 10 caracteres.")
        
    @api.constrains('fecha')
    def _check_fecha(self):
        for record in self:
            if record.fecha and record.fecha > fields.Date.today():
                raise ValidationError("La fecha de devolución no puede ser futura.")
