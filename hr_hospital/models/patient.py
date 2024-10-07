import logging
from datetime import date

from odoo import api, fields, models, _

_logger = logging.getLogger(__name__)


class HrHospitalPatient(models.Model):
    _name = 'hr_hospital.patient'
    _description = 'Hr Hospital Patient'
    _inherit = 'hr_hospital.person'

    name = fields.Char(string=_('Name'))
    age = fields.Integer(string=_('Age'), compute='_compute_age')
    gender = fields.Char(string=_('Gender'))
    dob_date = fields.Date(string=_('Date of Birth'))
    passport_data = fields.Char(string=_('Passport data'))
    contact_person = fields.Char(string=_('Contact Person'))
    doctor_id = fields.Many2one('hr_hospital.doctor', string=_('Doctor'))
    disease_ids = fields.Many2many('hr_hospital.disease', string='Disease')
    visit_ids = fields.One2many('hr_hospital.visit', 'patient_id',
                                string=_('Visit'))

    @api.depends('dob_date')
    def _compute_age(self):
        for record in self:
            if record.dob_date:
                today = date.today()
                birth_date = fields.Date.from_string(record.dob_date)
                record.age = today.year - birth_date.year - (
                            (today.month, today.day) < (birth_date.month, birth_date.day))
            else:
                record.age = 0
