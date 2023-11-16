# Developer Guide

## Overview

This guide provides an overview of the Custom PC Building module, its architecture, key components, and instructions for adding new components, configuring recommendations, and testing.

## Module Architecture

The module is structured around three main models:

- `product_components.py`: Defines the data structure for the components.
- `build_configurations.py`: Tracks user configurations.
- `compatibility_rules.py`: Defines compatibility rules between components.

## Key Components

The key components of the module are:

- `custom_pc_configuration_wizard.py`: Handles the step-by-step configuration process.
- `sales_order.py` and `invoice.py`: Handle the sales order and invoice generation for a configuration.
- `custom_pc_production_process.py`: Manages the assembly and installation services.

## Compatibility Rules

Compatibility rules are defined in the `compatibility_rules.py` model. These rules prevent incompatible component selections during the configuration process.

## Adding New Components

To add new components, extend the `product_components.py` model with the details of the new component. Then, update the `product_views.xml` file to include the new component in the component selection view.

## Configuring Recommendations

Recommendations are configured in the `custom_pc_configuration_wizard.py` file. The recommendation logic is based on the customer's use case (gaming, content creation, etc.).

## Testing

Testing is done using Python's unittest module. Test cases are defined in the `test_component_combinations.py`, `test_budgets.py`, and `test_configurations.py` files. Browser testing is done using Selenium and load testing is done using Locust.

## Versioning and Migration Strategy

Follow Odoo's standard versioning and migration guidelines. Ensure to test all migrations in a staging environment before deploying to production.

## Notes

- Follow Odoo development guidelines and structure.
- Ensure full test coverage.
- Set up a staging environment for testing.
- Plan deployment to avoid inventory issues.
- Internationalize text strings.

## Technical Specifications

- Odoo version: 16 Community Edition
- Compatible devices: PC, tablet, mobile
- Dependencies: eCommerce module, Inventory management, Website builder

For more detailed instructions, refer to the `installation_guide.md` file.