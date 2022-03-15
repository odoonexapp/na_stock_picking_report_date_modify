{
    'name': 'Nexapp order date modified',
    'summary': 'Removed the hour from the shipping date and the deadline',
    'description': """Added the supplier DDT Number and date""",
    'version': '14.0.1.1',
    'images': ['images/date_screenshot.png'],
    'depends': [
        'stock',
        'l10n_it_delivery_note',

    ],
    'author': "Nexapp S.p.a.",
    'license': "AGPL-3",
    'website': 'https://www.nexapp.it',
    'category': 'Nexapp',
    'data': [
        'reports/stock_picking_report.xml',

    ],
}
