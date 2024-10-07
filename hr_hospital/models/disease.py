import logging

from odoo import fields, models, _

_logger = logging.getLogger(__name__)


class HrHospitalDisease(models.Model):
    _name = 'hr_hospital.disease'
    _description = 'Hr Hospital Disease'
    _parent_name = 'parent_id'
    _parent_store = True
    _parent_order = 'name'

    name = fields.Char(string=_('Name'))
    patient_ids = fields.Many2many('hr_hospital.patient', string=_('Patients'))
    parent_id = fields.Many2one('hr_hospital.disease', string=_('Parent disease'), index=True, ondelete='cascade')
    child_ids = fields.One2many('hr_hospital.disease', 'parent_id', string=_('Children disease'))
