from odoo import _, api, fields, models,tools
from odoo.exceptions import ValidationError

class ProductCategory(models.Model):
    _name = 'product.categorys'
    _rec_name = 'catgory_name'
    
    
    catgory_name = fields.Char(string='catgory_name')
    product_line = fields.One2many("products",'category_id',string="Products")


class Products(models.Model):
    _name = 'products'
    _rec_name = 'product_name'
    
    category_id = fields.Many2one('product.categorys',string="catgory")
    product_name = fields.Char(string="product_name")
    buy_price = fields.Integer(string="Buying Price")
    sell_price = fields.Integer(string="Selling Price")
    profit = fields.Integer(string="Profit",compute="_compute_profit",inverse="_recompute_profit",readonly=False)
    
    
    @api.onchange('category_id')
    def onchange_category_id(self):
        pass
    
    @api.depends('buy_price','sell_price')
    def _compute_profit(self):
        self.profit = self.sell_price - self.buy_price
        
        
    def _recompute_profit(self):
        self.buy_price = self.sell_price - self.profit
        
class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    
    test_field = fields.Char(string="Test Field")
    
    
class ProductReport(models.Model):
    _name = 'product.report'
    _description = "Product Report"
    _rec_name = 'name'
    _auto = False
    
    name = fields.Char(string="product name")
    
    
    def init(self):
        tools.drop_view_if_exists(self.env.cr, self._table)
        self.env.cr.execute("""CREATE or REPLACE VIEW %s as (
                            SELECT
                                id,
                                product_name AS name
                            FROM
                                products
                            )""" % (self._table))
    
    
    
        
        