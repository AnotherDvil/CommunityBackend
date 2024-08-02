# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Contacts(models.Model):
    _inherit = 'res.partner'

    password = fields.Char(string='Contraseña')
    token = fields.Char(string='Token de seguridad')
    
    service_id_e = fields.Many2one('services', string='Servicio')
    service_id_f = fields.Many2one('services', string="Servicio")