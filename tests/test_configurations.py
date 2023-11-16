```python
import unittest
from models.build_configurations import BuildConfigurations

class TestConfigurations(unittest.TestCase):

    def setUp(self):
        self.config = BuildConfigurations()

    def test_initial_configuration_empty(self):
        self.assertEqual(self.config.get_configuration(), {})

    def test_add_component(self):
        self.config.add_component('CPU', 'Intel i7')
        self.assertEqual(self.config.get_configuration(), {'CPU': 'Intel i7'})

    def test_remove_component(self):
        self.config.add_component('CPU', 'Intel i7')
        self.config.remove_component('CPU')
        self.assertEqual(self.config.get_configuration(), {})

    def test_update_component(self):
        self.config.add_component('CPU', 'Intel i7')
        self.config.update_component('CPU', 'AMD Ryzen 7')
        self.assertEqual(self.config.get_configuration(), {'CPU': 'AMD Ryzen 7'})

    def test_configuration_total_cost(self):
        self.config.add_component('CPU', 'Intel i7', 300)
        self.config.add_component('GPU', 'Nvidia RTX 3080', 700)
        self.assertEqual(self.config.get_total_cost(), 1000)

    def test_configuration_exceeds_budget(self):
        self.config.set_budget(500)
        self.config.add_component('CPU', 'Intel i7', 300)
        self.config.add_component('GPU', 'Nvidia RTX 3080', 700)
        self.assertTrue(self.config.exceeds_budget())

    def test_configuration_within_budget(self):
        self.config.set_budget(1500)
        self.config.add_component('CPU', 'Intel i7', 300)
        self.config.add_component('GPU', 'Nvidia RTX 3080', 700)
        self.assertFalse(self.config.exceeds_budget())

if __name__ == '__main__':
    unittest.main()
```