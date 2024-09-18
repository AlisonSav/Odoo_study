import logging

from odoo import fields, models, _

_logger = logging.getLogger(__name__)

CONST_EXP = 'CONST_EXP'


class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    name = fields.Char(string=_('Name'))
    active = fields.Boolean(string=_('Active'), default=True)
    description = fields.Text(string=_('Description'))
    res_partner_id = fields.Many2one('res.partner', string=_('Author'))
    res_partner_ids = fields.Many2many('res.partner',
                                       string=_('Additional Authors'))
