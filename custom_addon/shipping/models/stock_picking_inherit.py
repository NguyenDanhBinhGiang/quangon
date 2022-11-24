from odoo import models, fields


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    shipping_order_id = fields.Many2one('shipping.order', string='Shipping order', ondelete='cascade')
