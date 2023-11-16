```python
from odoo import models, fields, api

class CustomPCInvoice(models.Model):
    _inherit = 'account.move'

    build_configuration_id = fields.Many2one('build.configurations', string='Build Configuration')

    @api.onchange('build_configuration_id')
    def _onchange_build_configuration_id(self):
        if self.build_configuration_id:
            self.invoice_line_ids = [(5, 0, 0)]
            for line in self.build_configuration_id.component_ids:
                invoice_line = self.env['account.move.line'].new({
                    'product_id': line.product_id.id,
                    'quantity': line.quantity,
                    'price_unit': line.price_unit,
                    'name': line.product_id.name,
                    'discount': line.discount,
                    'tax_ids': [(6, 0, line.tax_id.ids)],
                })
                invoice_line._onchange_product_id()
                self.invoice_line_ids += invoice_line

    def action_post(self):
        res = super().action_post()
        if self.build_configuration_id:
            self.build_configuration_id.write({'state': 'invoiced'})
        return res
```