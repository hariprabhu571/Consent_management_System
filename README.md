# Consent Management System

A comprehensive Odoo module for managing digital consent forms with signature capture, PDF generation, and portal access capabilities.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Screenshots](#screenshots)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)
- [Support](#support)

## 🎯 Overview

The Consent Management System is a powerful Odoo module designed to streamline the process of creating, managing, and tracking digital consent forms. It provides a complete solution for organizations that need to collect and manage user consent in a compliant and efficient manner.

### Key Benefits

- **Digital Signature Capture**: Secure electronic signature collection
- **PDF Generation**: Automatic PDF creation with professional formatting
- **Portal Access**: Customer self-service portal for form completion
- **Template Management**: Reusable consent form templates
- **Status Tracking**: Real-time status monitoring of consent forms
- **Compliance Ready**: Built with data protection regulations in mind

## ✨ Features

### Core Functionality

- **Consent Form Creation**: Create and manage consent forms with customizable templates
- **Digital Signatures**: Capture and store electronic signatures securely
- **PDF Reports**: Generate professional PDF reports with company branding
- **Portal Integration**: Customer-facing portal for form completion
- **Status Management**: Track form status (Draft, To Sign, Signed)
- **Template System**: Reusable templates with dynamic content replacement

### Advanced Features

- **Company Branding**: Customizable headers with company logos
- **Dynamic Content**: Template variables for personalized forms
- **Email Integration**: Automated email notifications
- **Activity Tracking**: Full audit trail with chatter functionality
- **Multi-company Support**: Works across multiple companies
- **Responsive Design**: Mobile-friendly portal interface

### Security Features

- **Access Control**: Role-based permissions and access rights
- **Data Encryption**: Secure storage of sensitive information
- **Audit Trail**: Complete logging of all activities
- **CSRF Protection**: Built-in security against cross-site request forgery


## 🔧 Requirements

### System Requirements

- **Python**: 3.8 or later
- **Odoo**: 16.0 or later
- **Database**: PostgreSQL 12 or later
- **Web Server**: nginx/apache (for production)
- **Operating System**: Linux, Windows, or macOS

### Python Dependencies

See [requirements.txt](requirements.txt) for the complete list of Python packages.

## 🚀 Installation

### Quick Start

1. **Install Python Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Install Odoo 16.0+**
   - Download from [Odoo's official website](https://www.odoo.com/page/download)
   - Or use Docker: `docker run -d -p 8069:8069 odoo:16.0`

3. **Install the Module**
   - Copy the module to your Odoo addons directory
   - Update Odoo configuration to include the addons path
   - Restart Odoo service
   - Install the module through Odoo's Apps menu

For detailed installation instructions, see [INSTALLATION.md](INSTALLATION.md).

## 📖 Usage

### Creating a Consent Form

1. **Navigate to Consent Management**
   - Go to **Consent > Consent Form** in the main menu

2. **Create New Form**
   - Click **Create** button
   - Fill in the required fields:
     - Subject
     - Partner (customer)
     - User (responsible person)
     - Template
     - Date

3. **Configure Form Settings**
   - Select a consent template
   - Enable/disable print header
   - Add additional information if needed

4. **Generate Portal Link**
   - Click **Customer Preview** button
   - Share the generated URL with the customer

### Managing Templates

1. **Create Template**
   - Go to **Consent > Templates**
   - Create new template with HTML content
   - Use variables like `${object.users_id.name}` for dynamic content

2. **Template Variables**
   - `${object.users_id.name}` - User name
   - `${object.date}` - Form date
   - `${object.partner_id.name}` - Partner name

### Portal Access

1. **Customer Portal**
   - Customers access forms via portal URL
   - View consent form content
   - Sign electronically
   - Download PDF copy

2. **Form Status Tracking**
   - **Draft**: Initial state
   - **To Sign**: Ready for customer signature
   - **Signed**: Completed with signature

## 🔌 API Documentation

### REST API Endpoints

#### Get Consent Form
```http
GET /my/consent_form/{consent_form_id}
```
Returns the consent form for portal display.

#### Download PDF
```http
GET /my/consent_form/download/{consent_form_id}
```
Downloads the consent form as a PDF file.

#### Sign Form
```http
POST /my/consent_form/{consent_form_id}/signed
```
Signs the consent form with customer signature.

**Parameters:**
- `name`: Customer name
- `signature`: Base64 encoded signature image

### Response Format
```json
{
    "force_refresh": true,
    "redirect_url": "https://example.com/my/consent_form/123"
}
```

## 🛠️ Development

### Project Structure

```
consent_management/
├── __init__.py
├── __manifest__.py
├── controllers/
│   ├── __init__.py
│   └── portal.py
├── models/
│   ├── __init__.py
│   ├── consent.py
│   └── consent_template.py
├── security/
│   └── ir.model.access.csv
├── static/
│   └── src/
│       └── css/
│           └── consent_form_template.css
├── views/
│   ├── consent_view.xml
│   ├── consent_template.xml
│   ├── menu.xml
│   ├── portal/
│   │   └── portal_templates.xml
│   ├── report_consent_form.xml
│   ├── report.xml
│   └── template.xml
├── requirements.txt
├── INSTALLATION.md
└── README.md
```

### Development Setup

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd consent-management-system
   ```

2. **Install Development Dependencies**
   ```bash
   pip install -r requirements.txt
   pip install pytest pytest-odoo black flake8
   ```

3. **Run Tests**
   ```bash
   pytest
   ```

4. **Code Formatting**
   ```bash
   black .
   flake8 .
   ```

### Adding New Features

1. **Create Model**
   - Add new model in `models/` directory
   - Update `models/__init__.py`

2. **Create Views**
   - Add XML views in `views/` directory
   - Update menu structure

3. **Add Controllers**
   - Create new controllers in `controllers/` directory
   - Define API endpoints

4. **Update Security**
   - Modify `security/ir.model.access.csv` for new models

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork the Repository**
   - Create a fork of this repository

2. **Create Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make Changes**
   - Implement your feature
   - Add tests for new functionality
   - Update documentation

4. **Submit Pull Request**
   - Create a pull request with detailed description
   - Include screenshots if UI changes

### Contribution Guidelines

- Follow PEP 8 coding standards
- Write comprehensive tests
- Update documentation for new features
- Ensure backward compatibility
- Add proper error handling


## 🆘 Support

### Getting Help

- **Documentation**: Check this README and [INSTALLATION.md](INSTALLATION.md)
- **Issues**: Report bugs and feature requests through GitHub Issues
- **Community**: Join our community discussions
- **Email**: Contact support at support@example.com

### Troubleshooting

Common issues and solutions:

1. **Module Not Found**
   - Verify addons path in Odoo configuration
   - Check file permissions
   - Restart Odoo service

2. **Import Errors**
   - Install all Python dependencies
   - Check Python version compatibility
   - Verify virtual environment

3. **Portal Access Issues**
   - Check portal user permissions
   - Verify portal configuration
   - Ensure proper URL routing

### Logs and Debugging

- **Odoo Logs**: `/var/log/odoo/odoo.log`
- **System Logs**: `journalctl -u odoo`
- **Debug Mode**: Enable debug mode in Odoo for detailed logs

## 📊 Version History

### v1.0.0 (Current)
- Initial release
- Basic consent form management
- Portal integration
- PDF generation
- Digital signature capture

### Planned Features
- Advanced template system
- Multi-language support
- Integration with external systems
- Enhanced reporting capabilities

## 🙏 Acknowledgments

- **Odoo Community**: For the excellent framework
- **Contributors**: All those who contributed to this project
- **Users**: For valuable feedback and suggestions

---
