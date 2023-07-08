from odoo import models, fields

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    partner_id = fields.Many2one(domain="[('parent_id', '=', False)]")

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    partner_id = fields.Many2one(domain="[('parent_id', '=', False)]")
