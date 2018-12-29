import unittest
import json
from app.app_routes import app




class TestForIncident(unittest.TestCase):

    def setUp(self):
        self.app_tester = app.test_client()

    def test_a_get_all_with_no_data(self):
       
        response = self.app_tester.get('/api/v1/red-flags')
        data =  json.loads(response.data)
        self.assertEqual(data["status"],404)


    def test_a_patch_location_in_index_when_there_is_no_data(self):
            
        location = {"location": "mutungo"}
        response = self.app_tester.patch("/api/v1/red-flags/100/location" ,json=location)
        self.assertEqual(response.status_code, 404)

    
    
    def test_a_delete_when_there_is_no_data(self):
           
        response = self.app_tester.delete('/api/v1/red-flags/1')
        self.assertEqual(response.status_code, 404)
       
        
   
    def test_posting_data_missing_a_variable(self):

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
        
        
        response = self.app_tester.get('/api/v1/red-flags/100')
        data =  json.loads(response.data)
        self.assertEqual(data["status"],404)

    def test_patch_location(self):
        
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

        location = {"location": "mutungo"}
        response = self.app_tester.patch("/api/v1/red-flags/1/location" ,json=location)
        data = json.loads(response.data)
        self.assertEqual(data["status"],200)
        self.assertIn(data["data"][0]["message"], "Updated red-flag record's location")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["data"][0]["id"], 1)

    def test_patch_location_in_index_that_is_not_existing(self):
        
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

        location = {"location": "mutungo"}
        response = self.app_tester.patch("/api/v1/red-flags/100/location" ,json=location)
        self.assertEqual(response.status_code, 404)
    

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
       

    def test_delete_record_that_doesnot_exist(self):
       
        response = self.app_tester.delete('/api/v1/red-flags/100')
        self.assertEqual(response.status_code, 404)
       

    
   
    
      
    

    
      