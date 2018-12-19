"""
Author:Harold
"""

from flask import Flask, jsonify, request, json

from app.models import User, Incident

app = Flask(__name__)

users = []
redflags=[]
interventions=[]


@app.route('/api/v1/redflags', methods=['GET'])

def get_all_redflags():

    json_redflags = []
    #print(redflags)
    
    for item in redflags:
        json_redflags.append(item.convert_dictionary())

    print(json_redflags)
    print(len(json_redflags))
    if len(json_redflags) < 1:
        return jsonify({"status":200,"message": "There is nothing to output"})
    return jsonify({"status":200 ,"red-flags": json_redflags})


@app.route('/api/v1/redflags', methods=['POST'])
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
        return jsonify({"message": "Please input text"}), 400
    return jsonify({"status": 201,"redflags": [redflag.convert_dictionary()]}) 



    @app.route('/api/v1/redflags', methods=['PATCH'])
    def add_redflag():
        pass



if __name__ == '__main__':
    app.run(debug=True)
