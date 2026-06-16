from odoo import models, fields

class Zapato(models.Model):
    _inherit = 'zapatos.zapato'

    temporada = fields.Selection([
        ('primavera', 'Primavera'),
        ('verano', 'Verano'),
        ('otono', 'Otoño'),
        ('invierno', 'Invierno')
    ], string='Temporada', default='verano', required=True)