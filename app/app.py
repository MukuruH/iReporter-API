"""
Author:Harold
"""

from flask import Flask, jsonify, request, json

from app.models import User, Incident

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

users = []
redflags=[]
interventions=[]


@app.route('/api/v1/red-flags', methods=['GET'])

def get_all_redflags():
       
    if len(redflags) < 1:
        return jsonify({"status":200,"message": "Resource does not exist"})
    return jsonify({"status":200 ,"data": redflags})


@app.route('/api/v1/red-flags', methods=['POST'])
def add_redflag():
    data = request.get_json()
    print(data)

    try:
       
        redflag = Incident(data["createdBy"], data["types"],data["location"],
                            data["status"],data["Images"],data["Videos"],data["comment"])

        redflags.append(redflag.convert_to_dictionary())
    except ValueError as e:
        print(e)
        return jsonify({"status":400,"message": "Please input text"}),
    return jsonify({"status": 201,"data":[{"id":redflag.id,"message":"Created red-flag record"}] }) 




@app.route('/api/v1/red-flags/<int:id>', methods=['GET'])
def get_specific_redflag(id):

    if len(redflags) <1:
        return jsonify({"status":204,"message":"Resource does not exist" })      
    
    for index in range(len(redflags)):
        if redflags[index]["id"]== id:
            return jsonify({"status":200,"data":redflags[index] })
        elif index == (len(redflags) -1):
            return jsonify({"status":404,"message":"Resource does not exist" })      
    
    


@app.route('/api/v1/red-flags/<int:id>/<string:key>', methods=['PATCH'])
def update_location(id,key):
    data = request.get_json()
    print(data)
 
    if len(redflags) <1:
        return jsonify({"status":204,"message":"Resource does not exist" })      
    
    for index in range(len(redflags)):
        if redflags[index]["id"]== id:
            redflags[index][key]=data[key]
            return jsonify({"status":200,"data": [{"id": redflags[index]["id"],"message": "Updated red-flag record's {}".format(key)}] })
        elif index == (len(redflags) -1):
            return jsonify({"status":404,"message":"Resource does not exist" })      
    
    
   


@app.route('/api/v1/red-flags/<int:id>', methods=['DELETE'])
def delete__redflag(id):
    data = request.get_json()
    print(data)

    for index in range(len(redflags)):
        if  redflags[index]["id"]== id: 
            del redflags[redflags.index(redflags[index])]
            return jsonify({"status":200,"data": [{"id":id,"message": "red-flag record has been deleted"}] })
        elif index == (len(redflags) -1):
            return jsonify({"status":404,"message":"Resource does not exist" })      
    
    
       


if __name__ == '__main__':
    app.run(debug=True)
