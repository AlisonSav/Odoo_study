import logging

from odoo import fields, models, _

_logger = logging.getLogger(__name__)


class HrHospitalPatient(models.Model):
    _name = 'hr_hospital.patient'
    _description = 'Hr Hospital Patient'

    name = fields.Char(string=_('Name'))
    age = fields.Integer(string=_('Age'))
    gender = fields.Char(string=_('Gender'))
    doctor_id = fields.Many2one('hr_hospital.doctor', string=_('Doctor'))
    disease_ids = fields.Many2many('hr_hospital.disease', string='Disease')
    visit_ids = fields.One2many('hr_hospital.visit', 'patient_id',
                                string=_('Visit'))
