import logging

from odoo import fields, models, _

_logger = logging.getLogger(__name__)


class HrHospitalVisit(models.Model):
    _name = 'hr_hospital.visit'
    _description = 'Hr Hospital Visit'

    visit = fields.Date(string=_('Visit'))
    patient_id = fields.Many2one('hr_hospital.patient')
