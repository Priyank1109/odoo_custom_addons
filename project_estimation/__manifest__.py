#project estimation menifest file
{
    'name': 'Project Estimation',
    'version': '1.0.0',
    'sequence': -100,
    'category': 'Project',
    'author': 'Doyenhub Software Solution',
    'company': 'Doyenhub Software Solution',
    'maintainer': 'Doyenhub Software Solution',
    'summary': 'Project Estimation',
    'description': """Project estimation is a critical process in planning and managing successful projects. It involves analyzing project requirements, resources, and deliverables to determine the effort, time, and cost required for successful completion. The Project Estimation document serves as a foundation for decision-making, resource allocation, and project scheduling.""",
    'depends': ['mail','base', 'web','project','hr'],
    'external_dependencies': {
        'python': ['pandas','openpyxl']
    },
    'images': ['static/description/banner.png'],
    'data': [
      'security/ir.model.access.csv',
      'wizards/import_file.xml',
      'views/menu.xml',
      'views/estimation.xml',
      'views/tag_view.xml',
      'views/technology_view.xml',
      'views/employee.xml',
      'static/src/js/add_section_and_notes.js',
      'views/addtask.xml',
      'views/category.xml',
      'report/report.xml'
    ],
    'assets': {
          'web.assets_backend': [
          'web_export_view/static/src/js/web_export_view.js',
          'web_export_view/static/tests/web_export_view_tests.js',
      ]
    },
    'demo': [],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'assets': {},
    'application': True, # display your module in app list
    'website':'https://www.doyenhub.com/',
}
