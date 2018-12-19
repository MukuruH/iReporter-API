import unittest
import json
from app.app import app



class TestIncident(unittest.TestCase):

    def setUp(self):
        self.app_tester = app.test_client()

    def test_no_data(self):
        response = self.app_tester.get('/api/v1/redflags')
        data =  json.loads(response.data)
        # self.assertEqual(data["status"],200)
        self.assertEqual(data["message"],"There is nothing to output")

    


