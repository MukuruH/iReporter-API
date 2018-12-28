import unittest
import json
from app.app import app




class TestForIncident(unittest.TestCase):

    def setUp(self):
        self.app_tester = app.test_client()
        
   
    def test_posting_empty_data(self):

       #created data option not provided
        random_data = {
                        
                        "types":"",
                        "location":"",
                        "status":"",
                        "Images":"hjj",
                        "Videos":"hj",
                        "comment":"ghd"
                    }
        response = self.app_tester.post('/api/v1/red-flags',json =random_data)
        data =  json.loads(response.data)
        self.assertEqual(data["status"],400)

    def test_posting_data(self):
    

        random_data = {
                        "createdBy":"hamza",
                        "types":"red-flag",
                        "location":"mbra",
                        "status":"on going",
                        "Images":"hjj",
                        "Videos":"hj",
                        "comment":"ghd"
                    }
        response=self.app_tester.post('/api/v1/red-flags',json =random_data)
        data =  json.loads(response.data)
        self.assertEqual(data["status"],201)


  


    def test_get_all_with_data(self):
    
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
    


    
    def test_get_specific_one(self):
        
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
        response = self.app_tester.get('/api/v1/red-flags/2')
        data =  json.loads(response.data)
        self.assertEqual(data["status"],200)


    def test_get_out_of_range_specific_one(self):
        
        
        response = self.app_tester.get('/api/v1/red-flags/4')
        data =  json.loads(response.data)
        self.assertEqual(data["status"],404)


    def test_post_then_delete(self):
        
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
        response = self.app_tester.delete('/api/v1/red-flags/2')
        data =  json.loads(response.data)
        self.assertEqual(data["status"],200)
       

    def test_post_nothing_then_delete(self):
            
   
        response = self.app_tester.delete('/api/v1/red-flags/5')
        data =  json.loads(response.data)
        self.assertEqual(data["status"],404)
       

    
      