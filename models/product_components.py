```python
from odoo import models, fields

class ProductComponents(models.Model):
    _inherit = 'product.template'

    component_type = fields.Selection([
        ('cpu', 'CPU'),
        ('motherboard', 'Motherboard'),
        ('ram', 'RAM'),
        ('gpu', 'GPU'),
        ('storage', 'Storage'),
        ('power_supply', 'Power Supply'),
        ('case', 'Computer Case'),
        ('cooler', 'CPU Cooler'),
        ('fans', 'Extra Case Fans'),
    ], string='Component Type')

    cpu_type = fields.Selection([
        ('intel', 'Intel'),
        ('amd', 'AMD'),
    ], string='CPU Type', required_if_component_type='cpu')

    storage_type = fields.Selection([
        ('hdd', 'HDD'),
        ('ssd', 'SSD'),
        ('m2', 'M.2'),
    ], string='Storage Type', required_if_component_type='storage')

    power_supply_wattage = fields.Integer(string='Power Supply Wattage', required_if_component_type='power_supply')

    case_size = fields.Selection([
        ('mini_itx', 'Mini-ITX'),
        ('micro_atx', 'Micro-ATX'),
        ('atx', 'ATX'),
    ], string='Case Size', required_if_component_type='case')

    cooler_type = fields.Selection([
        ('air', 'Air Cooler'),
        ('liquid', 'Liquid Cooler'),
    ], string='Cooler Type', required_if_component_type='cooler')

    fan_size = fields.Integer(string='Fan Size (mm)', required_if_component_type='fans')

    def required_if_component_type(self, component_type):
        return self.component_type == component_type
```