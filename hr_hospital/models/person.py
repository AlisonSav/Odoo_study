import logging

from odoo import fields, models, _

_logger = logging.getLogger(__name__)


class HrHospitalPerson(models.AbstractModel):
    _name = 'hr_hospital.person'
    _description = 'Abstract Person'
    _abstract = True

    name = fields.Char(string=_('Name'))
    phone = fields.Char(string=_('Phone'))
    photo = fields.Image(string=_('Photo'), max_width=500, max_height=500)
    gender = fields.Selection([('male', 'male'), ('female', 'female')], string=_('Gender'))
