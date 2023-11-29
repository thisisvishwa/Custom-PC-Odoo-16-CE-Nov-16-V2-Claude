```python
import unittest
from models import product_components, build_configurations, compatibility_rules
from wizards import custom_pc_configuration_wizard
from sales import sales_order, invoice

class TestCustomPCModule(unittest.TestCase):

    def setUp(self):
        self.product_components = product_components.ProductComponents()
        self.build_configurations = build_configurations.BuildConfigurations()
        self.compatibility_rules = compatibility_rules.CompatibilityRules()
        self.custom_pc_configuration_wizard = custom_pc_configuration_wizard.CustomPCConfigurationWizard()
        self.sales_order = sales_order.SalesOrder()
        self.invoice = invoice.Invoice()

    def test_component_selection(self):
        self.product_components.add_component('CPU', 'Intel i7')
        self.assertEqual(self.product_components.get_component('CPU'), 'Intel i7')

    def test_compatibility_check(self):
        self.compatibility_rules.add_rule('CPU', 'Intel i7', 'Motherboard', 'ASUS Z170')
        self.assertTrue(self.compatibility_rules.check_compatibility('CPU', 'Intel i7', 'Motherboard', 'ASUS Z170'))

    def test_budget_tracking(self):
        self.build_configurations.set_budget(1000)
        self.build_configurations.add_component('CPU', 'Intel i7', 300)
        self.assertEqual(self.build_configurations.get_total_cost(), 300)

    def test_recommendations(self):
        self.custom_pc_configuration_wizard.set_use_case('gaming')
        self.assertEqual(self.custom_pc_configuration_wizard.get_recommendations(), ['CPU: Intel i7', 'GPU: Nvidia GTX 1080'])

    def test_dynamic_pricing(self):
        self.product_components.set_price('CPU', 'Intel i7', 300)
        self.assertEqual(self.product_components.get_price('CPU', 'Intel i7'), 300)

    def test_assembly_options(self):
        self.sales_order.add_assembly_service('Standard Assembly')
        self.assertEqual(self.sales_order.get_assembly_service(), 'Standard Assembly')

    def test_invoice_generation(self):
        self.invoice.add_item('CPU', 'Intel i7', 1, 300)
        self.assertEqual(self.invoice.get_total(), 300)

if __name__ == '__main__':
    unittest.main()
```