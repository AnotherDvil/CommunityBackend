# -*- coding: utf-8 -*-

from odoo import models, fields, api

class services(models.Model):
    _name = 'services'
    _description = 'Modelo desarrollado para los servicios que habrá en la app'
    
    name = fields.Char('Nombre del negocio')
    owner = fields.Char('Dueño')
    image = fields.Binary('Perfil')
    direction = fields.Char('Dirección')
    number_phone = fields.Char('Teléfono')
    email = fields.Char('Correo electrónico')
    novedades = fields.One2many(comodel_name='news', inverse_name='service_id', string="Novedades")