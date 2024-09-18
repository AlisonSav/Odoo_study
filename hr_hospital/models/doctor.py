import logging

from odoo import fields, models, _

_logger = logging.getLogger(__name__)


class HrHospitalDoctor(models.Model):
    _name = 'hr_hospital.doctor'
    _description = 'Hr Hospital Doctor'

    name = fields.Char(string=_('Name'))
    age = fields.Integer(string=_('Age'))
    specialization = fields.Char(string=_('Specialization'))
    patient_ids = fields.One2many('hr_hospital.patient', 'doctor_id')
