#genrate excel report
from odoo import models
import datetime

class ExportFile(models.AbstractModel):
    _name = 'report.project_estimation.report_export_xls'
    _inherit = 'report.report_xlsx.abstract'


    def generate_xlsx_report(self, workbook, data, estimation):
        sheet = workbook.add_worksheet('Estimation')
        bold = workbook.add_format({'bold': True, 'align': 'center'})
        style = workbook.add_format({'align': 'center'})
        wrap_format = workbook.add_format({'align': 'justify', 'valign': 'top', 'text_wrap': True})
        sheet.set_column('A:A', 20)
        sheet.set_column('B:B', 40)
        sheet.set_column('C:C', 55)
        sheet.set_column('D:D', 45)
        sheet.set_column('E:E', 15)
        sheet.set_column('F:F', 15)
        row = 0
        col = 0
        sheet.write(row, col, 'Technology_Name', bold)
        sheet.write(row, col + 1, 'Category_Name', bold)
        sheet.write(row, col + 2, 'Module_Name', bold)
        sheet.write(row, col + 3, 'Notes', bold)
        sheet.write(row, col + 4, 'Hours', bold)
        sheet.write(row, col + 5, 'Total_Hours', bold)
        for i in estimation:
            for rec in i.project_detail_ids:
                row += 1
                sheet.write(row, col, rec.technology_id.technology_name)
                sheet.write(row, col + 1, rec.category_id.category_name)
                sheet.write(row, col + 2, rec.module_name)
                if rec.name == False:
                    sheet.write(row, col + 3, " ", wrap_format)
                else:
                    sheet.write(row, col + 3, rec.name, wrap_format)
                    notes_length = len(rec.name)
                    if notes_length > 50:
                        sheet.set_row(row, notes_length // 50 * 30)  # Adjust the height of the row based on the content length
                sheet.write(row, col + 4, rec.hours, style)
            sheet.write(row, col + 5, i.total_hours, style)
        
        sheet.set_column(col + 3, col + 3, 100)
           

class SampleReport(models.AbstractModel):
    _name = 'report.project_estimation.sample_report_xls'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self,workbook,data,estimation):
        sheet = workbook.add_worksheet('SampleReport')
        bold = workbook.add_format({'bold':True,'align':'center'})
        style = workbook.add_format({'align':'center'})
        sheet.set_column('A:A',20)
        sheet.set_column('B:B',20)
        sheet.set_column('C:C',20)
        sheet.set_column('D:D',50)
        sheet.set_column('E:E',15)
        sheet.set_column('F:F',15)
        row = 0
        col = 0
        sheet.write(row,col,'Technology_Name',bold)
        sheet.write(row,col+1,'Category_Name',bold)
        sheet.write(row,col+2,'Module_Name',bold)   
        sheet.write(row,col+3,'Notes',bold)
        sheet.write(row,col+4,'Hours',bold)
        sheet.write(row,col+5,'Total_Hours',bold)
        for i in range(0,1):
            row += 1 
            sheet.write(row,col,'Python')
            sheet.write(row,col+1,'python script')
            sheet.write(row,col+2,'Make input file')
            sheet.write(row,col+3,'The Script will return significant word from text')
            sheet.write(row,col+4,8)
            sheet.write('A3:A3','Python')
            sheet.write('B3:B3','python script')
            sheet.write('C3:C3','Extract data')
            sheet.write('D3:D3','The second script will exract data from youtube search')
            sheet.write('E3:E3',8)
            sheet.write('A4:A4','Python')
            sheet.write('B4:B4','python script')
            sheet.write('C4:C4','Deployment')
            sheet.write('D4:D4','Deployement of project')
            sheet.write('E4:E4',8)
            sheet.write('F4:F4',24)





       
            
          