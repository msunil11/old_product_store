from odoo import fields, models
from datetime import datetime, date
from queue import Queue


class CreateOldProduct(models.Model):
    _name = 'old.product'
    _description = 'Old Product'

    name = fields.Char('Product Name')
    list_price = fields.Float(string='Sale price')
    default_code = fields.Char('Internal Reference')
    sequence = fields.Integer(default=10)

    def create_old_product(self):
        product_obj = self.env['product.template']
        irConfigParam = self.env['ir.config_parameter']
        max_queue_update = irConfigParam.sudo().get_param('queue_create_max_size')
        q = Queue(maxsize=int(max_queue_update))
        product_ids = product_obj.search([])
        for product in product_ids:
            product_list = self.search([('name', '=', product.name)])
            if len(q.queue) >= int(max_queue_update):
                q.queue.popleft()
            q.queue.append(product)
            if product.name not in product_list.mapped('name'):
                self.create({
                    'name': product.name or "",
                    'default_code': product.default_code or "",
                    'list_price': product.list_price or ""
                })


class ResConfigSettingsData(models.TransientModel):
    _inherit = 'res.config.settings'

    queue_create_max_size = fields.Char(string='Old product create Max size')

    def get_values(self):
        res = super(ResConfigSettingsData, self).get_values()
        res.update(
            queue_create_max_size=self.env['ir.config_parameter'].sudo().get_param('queue_create_max_size'),
        )
        return res

    def set_values(self):
        super(ResConfigSettingsData, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param('queue_create_max_size', self.queue_create_max_size)
