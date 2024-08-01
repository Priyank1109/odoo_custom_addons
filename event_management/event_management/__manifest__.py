{
    'name': 'Event Management',
    'version': '17.0.1.0',
    'category': 'Events',
    'summary': 'Manage events',
    'description': """
        Module to manage events including creation, modification, and listing of events.
    """,
    'author': 'Roshan Pandey',
    'depends': [],
    'data': [
        'security/event_manager_recordrule.xml',
        'security/ir.model.access.csv',
        'views/event_views.xml',
    ],
    'installable': True,
    'application': True,
}
