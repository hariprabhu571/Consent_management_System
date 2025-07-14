from odoo import models, fields, api


class ConsentFormTemplate(models.Model):
    _name = 'consent.form.template'
    _description = 'Consent Form Template'

    name = fields.Char(string='Template Name', required=True)
    template_content = fields.Html(string='Consent Form Content', sanitize=False)
    active = fields.Boolean(string='Active', default=True)

    @api.model
    def default_get(self, fields):
        res = super(ConsentFormTemplate, self).default_get(fields)
        if not res.get('template_content'):
            res['template_content'] = '''
                <h1 style="text-align: center;">CONSENT FORM</h1>
                <br>
                <p style="text-align: center;">I hereby authorize the procedure. Upon me under the supervision of <b>${object.users_id.name | safe}</b>. 
                A description of the procedure and the side effects that may occur as a result of this procedure 
                have been explained to me. I understand that no guarantee or insurance has been given to me regarding 
                the outcome of the procedure. I also consent to any further alternative operative measures found to be 
                necessary during the procedure. I consent to any medical photographs that may be found necessary to be 
                kept in my private folder. I consent to the authorized persons of the Medical Center to deal with the 
                tissues or parts which may be removed from my body according to Medical Ethics.
                                            Thanks & Regards
                                            ${object.users_id.name | safe}
                                            ${object.date | safe}
                </p>
            '''
        return res
