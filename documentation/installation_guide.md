# Custom PC Building Module - Installation Guide

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed Odoo version 16 Community Edition.
- You have a basic understanding of Python and XML.
- You have access to the terminal/command line interface on your system.

## Installation Steps

1. Download the module from the repository and extract it to your Odoo addons directory.

```bash
cd /path/to/your/odoo/addons/directory
wget https://repository-url/custom_pc_building_module.zip
unzip custom_pc_building_module.zip
```

2. Update the Odoo module list.

```bash
/path/to/your/odoo/bin/odoo.py -u base --database=your_database
```

3. Install the module via Odoo Apps interface. Search for 'Custom PC Building Module' and click on 'Install'.

4. After installation, refresh your browser to see the changes.

## Configuration

1. Navigate to the 'Custom PC Building' menu in the Odoo interface.

2. Configure your product components under the 'Product Components' menu. Here you can add, edit, or remove components.

3. Set up compatibility rules under the 'Compatibility Rules' menu. This will ensure that customers can only select compatible components.

4. Set up your build configurations under the 'Build Configurations' menu. This will allow customers to save and load their custom configurations.

5. Customize your product views under the 'Product Views' menu. This will determine how your components are displayed to customers.

6. Set up your procurement rules under the 'Procurement Rules' menu. This will determine how components are procured for assembly.

7. Set up your custom PC production process under the 'Production Process' menu. This will manage the assembly and installation services.

## Testing

Refer to the `tests/` directory for testing scripts. Run the tests to ensure the module is working as expected.

```bash
python -m unittest discover -s /path/to/your/odoo/addons/custom_pc_building_module/tests
```

## Troubleshooting

If you encounter any issues during installation or configuration, refer to the `developer_guide.md` for more detailed information about the module's architecture and components.

## Contributing

For contributing guidelines, please see the `translation_contributions.md` file.

## Changelog

For a detailed list of changes for each version, see the `changelog.md` file.

## Support

If you need further assistance, visit our support site as detailed in the `support_site.md` file.