import logging

from odoo import fields, models, _

_logger = logging.getLogger(__name__)


class HrHospitalDoctorSpeciality(models.Model):
    _name = 'hr_hospital.doctor_speciality'
    _description = 'Hr Hospital Doctor Speciality'

    doctor_ids = fields.One2many('hr_hospital.doctor', 'doctor_id')