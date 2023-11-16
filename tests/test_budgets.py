```python
import unittest
from models.build_configurations import BuildConfiguration

class TestBudgets(unittest.TestCase):

    def setUp(self):
        self.config = BuildConfiguration()

    def test_initial_budget_zero(self):
        self.assertEqual(self.config.total_cost, 0)

    def test_add_component_updates_budget(self):
        self.config.add_component('CPU', 'Intel i7', 300)
        self.assertEqual(self.config.total_cost, 300)

    def test_remove_component_updates_budget(self):
        self.config.add_component('CPU', 'Intel i7', 300)
        self.config.remove_component('CPU')
        self.assertEqual(self.config.total_cost, 0)

    def test_budget_warning(self):
        self.config.set_budget(500)
        self.config.add_component('CPU', 'Intel i7', 300)
        self.config.add_component('GPU', 'Nvidia RTX 3080', 700)
        self.assertTrue(self.config.budget_exceeded)

if __name__ == '__main__':
    unittest.main()
```