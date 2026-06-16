from odoo import models, fields, api

class ZapatosZapato(models.Model):
    _inherit = 'zapatos.zapato'

    codigo = fields.Char(string='codigo')
    marca = fields.Char(string='marca')
    color = fields.Char(string='color')
    material = fields.Char(string='material')
    descripcion = fields.Text(string='descripcion')
    stock_minimo = fields.Integer(string='stock_minimo', default=5)
    descuento= fields.Boolean(string = 'descuento', default = False)
    valor_inventario = fields.Float(
        string='valor_inventario', 
        compute='_compute_valor_inventario', 
        store = True
    )
    @api.depends('precio', 'stock')
    def _compute_valor_inventario(self):
        for barrido in self:
            barrido.valor_inventario = barrido.precio * barrido.stock
    