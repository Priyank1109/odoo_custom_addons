{
    'name': 'Test Module',
    'version': '17.0.1.0',
    'category': 'Test Module',
    'summary': 'Test Module',
    'description': """
        Test Module
    """,
    'author': 'Priyank Paththa',
    'depends': ['sale'],
    'data': [
       "security\ir.model.access.csv",
       "views\Test_views.xml",
       "report\products.xml",
       "report\ir_action_report.xml"
    ],
    'installable': True,
    'application': True,
}
