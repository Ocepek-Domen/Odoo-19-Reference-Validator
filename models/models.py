from odoo import models, api, _
from odoo.exceptions import ValidationError


class ValidationMixin(models.AbstractModel):
    """Mixin class for default_code validation logic."""
    _name = 'validation.mixin'
    _description = 'Mixin class for default_code validation logic'

    def _validate_semicolons(self, code):
        """Helper method to validate semicolon count in default_code."""
        # Skip validation if field is empty or whitespace only
        if not code or not code.strip():
            return None

        # Count the number of semicolons in the reference field
        semicolon_count = code.count(';')
        if semicolon_count not in (0, 3):
            # Return the error message if validation fails
            return _(
                'Polje Referenca mora vsebovati natanko 3 podpičja ";". Polje lahko vsebuje tudi poševnico "/" in zvezdice "*".\n\n'
                '═══ BASIC (1-on-1) ═══\n'
                'Xiaomi;Redmi Note 13 Pro 4g;Popravilo kamere;\n'
                'Apple;iPhone 16 Plus;Menjava baterije;\n'
                'KuKirin;G2 Pro;Nosilec blatnika;\n\n'
                '═══ GENERAL (1-to-many) - Vsi brandi, vse znamke ═══\n'
                '*;*;Garancija: Popravilo level 1;\n'
                '*;*;Garancija: Pošiljanje preko pošte - TV;\n\n'
                '═══ STORITVE - Dodane storitve v trgovini in trackerju ═══\n'
                '*;*;Obvescanje stanja servisa prek SMSa;\n'
                '*;*;Dodatno zavarovanje pošiljke;\n'
                '*;*;*kurirske službe;\n\n'
                '═══ MULTI (1-to-many) ═══\n'
                'Samsung;*S24 FE;Menjava baterije;         → Vsi S24 FE\n'
                'Asus;Zenfone 8 Flip;Menjava ekrana*;      → Več storitev menjave ekrana\n'
                'Segway;*;Menjava pogonskega*;             → Vsi modeli Segway\n'
                'Samsung;Galaxy Xcover 4*;Popravilo ohišja; → Vse variacije Xcover 4/4S\n'
                '*;iPhone 13 Pro Max;Popravilo stekla*;    → Original in B klasa\n\n'
                '═══ EXTRA ═══\n'
                'Apple;*16e/*17;Menjava ekrana*;           → Modeli z 16e ali 17\n'
            )
        return None


class ProductTemplate(models.Model):
    _inherit = ['product.template', 'validation.mixin']

    @api.onchange('default_code')
    def _onchange_default_code(self):
        """Validate default_code on change in the UI (real-time validation)."""
        error_message = self._validate_semicolons(self.default_code)
        if error_message:
            return {
                'warning': {
                    'title': _('Napaka pri validaciji'),
                    'message': error_message
                }
            }

    @api.constrains('default_code')
    def _check_default_code_semicolons(self):
        """Validate that default_code contains exactly 3 semicolons when not empty (database-level validation)."""
        for rec in self:
            error_message = rec._validate_semicolons(rec.default_code)
            if error_message:
                raise ValidationError(error_message)


class ProductProduct(models.Model):
    _inherit = ['product.product', 'validation.mixin']

    @api.onchange('default_code')
    def _onchange_default_code(self):
        """Validate default_code on change in the UI (real-time validation)."""
        error_message = self._validate_semicolons(self.default_code)
        if error_message:
            return {
                'warning': {
                    'title': _('Napaka pri validaciji'),
                    'message': error_message
                }
            }

    @api.constrains('default_code')
    def _check_default_code_semicolons(self):
        """Validate that default_code contains exactly 3 semicolons when not empty (database-level validation)."""
        for rec in self:
            error_message = rec._validate_semicolons(rec.default_code)
            if error_message:
                raise ValidationError(error_message)