#add technology
from odoo import api, models,fields,_

class TechnologyModel(models.Model):
    _name = 'technology.info'
    _description = 'technology info'
    _rec_name = 'technology_name'
    
    technology_name = fields.Char(string="Technology Name",tracking=1)
     

   

   

  

   