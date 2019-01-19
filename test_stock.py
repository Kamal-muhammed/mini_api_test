import unittest
from flask_app import stock, server as app
import json

class TestStock(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_add_product(self):
        product = {
            'name': 'maize',
            'quantity': 78587
        }
        response = self.app.post('/stock', data=json.dumps(product))
        self.assertEqual(response.status_code, 201)
        self.assertIs(type(stock), list)
        self.assertEqual(len(stock), 1)
        self.assertIn(product, stock)
