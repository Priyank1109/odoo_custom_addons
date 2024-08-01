
{
    'name': 'Employee Award',
    'version': '15.0.0.0',
    'category': 'Human Resources',
    'summary': """Employee Award""",
    'description': """This Application helps to track record of employee's award.""",
    'author': 'Doyenhub Software Solution',
    'company': 'Doyenhub Software Solution',
    'maintainer': 'Doyenhub Software Solution',
    'website':'https://www.doyenhub.com/',
	"price": 9,
    "currency": 'USD',
    'depends': ['mail', 'hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/custom_form_report_template.xml',
        'data/custom_form_report_action.xml',
        'views/emp_award_view.xml',
    ],

    'demo': [],
    'application': True,
    'installable': True,
    'auto_install': False,
 	"images": ['static/description/banner.png'],
	'license': 'OPL-1'
}
