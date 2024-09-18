{
    'name': "HR Hospital",
    'version': '17.0.1.0.0',
    'author': 'Alis',
    'website': 'https://www.alis.com',
    'category': 'Customization',
    'license': 'OPL-1',
    'depends': ['base'],
    'external_dependencies': {
        'python': [],
    },
    'data': [
        'security/ir.model.access.csv',
        'data/hr_hospital_disease.xml',

        'views/hr_hospital_menu.xml',
        'views/hr_hospital_doctor_views.xml',
        'views/hr_hospital_patient_views.xml',
    ],
    'demo': [
        'demo/doctor_demo.xml',
        'demo/hr_hospital.patient.csv',
    ],
    'installable': True,
    'auto_install': False,
    'images': ['static/description/icon.png'],
}
