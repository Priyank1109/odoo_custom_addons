from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Event(models.Model):
    _name = 'event.event'
    _description = 'Event'

    # Define the fields for the event model
    name = fields.Char(string='Event Name')
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    location = fields.Char(string='Location')
    seats = fields.Integer(string='Seats')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done')
    ], string='State', default='draft')  # Default state is set to 'draft'

    @api.model
    def create(self, vals):
        # Ensure the event state is set to 'draft' when created
        vals['state'] = 'draft'
        return super(Event, self).create(vals)

    # Define button actions to change the state of the event
    def action_draft(self):
        self.state = 'draft'

    def action_confirm(self):
        self.state = 'confirmed'

    def action_done(self):
        self.state = 'done'        

    @api.constrains('start_date', 'end_date')
    def _check_dates(self):
        # Ensure that end_date is greater than or equal to start_date
        for record in self:
            if record.start_date and record.end_date and record.end_date < record.start_date:
                raise ValidationError('End date must be greater than or equal to start date.')
            
    @api.constrains('name')
    def _check_name(self):
        # Ensure that the event name is not empty
        for record in self:
            if not record.name:
                raise ValidationError('Event name cannot be empty.')        
