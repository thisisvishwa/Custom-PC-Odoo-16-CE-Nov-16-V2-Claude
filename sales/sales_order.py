```python
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class CustomPCSalesOrder(models.Model):
    _inherit = 'sale.order'

    build_configuration_id = fields.Many2one('build.configurations', string='Build Configuration')
    assembly_service = fields.Boolean(string='Assembly Service')

    @api.onchange('build_configuration_id')
    def _onchange_build_configuration_id(self):
        if self.build_configuration_id:
            self.order_line = [(5, 0, 0)]
            for component in self.build_configuration_id.component_ids:
                product = self.env['product.product'].search([('product_component_id', '=', component.id)], limit=1)
                if product:
                    line_vals = {
                        'product_id': product.id,
                        'product_uom_qty': 1,
                        'price_unit': product.lst_price,
                    }
                    self.order_line = [(0, 0, line_vals)]

    @api.constrains('assembly_service')
    def _check_assembly_service(self):
        if self.assembly_service and not self.build_configuration_id:
            raise ValidationError("Assembly service can only be selected for custom PC orders.")

    def action_confirm(self):
        res = super(CustomPCSalesOrder, self).action_confirm()
        if self.build_configuration_id and self.assembly_service:
            self.env['custom.pc.production.process'].create({
                'sale_order_id': self.id,
                'build_configuration_id': self.build_configuration_id.id,
            })
        return res
```