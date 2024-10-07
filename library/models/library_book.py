import logging

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)

CONST_EXP = 'CONST_EXP'


class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    name = fields.Char(string=_('Name'), copy=False)
    active = fields.Boolean(string=_('Active'), default=True)
    description = fields.Text(string=_('Description'))
    release_date = fields.Date(default=fields.Date.today(), string=_('Release Date'))
    release_datetime = fields.Datetime(default=lambda self: fields.Datetime.now(),)
    author_names = fields.Char(string=_('Author Names'))
    company_id = fields.Many2one('res.company', string=_('Company'), required=True,
                                 default=lambda self: self.env.company, readonly=True)
    company_currency_id = fields.Many2one('res.currency', related='company_id.currency_id',
                                          string=_('Currency'), readonly=True, tracking=True)
    monetary_price = fields.Monetary(string=_('Monetary'), currency_field='company_currency_id')
    partner_country_name = fields.Char(related='res_partner_id.country_id.name', string=_('Country'))
    active = fields.Boolean(string=_('Active'), default=True, groups='base.group_system')
    res_partner_id = fields.Many2one('res.partner', string=_('Author'), help=_('Main Author'))
    res_partner_ids = fields.Many2many('res.partner', 'library_book_res_partner_id',
                                       'book_id', 'res_partner_id', string=_('Additional Authors'),
                                       help=_('Additional Authors'))
    html_note = fields.Html(string=_('HTML Note'))
    book_cover_image = fields.Binary(string=_('Book Cover Image'), attacment=False)
    book_image = fields.Image(string=_('Book Image'), max_width=500, max_height=500)
    inventory_state = fields.Selection(string=_('Inventory State'),
                                       selection=[('draft', _('Draft')), ('published', _('Published'))],
                                       default='draft')
    res_partner_readers_ids = fields.Many2many('res.partner', 'library_book_res_partner_reader_rel',
                                               'book_id', 'res_partner_id', string=_('Book Readers'),)

    def _default_all_authors_get(self):
        author_names = ''
        res_partner_ids = self.res_partner_ids + self.res_partner_id
        for partner_id in res_partner_ids:
            author_names += partner_id.name
        return author_names

    @api.model_create_multi
    def create(self, vals_list):
        res = super().create(vals_list)
        # res.update({'name': 'Ololo'})  # добавление метода апдейт
        partner_id = self.env['res.partner'].browse(res.id)
        _logger.info(f'Partner name: {partner_id.name}')
        _logger.info('---------------------------')
        _logger.info(f'Books recordset: {res}')
        return res

    @api.returns('self', lambda value: value.id)
    def copy(self, default=None):
        res = super().copy(default)
        _logger.info('---------------------------')
        _logger.info(f'Copy of: {res}')
        return res

    @api.model
    def default_get(self, vals):
        _logger.info('---------------------------')
        _logger.info(f'Vals of: {vals}')
        res = super().default_get(vals)
        return res

    def write(self, vals):
        res = super().write(vals)
        _logger.info('---------------------------')
        _logger.info(f'Write of: {res}')
        return res

    def unlink(self):
        res = super().unlink()
        _logger.info('--------------------------')
        _logger.info(f'Unlink of: {res}')
        return res

    @api.ondelete(at_uninstall=False)
    def _unlink_except_done(self):
        _logger.info(f'Unlink of: {self.name}')

    @api.constrains('name')
    def _check_name_uniq(self):
        for record in self:
            if self.search([('name', '=', record.name), ('id', '!=', record.id)]):
                raise ValidationError(_('Book name must be unique'))

    @api.onchange('inventory_state')
    def _onchange_inventory_state(self):
        return {
            'warning': {
                'title': _('Warning'),
                'message': _('You have already changed the inventory state'),
            }
        }

    @api.onchange('monetary_price')
    def _onchange_inventory_state(self):
        if self.monetary_price > 0:
            self.inventory_state = 'published'

    def show_recordset_opportunities(self):
        self.ensure_one()
        books = self.search([('active', '=', True)])
        bookss = self.search([]).filtered_domain([('active', '=', True)])
        tolkien_id = self.env.ref('library.demo_author_1')
        print(self.search_read([('res_partner_id', '=', tolkien_id.id)], ['name', 'description', 'author_names']))
        print(self.read_group([], ['monetary_price'], ['res_partner_id'], lazy=False))
        print(books.mapped(lambda r: f'Hello {r.name}'))
        print(books.mapped('name'))
        print(books.mapped('res_partner_id.name'))
