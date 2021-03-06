{
    'name' : 'Administrador de préstmos',
    'version': '0.0.1',
    'summary': 'Módulo para gestionar préstamos',
    'description': """Módulo para administrar los préstamos 
                    realizados y los cobros""",
    'category': 'Sale',
    'website': 'https://www.loanmanager.com',
    'depends': ['base'],
    'data': [
        # Data
        'data/ir_sequence_data.xml',

        'security/loanmanager_groups.xml',
        'security/loanmanager_prestamo_security.xml',
        'security/ir.model.access.csv',

        # Vistas
        'views/loan_manager_menus.xml',
        'views/res_users_views.xml',
        'views/sede_views.xml',
        'views/cliente_views.xml',
        'views/prestamo_views.xml',
    ],
    'installable': True,
}
