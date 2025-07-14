# Consent Management System - Installation Instructions

## Prerequisites

### System Requirements
- **Python**: 3.8 or later
- **Odoo**: 16.0 or later
- **Database**: PostgreSQL 12 or later
- **Web Server**: nginx/apache (for production deployment)
- **Operating System**: Linux, Windows, or macOS

### Software Dependencies
- Odoo 16.0+ framework
- PostgreSQL database server
- Web server (for production)

## Installation Steps

### 1. Install Odoo 16.0+

#### Option A: Using Odoo's Official Installer
1. Download Odoo 16.0 from [Odoo's official website](https://www.odoo.com/page/download)
2. Follow the installation guide for your operating system
3. Ensure Odoo is running and accessible

#### Option B: Using Docker
```bash
docker run -d -p 8069:8069 --name odoo16 -v odoo-web-data:/var/lib/odoo -v odoo-addons:/mnt/extra-addons odoo:16.0
```

### 2. Install Python Dependencies

Navigate to your project directory and install the required Python packages:

```bash
# Install all dependencies
pip install -r requirements.txt

# Or install individually
pip install reportlab>=3.6.0
pip install Pillow>=9.0.0
pip install cryptography>=3.4.0
pip install ratelimit>=2.2.0
pip install structlog>=21.0.0
pip install requests>=2.25.0
pip install jsonschema>=3.2.0
pip install python-dateutil>=2.8.0
```

### 3. Install the Consent Management Module

1. **Copy the module to Odoo addons directory:**
   ```bash
   # Find your Odoo addons directory
   # Usually located at: /usr/lib/python3/dist-packages/odoo/addons/
   # Or: /opt/odoo/addons/
   
   # Copy the consent_management module
   cp -r "Consent Management System" /path/to/odoo/addons/consent_management
   ```

2. **Update Odoo configuration:**
   - Edit your Odoo configuration file (usually `/etc/odoo/odoo.conf`)
   - Add the addons path to the `addons_path` parameter:
   ```
   addons_path = /usr/lib/python3/dist-packages/odoo/addons,/path/to/odoo/addons
   ```

3. **Restart Odoo service:**
   ```bash
   sudo systemctl restart odoo
   # Or if using Docker:
   docker restart odoo16
   ```

### 4. Install the Module in Odoo

1. **Access Odoo:**
   - Open your web browser
   - Navigate to `http://localhost:8069` (or your Odoo URL)

2. **Install the module:**
   - Go to **Apps** menu
   - Remove the "Apps" filter to see all modules
   - Search for "Consent Management"
   - Click **Install** button

3. **Verify installation:**
   - Check that the "Consent" menu appears in the main menu
   - Verify that you can create and manage consent forms

### 5. Configure the Module

#### Basic Configuration
1. Go to **Consent > Consent Form** in the main menu
2. Create your first consent form template
3. Configure company information and settings

#### Advanced Configuration
1. **Portal Access:**
   - Ensure portal users can access consent forms
   - Configure portal permissions in **Settings > Users & Companies > Users**

2. **Email Templates:**
   - Customize email notifications in **Settings > Technical > Email > Templates**

3. **Report Templates:**
   - Customize PDF reports in **Settings > Technical > Reporting > Reports**

## Development Setup

### Install Development Dependencies
```bash
# Install development tools
pip install pytest>=6.0.0
pip install pytest-odoo>=1.0.0
pip install black>=21.0.0
pip install flake8>=3.8.0
```

### Running Tests
```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_consent.py

# Run with coverage
pytest --cov=consent_management
```

### Code Formatting
```bash
# Format code with black
black .

# Check code style with flake8
flake8 .
```

## Troubleshooting

### Common Issues

1. **Module not found:**
   - Verify the addons path is correct in Odoo configuration
   - Check file permissions on the module directory
   - Restart Odoo service

2. **Import errors:**
   - Ensure all Python dependencies are installed
   - Check Python version compatibility
   - Verify virtual environment (if using one)

3. **Database errors:**
   - Check PostgreSQL connection
   - Verify database user permissions
   - Check Odoo log files for detailed error messages

4. **Portal access issues:**
   - Verify portal user permissions
   - Check portal configuration in Odoo settings
   - Ensure proper URL routing

### Log Files
- **Odoo logs:** Usually in `/var/log/odoo/odoo.log`
- **System logs:** Check with `journalctl -u odoo`

### Getting Help
- Check Odoo documentation: https://www.odoo.com/documentation/16.0/
- Review module-specific logs in Odoo interface
- Contact system administrator for server-level issues

## Production Deployment

### Security Considerations
1. **HTTPS:** Always use HTTPS in production
2. **Firewall:** Configure firewall rules appropriately
3. **Database:** Use strong passwords and limit access
4. **Backups:** Implement regular backup procedures

### Performance Optimization
1. **Caching:** Enable Odoo caching mechanisms
2. **Database:** Optimize PostgreSQL settings
3. **Web Server:** Configure nginx/apache for optimal performance
4. **Monitoring:** Set up monitoring and alerting

### Backup Procedures
```bash
# Database backup
pg_dump odoo_db > backup_$(date +%Y%m%d).sql

# Module backup
tar -czf consent_management_backup_$(date +%Y%m%d).tar.gz consent_management/
```

## Support

For technical support or questions:
- Check the troubleshooting section above
- Review Odoo documentation
- Contact your system administrator
- Submit issues through your organization's support channels 