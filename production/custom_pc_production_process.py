```python
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class CustomPCProductionProcess(models.Model):
    _name = 'custom.pc.production.process'
    _description = 'Custom PC Production Process'

    build_id = fields.Many2one('build.configurations', string='Build Configuration')
    task_ids = fields.One2many('custom.pc.build.task', 'process_id', string='Build Tasks')
    quality_check = fields.Boolean('Quality Check Passed', default=False)
    assembly_service = fields.Selection([
        ('none', 'None'),
        ('basic', 'Basic'),
        ('premium', 'Premium'),
    ], string='Assembly Service', default='none')

    @api.constrains('build_id')
    def _check_build_id(self):
        for record in self:
            if not record.build_id:
                raise ValidationError("Build Configuration is required.")

    @api.constrains('task_ids')
    def _check_task_ids(self):
        for record in self:
            if not record.task_ids:
                raise ValidationError("At least one build task is required.")

    @api.constrains('quality_check')
    def _check_quality_check(self):
        for record in self:
            if not record.quality_check:
                raise ValidationError("Quality Check must be passed before proceeding.")

    @api.onchange('assembly_service')
    def _onchange_assembly_service(self):
        if self.assembly_service == 'none':
            self.task_ids = [(5, 0, 0)]
        elif self.assembly_service == 'basic':
            self.task_ids = [(0, 0, {'name': 'Basic Assembly', 'status': 'pending'})]
        elif self.assembly_service == 'premium':
            self.task_ids = [(0, 0, {'name': 'Premium Assembly', 'status': 'pending'})]

class CustomPCBuildTask(models.Model):
    _name = 'custom.pc.build.task'
    _description = 'Custom PC Build Task'

    name = fields.Char('Task Name')
    status = fields.Selection([
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ], string='Status', default='pending')
    process_id = fields.Many2one('custom.pc.production.process', string='Production Process')
```
