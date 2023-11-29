```python
import unittest
from models.product_components import ProductComponents
from models.build_configurations import BuildConfigurations
from models.compatibility_rules import CompatibilityRules

class TestComponentCombinations(unittest.TestCase):

    def setUp(self):
        self.product_components = ProductComponents()
        self.build_configurations = BuildConfigurations()
        self.compatibility_rules = CompatibilityRules()

    def test_compatibility_check(self):
        # Test a combination of components that should be compatible
        cpu = self.product_components.get_component('Intel Core i7')
        motherboard = self.product_components.get_component('ASUS ROG Strix Z390-E')
        self.assertTrue(self.compatibility_rules.check_compatibility(cpu, motherboard))

        # Test a combination of components that should not be compatible
        cpu = self.product_components.get_component('AMD Ryzen 9')
        motherboard = self.product_components.get_component('ASUS ROG Strix Z390-E')
        self.assertFalse(self.compatibility_rules.check_compatibility(cpu, motherboard))

    def test_build_configuration(self):
        # Test a build configuration that should be valid
        components = ['Intel Core i7', 'ASUS ROG Strix Z390-E', 'Corsair Vengeance LPX 16GB', 'NVIDIA GeForce RTX 2080']
        self.assertTrue(self.build_configurations.validate_configuration(components))

        # Test a build configuration that should not be valid
        components = ['AMD Ryzen 9', 'ASUS ROG Strix Z390-E', 'Corsair Vengeance LPX 16GB', 'NVIDIA GeForce RTX 2080']
        self.assertFalse(self.build_configurations.validate_configuration(components))

if __name__ == '__main__':
    unittest.main()
```