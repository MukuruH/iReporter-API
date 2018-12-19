import unittest
import json
from app.app import app



class TestIncidentWithData(unittest.TestCase):

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
        self.app_tester.post('/api/v1/redflags',json =random_data)

        random_data = {
                        "createdBy":"nino",
                        "types":"red-flag",
                        "location":"malaba",
                        "status":"rejected",
                        "Images":"ayo",
                        "Videos":"alloha",
                        "comment":"on the low"
                    }
        self.app_tester.post('/api/v1/redflags',json =random_data)

        response = self.app_tester.get('/api/v1/redflags')
        data =  json.loads(response.data)
        self.assertEqual(data["status"],200)
