from odoo import models, fields, _, api, exceptions
from datetime import datetime, timedelta


class EmployeeAward(models.Model):
    _name = 'hr.emp.award'
    _description = 'HR Employee Award'
    _rec_name = 'name'

    name = fields.Char(string="Name")


class EmployeeAwardForm(models.Model):
    _name = 'hr.emp.award.form'
    _description = 'HR Employee Award Form'
    _rec_name = 'award_name'

    employee_id = fields.Many2one('hr.employee')
    employee_name = fields.Many2one('hr.employee', string="Employee", help='Name of the employee for whom the request is creating')
    award_by = fields.Many2one('hr.employee', string="Award Given By", help='Name of the employee who give award')
    award_type = fields.Many2one('hr.emp.award',
                 string='Award Type', help='Award Type')
    award_name = fields.Char(string="Award Name")
    date = fields.Date(string="Date", default=datetime.today())
    win_amount = fields.Float(string="Winning Amount")
    award_detail = fields.Html(string="Detail")


class EmployeeAwardFormInherit(models.Model):
    _inherit = 'hr.employee'

    emp_id = fields.One2many(
        'hr.emp.award.form', 'employee_name',
        string='award_by', help='Award Type')

