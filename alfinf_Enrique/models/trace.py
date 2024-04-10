from odoo import fields, models

class AlfinfTrace(models.Model):
    _name = 'alfinf.trace'
    _description = 'Controlar las trazas'

    respartner_id = fields.One2many(
        string = 'Agricultor',
        comodel_name = 'res.partner',
        inverse_name = 'traces_ids'
    )
    idvr = fields.Integer()
    tz_planta = fields.Char(
        string = 'Planta'
    )
    tz_hectareas = fields.Integer(
        string = 'Hectáreas'
    )
    tz_columna = fields.Integer(
        string = 'Columna'
    )
    tz_fila = fields.Integer(
        string = 'Fila'
    )
    tz_parcela = fields.Char(
        string = 'Parcela'
    )
    idgfi = fields.Integer()