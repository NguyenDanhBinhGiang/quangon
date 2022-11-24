from odoo import models, fields


class ShippingOrder(models.Model):
    _name = 'shipping.order'

    shipper_id = fields.Many2one('res.users', string="Shipper", required=True,
                                 domain=[('is_shipper', '=', True)])
    delivery_order_id = fields.One2many('stock.picking', 'shipping_order_id',
                                        string="Delivery orders", ondelete='restrict', required=True)
    name = fields.Char(string='Name', compute='_compute_name')

    def _compute_name(self):
        for rec in self:
            rec.name = f"DS{rec.id}/{rec.delivery_order_id.name}"

    # TODO: declined state, merge accepted and shipping
    state = fields.Selection([
        ('draft', 'Pending'),
        ('accepted', 'Driver accepted'),
        ('shipping', 'Shipping'),
        ('done', 'Done')],
        string='Status', readonly=True, index=True, default='draft', compute='_compute_state', store=True)
