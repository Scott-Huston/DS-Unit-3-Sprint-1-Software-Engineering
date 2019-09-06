import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)
    
    def test_default_product_weight(self):
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_stealability_explode(self):
        prod = Product('Test Product', 100, 5, 100)
        self.assertEqual(prod.explode(), "...BABOOM!!")
        self.assertEqual(prod.stealability(), "Very stealable!")

class AcmeReportTests(unittest.TestCase):
    """Making sure the reports work"""
    def test_default_num_products(self):
        prod_list = generate_products()
        self.assertEqual(len(prod_list),30)
    
    def test_legal_names(self):
        prod_list = generate_products()
        for prod in prod_list:
            name = prod.name
            split_name = name.split()
            self.assertIn(split_name[0], ADJECTIVES)
            self.assertIn(split_name[1], NOUNS)
            concat_name = split_name[0]+' '+split_name[1]
            self.assertEqual(concat_name, prod.name)

if __name__ == '__main__':
    unittest.main()
