import logging

from odoo import fields, models, _, api
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class HrHospitalDoctor(models.Model):
    _name = 'hr_hospital.doctor'
    _description = 'Hr Hospital Doctor'
    _inherit = 'hr_hospital.person'

    name = fields.Char(string=_('Name'))
    age = fields.Integer(string=_('Age'))
    specialty_id = fields.Many2one('hr_hospital.doctor_speciality', string=_('Specialisation'))  # Поле спеціальності
    is_intern = fields.Boolean(string=_('Intern'), default=False)
    mentor_id = fields.Many2one('hr_hospital.doctor', string=_('Doctor-mentor'), domain="[('is_intern', '=', False)]")
    patient_ids = fields.One2many('hr_hospital.patient', 'doctor_id')

    @api.onchange('is_intern')
    def _onchange_is_intern(self):
        if self.is_intern:
            self.mentor_id = False

    @api.constrains('is_intern', 'mentor_id')
    def _check_mentor(self):
        for record in self:
            if self.mentor_id and record.mentor_id.is_intern:
                raise ValidationError(_('Doctor-mentor cant be intern'))
