import unittest
from service.routes import app

class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_list_all(self):
        response = self.client.get('/products')
        self.assertEqual(response.status_code, 200)

    def test_create(self):
        response = self.client.post('/products', json={"name": "Laptop", "category": "Electronics", "available": True})
        self.assertEqual(response.status_code, 201)

    def test_read(self):
        self.client.post('/products', json={"name": "Laptop", "category": "Electronics", "available": True})
        response = self.client.get('/products/1')
        self.assertEqual(response.status_code, 200)

    def test_update(self):
        self.client.post('/products', json={"name": "Laptop", "category": "Electronics", "available": True})
        response = self.client.put('/products/1', json={"name": "Updated Laptop"})
        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        self.client.post('/products', json={"name": "Laptop", "category": "Electronics", "available": True})
        response = self.client.delete('/products/1')
        self.assertEqual(response.status_code, 204)

    def test_search(self):
        self.client.post('/products', json={"name": "Laptop", "category": "Electronics", "available": True})
        response = self.client.get('/products/search?name=Laptop')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
