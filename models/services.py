# -*- coding: utf-8 -*-

from odoo import models, fields, api

class hr_employee(models.Model):
    _inherit = 'hr.employee'
    
    service_id_e = fields.Many2one('services', string='Servicio')
    service_id_f = fields.Many2one('services', string="Servicio")

class services(models.Model):
    _name = 'services'
    _description = 'Modelo desarrollado para los servicios que habrá en la app'
    _inherit = ['mail.thread', 'mail.activity.mixin'] # Heredamos estos módulos para tener una tabla de seguimiento
    
    name = fields.Char('Nombre del negocio')
    owner = fields.Many2one('hr.employee', 'Dueño')
    image = fields.Binary('Perfil', tracking=True)
    direction = fields.Char('Dirección', tracking=True)
    number_phone = fields.Char('Teléfono', tracking=True)
    email = fields.Char('Correo electrónico', tracking=True)
    bank_account_id = fields.Many2one('res.partner.bank', 'Método de pago', tracking=True)
    archived = fields.Boolean('¿Se dió de baja?', tracking=True)
    #se debe agregar una forma de generar un código de 6 digitos
    
    #Conexión con otros modelos
    novedades = fields.One2many('news', 'service_id', string="Novedades")
    empleados = fields.Many2many('hr.employee', 'service_id_e', string="Empleados")
    rewards = fields.One2many('rewards', 'service_id', string="Recompensas")
    followers = fields.Many2many('hr.employee', 'service_id_f', string="Seguidores")
    reviews = fields.One2many('reviews', 'service_id', string='Reseñas')