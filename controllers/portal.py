from odoo import http
from odoo.http import request
import base64
import logging
# from odoo import fields, http, SUPERUSER_ID, _
from odoo.exceptions import AccessError, MissingError
import binascii
# _logger = logging.getLogger(__name__)




class PortalConsentController(http.Controller):

    @http.route('/my/consent_form/<int:consent_form_id>', type='http', auth='user', website=True)
    def portal_consent_form(self, consent_form_id, **kw):
        consent_form = request.env['consent.form.custom'].sudo().browse(consent_form_id)
        if not consent_form.exists():
            return request.not_found()

        return request.render('consent_management.portal_consent_form_template', {
            'consent_form': consent_form
        })
    

    # download
    @http.route('/my/consent_form/download/<int:consent_form_id>', type='http', auth='public', website=True)
    def download_consent_form(self, consent_form_id, **kw):
        # Get the report reference
        report_action = request.env.ref('consent_management.report_project_style_shoot_action')
        pdf_content = request.env['ir.actions.report'].with_context(force_report_rendering=True)._render_qweb_pdf(
            'consent_management.report_project_style_shoot_action', res_ids=consent_form_id)

        # Set the filename for the PDF
        pdf_filename = "Consent_Form_{}.pdf".format(consent_form_id)

        # Return the PDF as a downloadable response
        return request.make_response(pdf_content, [
            ('Content-Type', 'application/pdf'),
            ('Content-Disposition', 'attachment; filename=%s;' % pdf_filename)
        ])

    @http.route('/my/consent_form/<int:consent_form_id>/signed', type='json', auth="public", website=True)
    def sign_contract(self, consent_form_id, name=None, signature=None):
        contract = request.env['consent.form.custom'].sudo().browse(consent_form_id)
        if contract:
            # Check if the signature is in base64 format
            if isinstance(signature, str) and signature.startswith('data:image'):
                # Remove the header 'data:image/png;base64,' before saving
                signature_base64 = signature.split(",")[1]
                contract.write({
                    'signed_by': name,
                    'signed_on': fields.Datetime.now(),
                    'signature': signature_base64,
                })

            base_url = request.env['ir.config_parameter'].sudo().get_param('web.base.url')
            redirect_url = f'{base_url}/my/consent_form/{consent_form_id}'
            return {
                'force_refresh': True,
                'redirect_url': redirect_url,
            }

