import logging

from odoo import fields, models, _

_logger = logging.getLogger(__name__)


class LibraryBook(models.Model):
    _inherit = 'res.partner'

    library_book_ids = fields.Many2many('library.book', string=_('Books'))
