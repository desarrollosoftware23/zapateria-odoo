from odoo import models, fields

class ZapatosCliente(models.Model):
    _name = 'zapatos.cliente'
    _description = 'Cliente de Zapatería'

    name = fields.Char(string='Nombre completo', required=True)
    cedula = fields.Char(string='Cédula o identificación')
    telefono = fields.Char(string='Teléfono')
    email = fields.Char(string='Correo electrónico')
    direccion = fields.Text(string='Dirección')
    fecha_registro = fields.Date(string='Fecha de registro', default=fields.Date.context_today)
    zapato_id = fields.Many2one('zapatos.zapato', string='Zapato de interés')