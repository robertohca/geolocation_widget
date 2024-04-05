# -*- coding: utf-8 -*-
{
    'name': "GeoLocationField Widget",

    'summary': """
        The GeoLocationField widget allows users to input and visualize geographical coordinates, 
        with the added functionality of directly accessing Google Maps from the field value.""",

    'description': """
        The GeoLocationField widget is designed to provide geolocation functionality within an Odoo module. It allows users to 
        input and display geographical coordinates, typically latitude and longitude, in a text field. Additionally, it enhances 
        user experience by enabling them to access Google Maps directly from the field value. Clicking on the field opens Google Maps 
        in a new browser tab, centered on the specified location. This widget simplifies the process of capturing and visualizing 
        geospatial data, enhancing the usability of Odoo applications for location-based tasks. It can be integrated into custom modules 
        to facilitate geolocation-related functionalities such as mapping, tracking, and location-based searches.""",

    'author': "Roberto Camejo",
    'website': "https://github.com/robertohca",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tools',
    'version': '16.0.1.0.0',
    'price': 9.99,
    'currency': 'USD',
    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [],
    'assets': {
        'web.assets_backend': [
            'geolocation_widget/static/src/js/*.js',
            'geolocation_widget/static/src/xml/*.xml',
        ],
    },
    'application': True,
    'installable': True,
    'auto_install': False,
}
