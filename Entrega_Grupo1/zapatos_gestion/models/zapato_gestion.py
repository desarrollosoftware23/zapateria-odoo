from odoo import models, fields, api

class ZapatosZapato(models.Model):
    _inherit = 'zapatos.zapato' 

    # IMPORTANTE: Creas el campo en tu propio módulo para ser independiente
    stock_minimo = fields.Integer(string='Stock Mínimo', default=10)

    genero = fields.Selection([
        ('hombre', 'Hombre'),
        ('mujer', 'Mujer'),
        ('unisex', 'Unisex'),
        ('nino', 'Niño/a')
    ], string='Género Target', default='unisex')

    tipo_cierre = fields.Selection([
        ('cordones', 'Cordones / Agujetas'),
        ('velcro', 'Velcro'),
        ('cremallera', 'Cremallera'),
        ('ninguno', 'Mocasín / Abierto')
    ], string='Tipo de Cierre', default='cordones')

    temporada = fields.Selection([
        ('primavera_verano', 'Primavera / Verano'),
        ('otono_invierno', 'Otoño / Invierno'),
        ('escolar', 'Temporada Escolar'),
        ('permanente', 'Básico / Todo el año')
    ], string='Temporada / Colección', default='permanente')

    necesita_reposicion = fields.Boolean(
        string='Necesita Reposición',
        compute='_compute_necesita_reposicion',
        store=True
    )

    valor_inventario = fields.Float(
        string='Valor Inventario',
        compute='_compute_valor_inventario',
        store=True
    )

    @api.depends('precio', 'stock')
    def _compute_valor_inventario(self):
        for record in self:
            record.valor_inventario = record.precio * record.stock 

    @api.depends('stock', 'stock_minimo')
    def _compute_necesita_reposicion(self):
        for record in self:
            record.necesita_reposicion = record.stock <= record.stock_minimo