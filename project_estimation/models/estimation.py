from odoo import api, models,fields,_
import datetime 
import pandas as pd
from odoo.exceptions import ValidationError


class EmployeeNameModel(models.Model):
    _name = 'employee.name'
    _description = 'Employee Name'
    _rec_name = 'emloyee_name'

    emloyee_name = fields.Char(string="Employee Name",tracking=1)

class EstimationModel(models.Model):
    _name = 'estimation.info'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'estimation info'
    _rec_name = 'title'

    employee_id = fields.Many2one('res.users',string="Assign to",tracking=1)
    category = fields.Selection([('fixed', 'Fixed Price'), ('monthly', 'Monthly Price'),('hourly','Hourly Price')], string='Project Category',default="fixed")
    description = fields.Text(string='Description',tracking=1)
    estimation_file = fields.Many2many('ir.attachment',string="Upload Project Document", tracking=1)
    file_name = fields.Char('File Name')
    created_at = fields.Datetime(string='Created At',default=fields.Datetime.now)
    created_by = fields.Many2one('res.users', string="Created By",default=lambda self:self.env.user)
    updated_at = fields.Datetime(string='Updated At')
    updated_by = fields.Many2one('res.users', string="Updated By",default=lambda self:self.env.user)
    estimation_type = fields.Selection([('internal', 'Internal'), ('external', 'External')], string='Estimation type')
    active = fields.Boolean(string="Active",default=True)
    assign_to = fields.Char(string="Assign To")
    review_date = fields.Datetime(string='Review Date',default=fields.Datetime.now)
    review_by = fields.Many2one('res.users',string='Review By')
    project_detail_ids = fields.One2many(
    'project.details','estimation_id',string="Project Details")
    project_manager = fields.Many2one('res.users', string="Project Manager")
    technology_id = fields.Many2many('technology.info',string="Technology Name",tracking=1)
    title = fields.Char(string="Title",tracking=1)
    tag_ids = fields.Many2many('project.tag', string="Project Tag",store=True)
    Last_submitted_date = fields.Date(string="Last Submitted Date")
    notes = fields.Html(string="Additional Notes")
    total_hours = fields.Float(string="Total Hours", compute='_compute_final_total')
    xls_file = fields.Binary('Import File')
    category_id = fields.Many2one('project.category',string='Category Name')
    context = fields.Char(string='Context')

    def export_button(self):
        lists = []
        data_dict = {}
        for rec in self:
            for record in rec.project_detail_ids:
                dicts = {}
                dicts['Technology_Name'] = record.technology_id.technology_name
                dicts['Category_Name'] = record.category_id.category_name
                dicts['Module_Name'] = record.module_name
                dicts['Hours'] = record.hours
                dicts['Notes'] = record.name
                dicts['Total_Hours']= self.total_hours
                df = pd.DataFrame.from_dict(lists)
                lists.append(dicts)
                return self.env.ref('project_estimation.report_export_file_xls').report_action(self,data=data_dict)
    
    def sample_report(self):
        return self.env.ref('project_estimation.sample_report_export_file_xls').report_action(self)
    
    @api.depends('project_detail_ids.hours')
    def _compute_final_total(self):
        for hour in self:
            total = 0.0
            for line in hour.project_detail_ids:
                total += line.hours
            hour.total_hours = total
  
    @api.returns('self', lambda value: value.id)
    def copy(self, default=None):
        if default is None:
            default = {}
        if not default.get('employee_id'):
            default['employee_id'] = _("%s (copy)", self.title)
        return super(EstimationModel,self).copy(default=default)


class ProjectDetails(models.Model):
    _name = 'project.details'
    _description = 'project details'

    sequence = fields.Integer(default=10)
    module_name = fields.Char(string="Module Name")
    hours = fields.Float(string="hours",readonly=False,store=True)
    task_notes = fields.Text(string="Notes",readonly=False,store=True)
    task_id = fields.Many2one('add.task',string='Module Name..')
    total_hours = fields.Float(string="Total hours",tracking=1)
    estimation_id = fields.Many2one('estimation.info', string="estimation")
    final_total = fields.Char(string="Final Total", compute="_compute_final_total",store=True)
    name = fields.Text(string='Notes',readonly=False,required=False,store=True)
    display_type = fields.Selection([('line_section', "Section"),('line_note', "Note")], default=False, help="Technical field for UX purpose.")
    category_id = fields.Many2one('project.category',string='Category Name',readonly=False,store=True)
    technology_id = fields.Many2one('technology.info',string="Technology Name",tracking=1,store=True) 
    # related='estimation_id.technology_id'
    # domain=[('id','in',estimation_id.technology_id.id)]

    # @api.onchange('technology_id')
    # def _onchange_technology_id(self):
    #     for rec in self:
    #         if rec.technology_id:
    #             raise ValidationError(_("Your record is too small:"))

#add task 
class AddTask(models.Model):
    _name = 'add.task'
    _description = 'Add technology and tags wise task'
    _rec_name = 'module_name'

    module_name = fields.Char(string="Module Name")
    project_id = fields.Many2one('project.details',string='project')
    technology_id = fields.Many2one('technology.info',string="Technology Name",tracking=1)
    category_id = fields.Many2one('project.category',string='Category Name')
    # tag_ids = fields.Many2one('project.tag', string="Project Tag")
    hours = fields.Float(string="hours")
    total_hours = fields.Float(string="Total hours",tracking=1)
    estimation_id = fields.Many2one('estimation.info', string="estimation")
    name = fields.Text(string='Notes', required=False)
    notes = fields.Char(string='Add Notes')
    task_notes = fields.Text(string='Add Notes')
    
    def default_get(self,fields):
        res = super(AddTask, self).default_get(fields)
        res['module_name'] = self._context.get('default_name')
        
        rec = self.env['project.details'].browse(self.env.context.get('active_id'))
        # res['technology_id'] = rec.technology_id.id 
        res['category_id'] = self._context.get('default_category_id')
        return res

    def name_get(self):
        task_list = []
        for record in self:
            name = record.module_name 
            # + "[" + str(datetime.timedelta(hours=record.hours)) + "  " + "Hours"+"]"
            task_list.append((record.id,name))
        return task_list


class ProjectCategory(models.Model):
    _name = "project.category"
    _description = "Add project category"
    _rec_name = "category_name"

    category_name = fields.Char(string='Category Name')


   

   


    
       
    
    
    

   
    










   

  

   