from pymongo import MongoClient
from flask import Flask, jsonify, request 
client = MongoClient('mongodb://localhost:27017/')
db = client.school
student = db.student_name
# db.mycollection.createIndex( { "name": 1 }, { unique: true })
 
app = Flask(__name__)
@app.route('/create', methods=['POST'])
def create():
    try:
        request.json['student_name']
    except KeyError as e:
        return 'invalid request'
    try:
        student.insert_one({
            "student_name": request.json['student_name'],
            "id": request.json['id'],
            "role_number" : request.json['role_number']
        })
        return jsonify({ "respcode": 200,
                        "process_time_ms": "",
                        "result":"success"
                        } )
    except Exception as e:
        return 'infamation not curect'
    
@app.route('/read', methods=['GET'])
def read():
    cursor = student.find({})
    data = []
    for x in cursor:
        data.append({
            "student_name" : x['student_name'],
            "id" : x['id'],
            "role_number" : x['role_number']
        })
    return jsonify({"data":data})

@app.route('/update', methods = ['POST'])
def update():
    myquery = {"student_name":request.json['student_name']}
    newvalues = {"$set": {"student_name":request.json['new_student_name']}}
    student.update_one(myquery, newvalues)
    return jsonify({})

@app.route('/delete', methods = ['POST'])
def delete():
    myquery = {"student_name" : request.json['student_name']}
    student.delete_one(myquery)
    return jsonify({})

if __name__ == '__main__':
    app.run(debug = True)