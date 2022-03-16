{
    'name': 'Nexapp Report order date',
    'summary': 'Removed the hour from the shipping date in the report print',
    'description': """Removed the hour from the shipping date in the report print""",
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
