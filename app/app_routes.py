"""
Author:Harold
"""

from flask import Flask, jsonify, request, json

from app.models import User, Incident


app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


redflags=[]
count=0

@app.route('/')
def hello_world():
    return 'Hello, welcome to my first api'

@app.route('/api/v1/red-flags', methods=['POST'])
def add_redflag():
    data = request.get_json()
    global count

    try:
        
        count+=1

        redflag = Incident(count,data["createdBy"], data["types"],data["location"],
                            data["status"],data["Images"],data["Videos"],data["comment"])

        redflags.append(redflag.convert_to_dictionary())

        return jsonify({"status": 201,"data":[{"id":redflag.id,"message":"Created red-flag record"}] }) ,201

    except :
        
        return jsonify({"status":400,"message": "Please input text"}),400
    



@app.route('/api/v1/red-flags', methods=['GET'])

def get_all_redflags():
       
    if len(redflags) < 1:
        return jsonify({"status":404,"message":"Resource does not exist" }),404
    return jsonify({"status":200 ,"data": redflags}),200
    
        

        




@app.route('/api/v1/red-flags/<int:id>', methods=['GET'])
def get_specific_redflag(id):

    
    for index in range(len(redflags)):
        if redflags[index]["id"]== id: 
            return jsonify({"status":200,"data":redflags[index] }),200
        elif index == (len(redflags) -1):
            return jsonify({"status":404,"message":"Resource does not exist" }) ,404

    
    if len(redflags) <1:
        return jsonify({"status":404,"message":"Resource does not exist"  }),404    
            
    
    


@app.route('/api/v1/red-flags/<int:id>/<string:key>', methods=['PATCH'])
def update_location(id,key):
    data = request.get_json()
    
 
    if len(redflags) <1:
        return jsonify({"status":404,"message":"Resource does not exist"  }),404
    
    for index in range(len(redflags)):
        if redflags[index]["id"]== id:
            redflags[index][key]=data[key]
            return jsonify({"status":200,"data": [{"id": redflags[index]["id"],"message": "Updated red-flag record's {}".format(key)}] }),200
        elif index == (len(redflags) -1):
            return jsonify({"status":404,"message":"Resource does not exist" }), 404     
    
    
   


@app.route('/api/v1/red-flags/<int:id>', methods=['DELETE'])
def delete__redflag(id):

    if len(redflags) <1:
        return jsonify({"status":404,"message":"Resource does not exist"  }),404    
    

    for index in range(len(redflags)):
        if  redflags[index]["id"]== id: 
            del redflags[redflags.index(redflags[index])]
            return jsonify({"status":200,"data": [{"id":id,"message": "red-flag record has been deleted"}] }),200
        elif index == (len(redflags) -1):
            return jsonify({"status":404,"message":"Resource does not exist" }),404
    
    
       


if __name__ == '__main__':
    app.run(debug=True)
