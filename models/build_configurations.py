```python
from odoo import models, fields

class BuildConfigurations(models.Model):
    _name = 'build.configurations'
    _description = 'Build Configurations'

    name = fields.Char(string='Configuration Name', required=True)
    user_id = fields.Many2one('res.users', string='User')
    cpu_id = fields.Many2one('product.template', string='CPU')
    motherboard_id = fields.Many2one('product.template', string='Motherboard')
    ram_id = fields.Many2one('product.template', string='RAM')
    gpu_id = fields.Many2one('product.template', string='GPU')
    storage_id = fields.Many2one('product.template', string='Storage')
    power_supply_id = fields.Many2one('product.template', string='Power Supply')
    case_id = fields.Many2one('product.template', string='Computer Case')
    cooler_id = fields.Many2one('product.template', string='CPU Cooler')
    fans_id = fields.Many2one('product.template', string='Extra Case Fans')
    budget = fields.Float(string='Budget')
    total_cost = fields.Float(string='Total Cost', compute='_compute_total_cost')
    is_compatible = fields.Boolean(string='Is Compatible', compute='_check_compatibility')
    recommendation_id = fields.Many2one('product.template', string='Recommended Component')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done'),
    ], string='Status', default='draft')

    def _compute_total_cost(self):
        for record in self:
            total_cost = sum([
                record.cpu_id.list_price,
                record.motherboard_id.list_price,
                record.ram_id.list_price,
                record.gpu_id.list_price,
                record.storage_id.list_price,
                record.power_supply_id.list_price,
                record.case_id.list_price,
                record.cooler_id.list_price,
                record.fans_id.list_price,
            ])
            record.total_cost = total_cost

    def _check_compatibility(self):
        # This is a placeholder. Actual compatibility check logic will be implemented here.
        pass
```