# -*- coding: utf-8 -*-

from odoo import models, fields, api

class news(models.Model):
    _name = 'news'
    _description = 'Novedades del negocio'
    
    name = fields.Char('Nombre')
    description = fields.Char('Descripción')
    service_id = fields.Many2one(comodel_name='services', string="Servicio")