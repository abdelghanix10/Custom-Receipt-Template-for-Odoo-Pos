{
    'name': 'Custom Receipt Templates for POS',
    'version': '18.0.1.0.0',
    'category': 'Point of Sale',
    'summary': 'Customize POS receipt templates',
    'description': """
        Custom POS Receipt Templates
        ========================================
        
        Enhance your Point of Sale experience with custom receipt templates.

        Key Features:
        -------------
        * **Multiple Receipt Templates**: Choose from pre-templateed receipt templates
        * **Custom Receipt Layouts**: Personalize receipt appearance and branding
        * **Easy Configuration**: Simple setup through POS configuration
        * **Seamless Integration**: Works with existing POS workflow
        
        Perfect for:
        ------------
        * Retail stores needing branded receipts
        * Restaurants with custom receipt requirements
        * Any POS setup wanting enhanced receipt functionality
        
        Installation:
        -------------
        1. Install the module
        2. Configure receipt template in POS settings
        3. Start using custom receipt templates immediately
    """,
    'author': 'Abdelghani X',
    'website': 'https://www.AbdelghaniX.com',
    'license': 'OPL-1',
    'price': 19.99,
    'currency': 'USD',
    'images': ['static/description/banner.png'],
    'depends': ['point_of_sale'],
    'data': [
        'security/ir.model.access.csv',
        'data/pos_receipt_template1_data.xml',
        'data/pos_receipt_template2_data.xml',
        'data/pos_receipt_template3_data.xml',
        'views/pos_receipt_views.xml',
        'views/pos_config_views.xml'
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'pos_custom_receipt_template/static/src/js/receipt_template.js',
            'pos_custom_receipt_template/static/src/xml/order_receipt.xml',
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': False
}