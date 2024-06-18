# -*- coding: utf-8 -*-

from odoo import models, fields, api

class reviews(models.Model):
    _name = 'reviews'
    _description = 'Modelo desarrollado para las reseñas que tendrá cáda negocio'
    
    name = fields.Char("Titulo")
    description = fields.Char("Descripción")
    rating = fields.Float('Calificación', store=True)
    
    service_id = fields.Many2one('services', 'Servicios')