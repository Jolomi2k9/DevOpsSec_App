import unittest
from main import app

class BasicTestCase(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()

    def test_index_route(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
