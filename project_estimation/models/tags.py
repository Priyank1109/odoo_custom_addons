#add tags
from odoo import api, models, fields, _


class TagModel(models.Model):
    _name = 'project.tag'
    _description = 'project technology tag'

    name = fields.Char(string="Tag name")
    active = fields.Boolean(string="Active", default=True, copy=False)

    _sql_constraints = [
        ('tag_name_unique', 'unique(name, active)', 'Tag name must be unique !'),
    ]

    

