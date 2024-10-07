import logging
from datetime import datetime

from odoo import fields, models, _, api
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)

status_list = [('planned', _('Planned')), ('finished', _('Finished')), ('canceled', _('Canceled')),]


class HrHospitalVisit(models.Model):
    _name = 'hr_hospital.visit'
    _description = 'Hr Hospital Visit'

    visit_datetime = fields.Datetime(string=_('Visit Date'))
    planed_datetime = fields.Datetime(string=_('Planed Date'))
    status = fields.Selection(status_list, string=_('Status'))
    active = fields.Boolean('Active', default=True)
    doctor_id = fields.Many2one('hr_hospital.doctor', string=_('Doctor'))
    patient_id = fields.Many2one('hr_hospital.patient', string=_('Patient'))
    diagnosis_ids = fields.One2many('hr_hospital.diagnosis', 'visit', string=_('Diagnosis'))

    @api.multi
    def write(self, vals):
        if 'active' in vals and not vals['active']:
            for record in self:
                if record.diagnosis_ids:
                    raise UserError(_('You cant archive this visit'))
        for record in self:
            if record.visit_datetime and record.visit_datetime < fields.Datetime.now():
                if any(field in vals for field in ['visit_datetime']):
                    raise UserError(_('You cant change the visit date'))
        return super(HrHospitalVisit, self).write(vals)

    @api.multi
    def unlink(self):
        for record in self:
            if record.diagnosis_ids:
                raise UserError(_('You cant unlink visit with diagnosis'))

    @api.constrains('doctor_id', 'patient_id', 'visit_datetime')
    def _check_duplicate_visit(self):
        for record in self:
            visit_date = fields.Datetime.to_date(record.visit_datetime)
            existing_visits = self.env['hr_hospital.visit'].search([
                ('id', '=', record.id),
                ('doctor_id', '=', record.doctor_id.id),
                ('patient_id', '=', record.patient_id.id),
                ('visit_datetime', '=', visit_date),
            ])
            if existing_visits:
                raise ValidationError(_('Visit already exists'))
