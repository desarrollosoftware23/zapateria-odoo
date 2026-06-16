from odoo import models, fields, api

class ZapatosZapato(models.Model):
    _inherit = 'zapatos.zapato'

    codigo = fields.Char(string='Codigo')
    marca = fields.Char(string='Marca')
    color = fields.Char(string='Color')
    material = fields.Char(string='Material')
    descripcion = fields.Text(string='Descripcion')
    stock_minimo = fields.Integer(string='Stock Minimo', default=5)
    talla = fields.Selection([
        ('35', '35'),
        ('36', '36'),
        ('37', '37'),
        ('38', '38'),
        ('39', '39'),
        ('40', '40'),
        ('41', '41'),
        ('42', '42'),
        ('43', '43'),
        ('44', '44'),
        ('45', '45'),
    ], string='Talla')
    temporada = fields.Selection([
        ('verano', 'Verano'),
        ('invierno', 'Invierno'),
        ('primavera', 'Primavera'),
        ('otono', 'Otoño'),
    ], string='Temporada')
    valor_inventario = fields.Float(
        string='Valor Inventario',
        compute='_compute_valor_inventario',
        store=True
    )

    @api.depends('precio', 'stock')
    def _compute_valor_inventario(self):
        for record in self:
            record.valor_inventario = record.precio * record.stock