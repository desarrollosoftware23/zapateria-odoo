from odoo import models, fields

class ZapatoPersonalizacion(models.Model):
    _name = 'zapato.personalizacion'
    _description = 'Personalización de Zapatos'

    name = fields.Char(string='Nombre de la Personalización', required=True)
    description = fields.Text(string='Descripción')
    precio = fields.Float(string='Precio Adicional', required=True)
    imagen = fields.Binary(string="Diseño de Referencia")
    zapato_id = fields.Many2one('zapatos.zapato', string='Zapato Base', required=True)
    color = fields.Char(string='Color Original', related='zapato_id.color', readonly=True)
    material = fields.Char(string='Material Original', related='zapato_id.material', readonly=True)
    talla = fields.Integer(string='Talla Original', related='zapato_id.talla', readonly=True)
    calificacion = fields.Selection([
        ('0', 'Sin Calificar'),
        ('1', 'Muy Bajo'),
        ('2', 'Bajo'),
        ('3', 'Medio'),
        ('4', 'Alto'),
        ('5', 'Excelente')
    ], string="Calidad", default='0')