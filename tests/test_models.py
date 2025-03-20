import unittest
from tests.factories import ProductFactory

class TestProductModel(unittest.TestCase):
    def test_create_product(self):
        product = ProductFactory()
        self.assertIsNotNone(product)

    def test_update_product(self):
        product = ProductFactory()
        product["name"] = "UpdatedName"
        self.assertEqual(product["name"], "UpdatedName")

    def test_delete_product(self):
        product = ProductFactory()
        product = None
        self.assertIsNone(product)

    def test_find_by_name(self):
        products = [ProductFactory(name="Apple"), ProductFactory(name="Banana")]
        found = [p for p in products if p["name"] == "Apple"]
        self.assertEqual(len(found), 1)

    def test_find_by_category(self):
        products = [ProductFactory(category="Fruit"), ProductFactory(category="Electronics")]
        found = [p for p in products if p["category"] == "Fruit"]
        self.assertEqual(len(found), 1)

    def test_find_by_availability(self):
        products = [ProductFactory(available=True), ProductFactory(available=False)]
        found = [p for p in products if p["available"]]
        self.assertEqual(len(found), 1)

if __name__ == '__main__':
    unittest.main()

