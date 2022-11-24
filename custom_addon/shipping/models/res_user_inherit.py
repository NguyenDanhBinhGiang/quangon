from odoo import models, fields


class ResUserInherit(models.Model):
    _inherit = 'res.users'

    is_shipper = fields.Boolean(string="Is shipper", default=False)
