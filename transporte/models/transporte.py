from odoo import models, fields, api
from odoo.exceptions import ValidationError


class TransportePublico(models.Model):
    _name = 'transporte.publico'
    _description = 'Transporte Público'

    name = fields.Char(string='Nombre del Cliente', required=True)
    cedula = fields.Char(string='N° de Cédula', required=True)
    destino = fields.Selection([('atacames', 'Atacames'), ('cuenca', 'Cuenca'), ('guayaquil', 'Guayaquil'), ('loja', 'Loja'),
                             ('manta', 'Manta'), ('quito', 'Quito')], string='Lugar del destino', required=True)
    fecha = fields.Date(string='Fecha del viaje', default=fields.Date.today)
    tarifa = fields.Selection([
        ('turista', 'Turista 12.5$'),
        ('ejecutiva', 'Ejecutiva 25$'),
        ('vip', 'VIP 35.5$')],string='Tipo de Tarifa', required=True)
    tipo = fields.Selection([('bus', 'Bus'), ('metro', 'Metro'), ('avion', 'Avion')], string='Tipo de Transporte', required=True)
    pasajeros = fields.Integer(string='Número de Pasajeros', required=True)
    total_tarifa = fields.Float(string='Total de Tarifa', compute='tarifa_pasajeros', store=True)

    
    @api.constrains('name')
    def validar_name(self):
        for record in self:
            if record.name:
                if not record.name.replace(' ', '').isalpha():
                    raise ValidationError("EL nombre solo acepta letras")
                if len(record.name) > 12:
                    raise ValidationError("El nombre no puede tener más de 12 caracteres")
    
    @api.constrains('cedula')
    def validar_cedula(self):
        for record in self:
            if record.cedula:
                if len(str(record.cedula)) != 10:
                    raise ValidationError("La cédula mal ingresada")
                if not str(record.cedula).isdigit():
                    raise ValidationError("La cédula mal ingresada")
                provincia = int(record.cedula[:2])
                if provincia < 1 or provincia > 24:
                    raise ValidationError('La cédula mal ingresada')
                tercer_digito = int(record.cedula[2])
                if tercer_digito >=6:
                    raise ValidationError('La cédula mal ingresada')

                

    @api.depends('pasajeros', 'tarifa')
    def tarifa_pasajeros(self):
        for record in self:
            if record.tarifa == 'turista':
                record.total_tarifa = record.pasajeros * 12.5
            elif record.tarifa == 'ejecutiva':
                record.total_tarifa = record.pasajeros * 25.0
            elif record.tarifa == 'vip':
                record.total_tarifa = record.pasajeros * 35.5 


    
                
                