"""
Author:MukuruH
"""



from flask import Flask, jsonify, request, json
from flask.views import MethodView

from app.models.incident_model import  Incident
from app.models.user_model import  User


redflags=[]
count=0

class IncidentMap(MethodView):



    def get(self, id):

        if id is None:
            if len(redflags) < 1:
                return jsonify({"status":404,"message":"Resource does not exist" }),404
            return jsonify({"status":200 ,"data": redflags}),200
    
        else:
            for index in range(len(redflags)):
                if redflags[index]["id"]== id: 
                    return jsonify({"status":200,"data":redflags[index] }),200
                elif index == (len(redflags) -1):
                    return jsonify({"status":404,"message":"Resource does not exist" }) ,404

    
            if len(redflags) <1:
                return jsonify({"status":404,"message":"Resource does not exist"  }),404    
            
    
    def post(self):
        data = request.get_json()
        global count

        try:
            validate = Incident.validate_data(data["createdBy"])
            print(validate)
            if validate == True: 

                count+=1  
                redflag = Incident(count,data["createdBy"], data["types"],location=data["location"],
                                    Images=data["Images"],Videos=data["Videos"],comment=data["comment"])
                redflags.append(redflag.inident_information())
                return jsonify({"status": 201,"data":[{"id":redflag.id,"message":"Created red-flag record"}] }) ,201

            else:
                return jsonify({"status":400,"message": "Please input text"}),400


        except :       
            return jsonify({"status":400,"message": "Please input text"}),400

    def delete(self,id):
        if len(redflags) <1:
            return jsonify({"status":404,"message":"Resource does not exist"  }),404    
    

        for index in range(len(redflags)):
            if  redflags[index]["id"]== id: 
                del redflags[redflags.index(redflags[index])]
                return jsonify({"status":200,"data": [{"id":id,"message": "red-flag record has been deleted"}] }),200
            elif index == (len(redflags) -1):
                return jsonify({"status":404,"message":"Resource does not exist" }),404



    def patch(self, id, key):
        data = request.get_json()
    
 
        if len(redflags) <1:
            return jsonify({"status":404,"message":"Resource does not exist"  }),404
        
        for index in range(len(redflags)):
            if redflags[index]["id"]== id:
                redflags[index][key]=data[key]
                return jsonify({"status":200,"data": [{"id": redflags[index]["id"],"message": "Updated red-flag record's {}".format(key)}] }),200
            elif index == (len(redflags) -1):
                return jsonify({"status":404,"message":"Resource does not exist" }), 404     
        