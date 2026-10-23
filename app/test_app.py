import unittest
from app import app

class AppTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home_returns_success(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["application"], "DevOps Demo App")

    def test_health_endpoint(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["status"], "healthy")

if __name__ == "__main__":
    unittest.main()
