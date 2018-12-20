"""
Author:Harold
"""

from flask import Flask, jsonify, request, json

from models import User, Incident

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

users = []
redflags=[]
interventions=[]


@app.route('/api/v1/red-flags', methods=['GET'])

def get_all_redflags():

    json_redflags = []
    #print(redflags)
    
    for item in redflags:
        json_redflags.append(item.convert_to_dictionary())

    print(json_redflags)
    print(len(json_redflags))
    if len(json_redflags) < 1:
        return jsonify({"status":200,"message": "There is nothing to output"})
    return jsonify({"status":200 ,"red-flags": json_redflags})


@app.route('/api/v1/red-flags', methods=['POST'])
def add_redflag():
    data = request.get_json()
    print(data)

    try:
        # print(data)
        # if type(data['types']) is not str:
        #     raise ValueError('Please input text')
        redflag = Incident(data["createdBy"], data["types"],data["location"],
                            data["status"],data["Images"],data["Videos"],data["comment"])

        redflags.append(redflag)
    except ValueError as e:
        print(e)
        return jsonify({"status":400,"message": "Please input text"}),
    return jsonify({"status": 201,"redflags": [redflag.convert_to_dictionary()]}) 




@app.route('/api/v1/red-flags/<int:id>', methods=['GET'])

def get_specific_redflag(id):

    json_redflags = []
            #print(redflags)
    for item in redflags:
        json_redflags.append(item.convert_to_dictionary())

    for index in json_redflags:
        if index["id"]== id :
            return jsonify({"status":200,"data":index })
        else:
            return jsonify({"status":404,"message":"Resource does not exist" })       
            

            
    

    


@app.route('/api/v1/red-flags/<int:id>/location', methods=['PATCH'])
def edit_redflag(id, location):

    json_redflags = []
            #print(redflags)
    for item in redflags:
        json_redflags.append(item.convert_to_dictionary())

    for index in json_redflags:
        if index["id"]== id :
            print(index.get('location'))
            index['location'] = location
            print(index.get('location'))
    return dea




if __name__ == '__main__':
    app.run(debug=True)
