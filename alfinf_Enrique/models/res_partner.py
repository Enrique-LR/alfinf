from odoo import fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_trace = fields.Boolean(
        string = 'nombre_campo'
    )

    traces_ids = fields.Many2one(
        string = 'Trazas',
        comodel_name = 'alfinf.trace',
        inverse_name = 'respartner_id'
    )