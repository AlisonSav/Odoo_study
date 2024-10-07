import logging

from odoo import fields, models, _, api
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class HrHospitalDiagnosis(models.Model):
    _name = 'hr_hospital.diagnosis'
    _description = 'Hr Hospital Diagnosis'

    visit = fields.Many2one('hr_hospital.visit', string=_('Visit'))
    name = fields.Char(string=_('Diagnosis'))
    description = fields.Text(string=_('Description'))
    doctor_id = fields.Many2one('hr_hospital.doctor', string=_('Doctor'), required=True)
    is_approve_by_mentor = fields.Boolean(string=_('Approved by mentor'), default=False, readonly=True)

    @api.model_create_multi
    def create(self, vals):
        for record in self:
            if record.doctor_id.mentor_id:
                record.is_approve_by_mentor = True
            else:
                record.is_approve_by_mentor = False
        return super(HrHospitalDiagnosis, self).create(vals)

    @api.multi
    def write(self, vals):
        for record in self:
            doctor = record.doctor_id
            if doctor.is_intern and not record.is_approve_by_mentor:
                if 'is_approve_by_mentor' not in vals:
                    raise ValidationError(_('Only mentor can approve diagnosis'))
        return super(HrHospitalDiagnosis, self).write(vals)
