from odoo import models, fields, api


class ZapatosDescuento(models.Model):
    _inherit = 'zapatos.zapato'
    
    precio_oferta = fields.Float(
        string="Precio de Oferta",
        compute="_compute_precio_oferta",
        readonly=True,
        store=False
    )
    
    @api.depends('precio', 'stock')
    def _compute_precio_oferta(self):
        """Calcula el precio de oferta con 15% de descuento si stock > 30"""
        for record in self:
            if record.stock > 30:
                record.precio_oferta = record.precio * 0.85
            else:
                record.precio_oferta = record.precio
