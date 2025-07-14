{
    'name': 'Consent Management',
    'version': '1.0.0',
    'sequence': -101,
    'author': 'Hari Raja Prabhu',
    'website': 'www.hari.com',
    'category': 'Consent',
    'summary': 'consent management System',
    'description': 'Consent Management System',
    'depends': ['mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/consent_view.xml',
        'views/consent_template.xml',
        'views/portal/portal_templates.xml',
        'views/consent_template.xml',
        'views/template.xml',
        'views/report.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'consent_management/static/src/css/consent_form_template.css',
        ],
    },
    'controllers': [
        'controllers/portal.py',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',
}
