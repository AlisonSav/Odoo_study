import logging

from odoo import api, fields, models, _

_logger = logging.getLogger(__name__)


class LibraryAddReader(models.TransientModel):
    _name = 'library.add_reader_wizard'
    _description = 'Add a reader to book'

    book_id = fields.Many2one('library.book', string=_('Book'), readonly=True)
    res_partner_ids = fields.Many2many('res.partner', string=_('Readers'))

    @api.model
    def default_get(self, fields):
        res = super().default_get(fields)
        print(self.env.context)
        if self.env.context.get('active_id'):
            book_id = self.env['library.book'].browse(self.env.context.get('active_id'))
            res['book_id'] = book_id.id
            res['res_partner_ids'] = [(6, 0, book_id.res_partner_readers_ids.ids)]
        return res

    def add_reader(self):
        self.book_id.res_partner_readers_ids = self.res_partner_ids
