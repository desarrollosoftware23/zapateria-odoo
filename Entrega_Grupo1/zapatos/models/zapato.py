from odoo import api, fields, models


class ZapatosZapato(models.Model):
    _name = 'zapatos.zapato'
    _description = 'Zapato'

    name = fields.Char(string='Nombre', required=True)
    codigo = fields.Char(
        string='Código', 
        required=True, 
        copy=False, 
        readonly=True
    )
    talla = fields.Integer(string='Talla')
    precio = fields.Float(string='Precio')
    stock = fields.Integer(string='Stock')
    activo = fields.Boolean(string='Activo', default=True)

    _sql_constraints = [
        ('codigo_unico', 'UNIQUE(codigo)',
         'El código ya existe, debe ser único.'),
    ]

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('codigo') or vals.get('codigo') == 'Nuevo':
                vals['codigo'] = self.env['ir.sequence'].next_by_code(
                    'zapatos.zapato') or 'Nuevo'
        return super().create(vals_list)