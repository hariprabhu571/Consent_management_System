from odoo import api, models, fields
from odoo.http import request
import random


class ConsentFormCustom(models.Model):
    _name = 'consent.form.custom'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Consent Form Custom'
    _rec_name ='ref'

    #status
    status = fields.Selection([
        ('draft', 'DRAFT'),
        ('to_sign', 'TO SIGN'),
        ('signed', 'SIGNED')
    ], string='Status', default='draft', tracking=True)

    # Basic Information
    ref = fields.Char(string='Reference', readonly=True, copy=False, default=lambda self: self._generate_random_id())

    name = fields.Char(string='Subject', tracking=True)
    partner_id = fields.Many2one('res.partner', string='Partner', required=True,domain=[('is_company', '=', False)])
    users_id = fields.Many2one('res.users', string='User')
    tag_ids = fields.Many2many('res.partner.category', string='Tags')
    # company_id = fields.Many2one('res.company', string='Company')
    company_id = fields.Many2one(
        'res.company',
        string='Company',
        default=lambda self: self.env.company.id,
        readonly=True
    )

    date = fields.Date(string='Date', default=fields.Date.today)
    template_id = fields.Many2one('consent.form.template', string='Template')
    consent_given = fields.Boolean(string='Print Header')

    #document
    consent_content = fields.Html(
        compute='_compute_consent_content',
        readonly=True
    )

    #additional info
    additional_info = fields.Text(string='Additional Information')
    signature = fields.Image('Signature', help='Contract Signature received through the portal.', copy=False,
                             attachment=True, max_width=1024, max_height=1024)
    signed_by = fields.Char('Signed By', help='Name of the person that signed the Contract.', copy=False, tracking=True)
    signed_on = fields.Datetime('Signed On', help='Date of the signature.', copy=False, tracking=True)




    @api.depends('template_id', 'users_id')
    def _compute_consent_content(self):
        for record in self:
            if record.template_id and record.template_id.template_content:
                content = record.template_id.template_content
                if record.users_id:
                    content = content.replace('${object.users_id.name | safe}', record.users_id.name)
                if record.date:
                    content = content.replace('${object.date | safe}', record.date.strftime('%Y-%m-%d'))
                record.consent_content = content
            else:
                record.consent_content = False
    # Status
    active = fields.Boolean(string='Active', default=True)



    @api.model
    def create(self, vals):
        vals['ref'] = vals.get('ref') or self._generate_random_id()
        return super(ConsentFormCustom, self).create(vals)

    def _generate_random_id(self):
        """Generate a random ID in the format CF####"""
        prefix = 'CF'
        number = random.randint(1, 9999)
        return f"{prefix}{number:04d}"

    def action_to_sign(self):
        for rec in self:
            rec.status = 'to_sign'

    def action_signed(self):
        for rec in self:
            rec.status = 'signed'



    def action_customer_preview(self):
        """Generate the portal URL and redirect to the customer preview page."""
        self.ensure_one()
        base_url = request.env['ir.config_parameter'].sudo().get_param('web.base.url')
        portal_url = f"{base_url}/my/consent_form/{self.id}"
        return {
            'type': 'ir.actions.act_url',
            'url': portal_url,
            'target': 'new',  # Opens in a new tab.
        }