# -*- coding: utf-8 -*-

import random
import string
from odoo import models, fields, api

class services(models.Model):
    _name = 'services'
    _description = 'Modelo desarrollado para los servicios que habrá en la app'
    _inherit = ['mail.thread', 'mail.activity.mixin'] # Heredamos estos módulos para tener una tabla de seguimiento
    
    name = fields.Char('Nombre del negocio')
    owner = fields.Many2one('res.partner', 'Dueño')
    image = fields.Binary('Perfil', tracking=True)
    direction = fields.Char('Dirección', tracking=True)
    number_phone = fields.Char('Teléfono', tracking=True)
    email = fields.Char('Correo electrónico', tracking=True)
    bank_account_id = fields.Many2one('res.partner.bank', 'Método de pago', tracking=True)
    archived = fields.Boolean('¿Se dió de baja?', tracking=True)
    #se debe agregar una forma de generar un código de 6 digitos
    access_code = fields.Char('Código de acceso', tracking=True)

    def generate_access_code(self):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for i in range(6))

    @api.model
    def _cron_scheduled_generate_access_code(self):
        services = self.search([])
        for service in services:
            service.access_code = self.generate_access_code()
    
    #Conexión con otros modelos
    novedades = fields.One2many('news', 'service_id', string="Novedades")
    empleados = fields.Many2many('res.partner', 'service_id_e', string="Empleados")
    rewards = fields.One2many('rewards', 'service_id', string="Recompensas")
    followers = fields.Many2many('res.partner', 'service_id_f', string="Seguidores")
    reviews = fields.One2many('reviews', 'service_id', string='Reseñas')
    proposals = fields.One2many('proposals', 'service_id', string="Propuestas")