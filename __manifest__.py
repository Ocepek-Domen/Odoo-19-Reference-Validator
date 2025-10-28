{
    'name': "Domen Module - Product Reference Code Validator",

    'summary': "Validates product reference code format with semicolon validation",

    'description': """
Product Reference Code Validator
================================

This module adds validation to the product reference code (default_code) field
for both product.template and product.product models.

Features:
---------
* Validates that the reference code contains exactly 3 semicolons
* Real-time validation during data entry using @api.onchange
* Database-level validation using @api.constrains
* Comprehensive error messages with examples of valid formats
* Supports wildcard (*) and alternative format patterns

Valid Formats:
--------------
* Basic format: Brand;Model;Service;
* Wildcards supported: *;*;Service;
* Multiple formats: Brand;*Model;Service*;

The validation ensures data consistency for your product catalog.
    """,

    'author': "Domen Ocepek, OptiCode.si",
    'website': "https://www.opticode.si",

    'category': 'Inventory/Inventory',
    'version': '0.1.1',
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product'],

    'installable': True,
    'application': False,
    'auto_install': False,

    'images': ['static/description/icon.png']
}
