```python
from odoo import models, fields, api

class ComponentAvailabilityCheck(models.Model):
    _inherit = 'product.template'

    @api.model
    def check_component_availability(self):
        products = self.env['product.template'].search([('is_component','=',True)])
        for product in products:
            if product.qty_available <= 0:
                product.write({'website_published': False})
            else:
                product.write({'website_published': True})

    @api.model
    def scheduler_check_availability(self):
        self.check_component_availability()
```