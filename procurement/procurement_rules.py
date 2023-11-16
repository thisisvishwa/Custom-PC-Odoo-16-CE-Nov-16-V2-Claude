```python
from odoo import models, fields, api

class ProcurementRules(models.Model):
    _inherit = 'procurement.rule'

    @api.multi
    def _run_move(self, move):
        if move.product_id.categ_id.name == 'PC Components':
            return self._run_custom_pc(move)
        return super(ProcurementRules, self)._run_move(move)

    @api.multi
    def _run_custom_pc(self, move):
        # Check component availability
        if not self.env['scheduler.component_availability_check'].check_availability(move.product_id):
            # If not available, set state to waiting another move
            move.state = 'waiting_another_move'
            return False
        # If available, proceed with procurement
        return super(ProcurementRules, self)._run_move(move)

    @api.multi
    def _get_custom_pc_supplier(self, product):
        # Override this method to implement custom supplier selection logic
        return product.seller_ids[0] if product.seller_ids else None
```