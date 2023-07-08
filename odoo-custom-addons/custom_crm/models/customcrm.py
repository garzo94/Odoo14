# -*- coding: utf-8 -*-
from odoo import models, fields, api
import datetime

class custom_crm(models.Model):
     _name = 'custom_crm.visit'
     _description = 'Visit'

     name = fields.Char(string="Description")
     customer = fields.Many2one(string="Cliente", comodel_name="res.partner")
     date = fields.Datetime(string="Fecha")
     type = fields.Selection([("P","Presencial"),("W", "Whatsapp"),("T","Telefononico")], string="Tipo")
     done = fields.Boolean(string="Realizado")
     image = fields.Binary(string="Imagen")

     def toggle_state(self):
          self.done = not self.done

          # ORM

     def f_create(self):
          visit = {
               'name': 'ORM test',
               'customer': 1,
               'date': str(datetime.date(2020, 8, 6)),
               'type': 'P',
               'done': False
          }
          print(visit)
          self.env['custom_crm.visit'].create(visit)

     def f_search_update(self):
          visit = self.env['custom_crm.visit'].search([('name', '=', 'ORM test')])
          # search(), id, nombre de la instancia
          print('search()', visit, visit.name)

          #$ Otra forma de hacerlo pasando el id directamente
          visit_b = self.env['custom_crm.visit'].browse([8])
          print('browse()', visit_b, visit_b.name)

          # actualizadon el dato
          visit.write({
               'name': 'ORM test write'
          })

     def f_delete(self):
          visit = self.env['custom_crm.visit'].browse([8])
          visit.unlink()

# AbstactModel
class VisitReport(models.AbstractModel):

    _name='report.custom_crm.report_visit_card'

    @api.model
    def _get_report_values(self, docids, data=None):
        report_obj = self.env['ir.actions.report']
        # Nombre del reporte en la carpeta reports -custom_crm.report_visit_card-
        report = report_obj._get_report_from_name('custom_crm.report_visit_card')
        # docs viene de la iteracion que definimos en  views/purchase_order_inherit.xml
        return {
            'doc_ids': docids,
            'doc_model': self.env['custom_crm.visit'],
            'docs': self.env['custom_crm.visit'].browse(docids)
        }

