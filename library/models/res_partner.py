import logging

from odoo import api, fields, models, _

_logger = logging.getLogger(__name__)


class LibraryBook(models.Model):
    _inherit = 'res.partner'

    name = fields.Char(required=True)
    is_book_author = fields.Boolean(default=True)
    library_book_ids = fields.Many2many('library.book', string=_('Books'))
    books_count = fields.Integer(string=_('Books'), compute='_compute_library_books_count', store=True)

    _sql_constraints = [
        ('name_uniq', 'unique(name)', _('Name must be unique'))
    ]

    @api.depends('library_book_ids')
    def _compute_library_books_count(self):
        for partner in self:
            partner.books_count = len(partner.library_book_ids)

    @api.depends('name', 'library_book_ids')
    def _compute_display_name(self):
        for obj in self:
            book_names = ','.join([f"'{book.name}'" for book in obj.library_book_ids])
            display_name = (obj.name or '') + ' ' + (book_names or '')
            obj.display_name = display_name
