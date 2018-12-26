import unittest
import json
from app.app import app
from app.models import User, Incident


class TestPostIncident(unittest.TestCase):

    def setUp(self):
        self.app_tester = app.test_client()
        
    def test_get_all(self):
    
        random_data = {
                        "createdBy":"hamza",
                        "types":"red-flag",
                        "location":"mbra",
                        "status":"on going",
                        "Images":"hjj",
                        "Videos":"hj",
                        "comment":"ghd"
                    }
        self.app_tester.post('/api/v1/red-flags',json =random_data)

        random_data = {
                        "createdBy":"nino",
                        "types":"red-flag",
                        "location":"malaba",
                        "status":"rejected",
                        "Images":"ayo",
                        "Videos":"alloha",
                        "comment":"on the low"
                    }
        self.app_tester.post('/api/v1/red-flags',json =random_data)

        response = self.app_tester.get('/api/v1/red-flags')
        data =  json.loads(response.data)
        self.assertEqual(data["status"],200)


    
    def test_specific(self):
        
        random_data = {
                        "createdBy":"hamza",
                        "types":"red-flag",
                        "location":"mbra",
                        "status":"on going",
                        "Images":"hjj",
                        "Videos":"hj",
                        "comment":"ghd"
                    }
        self.app_tester.post('/api/v1/red-flags',json =random_data)

        random_data = {
                        "createdBy":"nino",
                        "types":"red-flag",
                        "location":"malaba",
                        "status":"rejected",
                        "Images":"ayo",
                        "Videos":"alloha",
                        "comment":"on the low"
                    }
        self.app_tester.post('/api/v1/red-flags',json =random_data)
        response = self.app_tester.get('/api/v1/red-flags')
        data =  json.loads(response.data)
        self.assertEqual(data["status"],200)
        self.assertEqual(data["message"],"There is nothing to output")