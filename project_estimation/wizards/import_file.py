#import task
from odoo import fields, models, _
import datetime 
import pandas as pd
import base64
from odoo.exceptions import ValidationError


class ImportFile(models.TransientModel):
    _name = 'import.file'
    _inherit = 'estimation.info'

    import_file = fields.Binary('Import File')

    def import_xls(self):
        tech_id = self.technology_id.id
        tag_id = self.tag_ids.id
        # -----------------read excel file -------------------
        data = pd.read_excel(base64.decodebytes(self.import_file))
        df = pd.DataFrame(data,columns=['Technology_Name','Category_Name','Module_Name', 'Hours', 'Notes'])
        
        for i in range(len(df.index)):
            # -----------------end of excel file -------------------

            # -------------------category object ---------------------
            category_id = 0
            technology_id = 0
            if self.env['project.category'].search([('category_name', '=', df['Category_Name'][i])]):
                category_id = self.env['project.category'].search([('category_name', '=', df['Category_Name'][i])]).id
            else:
                cat = self.env['project.category'].create({
                        'category_name':df['Category_Name'][i]
                    }).id
                category_id = cat

            if self.env['technology.info'].search([('technology_name','=',df['Technology_Name'][i])]):
                technology_id = self.env['technology.info'].search([('technology_name','=',df['Technology_Name'][i])]).id
            else:
                tech = self.env['technology.info'].create({
                        'technology_name':df['Technology_Name'][i]
                    }).id
                technology_id = tech

            # --------------------add data on add task table -------
            task_obj = self.env['add.task'].search([])
            task_id = task_obj.create({
                'technology_id':technology_id, #estimation technology_id
                # 'tag_ids':tag_id,
                'category_id':category_id,
                'module_name':df['Module_Name'][i],
                'hours':df['Hours'][i],
                'task_notes':df['Notes'][i]
                }).id
           
            # -------------------------------------------------------
            if self.env['estimation.info'].browse(self.env.context.get('active_id')):
                project  = self.env['estimation.info'].browse(self.env.context.get('active_id'))
                # ------------------insert data on project_details--------
                project.write({
                    'project_detail_ids':[(0,0,{
                        'technology_id':technology_id,
                        'category_id':category_id,
                        'task_id':task_id,
                        'module_name':df['Module_Name'][i],
                        'hours':df['Hours'][i],
                        'name':df['Notes'][i]
                    })]
                })
                i + 1
            else:
                pass
            
           
       

    
