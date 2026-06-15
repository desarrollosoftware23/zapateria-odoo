
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ZapatoCategoria(models.Model):
    _name = 'zapato.categoria'
    _description = 'Categoría de Zapatos'

    name = fields.Char(string='Nombre de Categoría', required=True) # deporte, casual, formal
    description = fields.Text(string='Descripción')


class ZapatoBase(models.Model):
    _name = 'zapato.base'
    _description = 'Modelo Base de Zapato'

    nombre = fields.Char(string='Nombre', required=True)
    marca = fields.Char(string='Marca', required=True)
    talla = fields.Integer(string='Talla', required=True)
    precio = fields.Float(string='Precio', required=True)
    color = fields.Char(string='Color')
    stock = fields.Integer(string='Stock', default=0)

    categoria_id = fields.Many2one('zapato.categoria', string='Categoría')
    
    @api.constrains('precio', 'stock', 'talla')
    def _check_valores_positivos(self):
        for record in self:
            if record.precio <= 0:
                raise ValidationError("El precio del zapato debe ser mayor que cero")
            if record.stock < 0:
                raise ValidationError("El stock de zapatos no puede ser negativo")
            if record.talla <= 0:
                raise ValidationError("La talla debe ser un número válido mayor a cero")