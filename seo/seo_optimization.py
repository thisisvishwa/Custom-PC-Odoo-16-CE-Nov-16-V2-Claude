```python
from odoo import models, fields, api

class SEOOptimization(models.Model):
    _inherit = 'product.template'

    meta_title = fields.Char('Meta Title')
    meta_description = fields.Text('Meta Description')
    structured_data = fields.Text('Structured Data')

    @api.onchange('name')
    def _onchange_name(self):
        # Automatically generate meta title and description when product name changes
        self.meta_title = f"Buy {self.name} for Custom PC | YourStoreName"
        self.meta_description = f"Configure your custom PC with {self.name}. High quality, compatible with all major brands. Order now from YourStoreName."

    @api.model
    def create(self, vals):
        # Generate structured data for rich snippets
        structured_data = {
            "@context": "https://schema.org/",
            "@type": "Product",
            "name": vals.get('name'),
            "image": vals.get('image'),
            "description": vals.get('description'),
            "sku": vals.get('default_code'),
            "mpn": vals.get('manufacturer_pref'),
            "brand": {
                "@type": "Brand",
                "name": vals.get('brand_id')
            },
            "offers": {
                "@type": "Offer",
                "priceCurrency": "USD",
                "price": vals.get('list_price'),
                "availability": "https://schema.org/InStock",
            }
        }
        vals['structured_data'] = json.dumps(structured_data)
        return super().create(vals)
```