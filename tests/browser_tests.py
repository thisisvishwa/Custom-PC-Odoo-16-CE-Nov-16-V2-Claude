```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class CustomPCBuilderBrowserTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_title(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Custom PC Builder', self.browser.title)

    def test_component_selection(self):
        self.browser.get('http://localhost:8000')
        cpu = self.browser.find_element_by_name('cpu')
        cpu.send_keys('Intel i7')
        cpu.send_keys(Keys.RETURN)
        self.assertIn('Intel i7', self.browser.page_source)

    def test_compatibility_check(self):
        self.browser.get('http://localhost:8000')
        cpu = self.browser.find_element_by_name('cpu')
        cpu.send_keys('Intel i7')
        cpu.send_keys(Keys.RETURN)
        motherboard = self.browser.find_element_by_name('motherboard')
        motherboard.send_keys('AMD Motherboard')
        motherboard.send_keys(Keys.RETURN)
        error_message = self.browser.find_element_by_class_name('error')
        self.assertIn('Incompatible components', error_message.text)

    def test_budget_tracking(self):
        self.browser.get('http://localhost:8000')
        budget = self.browser.find_element_by_name('budget')
        budget.send_keys('1000')
        budget.send_keys(Keys.RETURN)
        total_cost = self.browser.find_element_by_id('total_cost')
        self.assertLessEqual(int(total_cost.text), 1000)

    def test_recommendations(self):
        self.browser.get('http://localhost:8000')
        use_case = self.browser.find_element_by_name('use_case')
        use_case.send_keys('Gaming')
        use_case.send_keys(Keys.RETURN)
        recommended_components = self.browser.find_element_by_id('recommended_components')
        self.assertIn('Gaming', recommended_components.text)

if __name__ == '__main__':
    unittest.main()
```