```python
from odoo import models, fields

class CompatibilityRules(models.Model):
    _name = 'product.compatibility.rules'
    _description = 'Product Compatibility Rules'

    product_id = fields.Many2one('product.template', 'Product', required=True)
    compatible_with = fields.Many2many('product.template', 'product_compatibility_rel', 'product_id', 'compatible_id', string='Compatible Products')

    def check_compatibility(self, product_ids):
        incompatible_products = []
        for product in self.env['product.template'].browse(product_ids):
            compatibility_rules = self.search([('product_id', '=', product.id)])
            for rule in compatibility_rules:
                if set(product_ids) - set(rule.compatible_with.ids):
                    incompatible_products.append(product.name)
        return incompatible_products
```