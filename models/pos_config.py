from odoo import fields, models


class PosConfig(models.Model):
    """
        This is an Odoo model for Point of Sale (POS).
        It inherits the 'pos.config' model to add new fields.
    """
    _inherit = 'pos.config'

    receipt_template_id = fields.Many2one('pos.receipt', string='Receipt Template',
                                     help='Choose any receipt template')
    template_receipt = fields.Text(related='receipt_template_id.template_receipt',
                                 string='Receipt XML')
    logo = fields.Binary(related='company_id.logo', string='Logo',
                         readonly=False)
    is_custom_receipt = fields.Boolean(string='Is Custom Receipt',
                                       help='Indicates the receipt  template is '
                                            'custom or not')
