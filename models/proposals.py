# -*- coding: utf-8 -*-

from odoo import models, fields, api

class proposals(models.Model):
    _name = 'proposals'
    _description = 'Propuestas'
    
    name = fields.Char('Nombre propuesta')
    description = fields.Char('Detalles')
    written_by = fields.Many2one('hr.employee', string="Creado por", readonly=True)
    status = fields.Selection(
        [
            ('draft', 'Borrador'), 
            ('complete', 'Completo'), 
            ('process', 'En proceso'), 
            ('cerrado', 'Cerrado')
        ], default='draft', string="Estado")
    close_date = fields.Datetime('Fecha de cierre')
    service_id = fields.Many2one('services', 'Servicios')
    
    
    #Metodos para cambiar el estado del registro
    def complete_status(self):
        self.status = 'complete'
    def draft_status(self):
        self.status = 'draft'
        
    #Al momento de crear un registro se llenará el campo written_by con el nombre del usuario actual
    @api.model
    def create(self, vals):
        # Obtener el usuario actual
        user = self.env.user
        # Obtener el empleado correspondiente al usuario actual
        employee = self.env['hr.employee'].search([('user_id', '=', user.id)], limit=1)
        # Establecer el campo written_by con el empleado correspondiente
        vals['written_by'] = employee.id if employee else False
        return super(proposals, self).create(vals)