import logging

from odoo import fields, models, _

_logger = logging.getLogger(__name__)


class HrHospitalDisease(models.Model):
    _name = 'hr_hospital.disease'
    _description = 'Hr Hospital Disease'

    name = fields.Char(string=_('Name'))
    patient_ids = fields.Many2many('hr_hospital.patient', string=_('Patients'))
