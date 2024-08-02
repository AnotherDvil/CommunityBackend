# -*- coding: utf-8 -*-
import secrets
import json
from odoo import http
from odoo.http import request, Response

class CommunityLogin(http.Controller):
    @http.route('/login', type='json', auth='none', methods=['POST'], csrf=False, cors='*')
    def login(self, **kwargs):
        email = kwargs.get('email')
        password = kwargs.get('password')
        # Buscar contacto por correo electrónico y contraseña
        partner = request.env['res.partner'].sudo().search([('email', '=', email), ('work_password', '=', password)], limit=1)
        if partner:
            token = secrets.token_urlsafe(20)
            partner.sudo().write({'token': token})
            response = {
                'status': 'success',
                'partner_id': partner.id,
                'partner_name': partner.name,
                'email': partner.email,
                'token': token
            }
        else:
            response = {
                'status': 'error',
                'message': 'Credenciales invalidas'
            }
        return response

    @http.route('/logout', type='json', auth='none', methods=['POST'], csrf=False, cors='*')
    def logout(self, **kwargs):
        # Asegurémonos de recibir el token correctamente
        token = kwargs.get('token')
        # Buscar empleado por token
        partner = request.env['res.partner'].sudo().search([('token', '=', token)], limit=1)
        if partner:
            # Invalidar el token
            partner.sudo().write({'token': False})
            response = {
                'status': 'success',
                'message': 'Logout successful'
            }
        else:
            response = {
                'status': 'error',
                'message': 'Invalid token'
            }
        return response

    @http.route('/register', type='json', auth='none', methods=['POST'], csrf=False, cors='*')
    def register(self, **kwargs):
        name = kwargs.get('name')
        email = kwargs.get('email')
        password = kwargs.get('password')
        if not name or not email or not password:
            response = {
                'status': 'error',
                'message': 'Missing name, email or password'
            }
            return response
        existing_partner = request.env['res.partner'].sudo().search([('email', '=', email)], limit=1)
        if existing_partner:
            response = {
                'status': 'error',
                'message': 'El correo ya está registrado'
            }
            return response
        partner = request.env['res.partner'].sudo().create({
            'name': name,
            'email': email,
            'password': password,
        })
        response = {
            'status': 'success',
            'id': partner.id,
            'name': partner.name,
            'email': partner.email
        }
        return response