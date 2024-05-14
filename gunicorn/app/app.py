from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
import os

application = Flask(__name__)

application.config["MONGO_URI"] = 'mongodb://' + os.environ['MONGODB_USERNAME'] + ':' + os.environ['MONGODB_PASSWORD'] + '@' + os.environ['MONGODB_HOSTNAME'] + ':27017/' + os.environ['MONGODB_DATABASE']
db = PyMongo(application).db

#my_db.db.create_collection("test")
#my_db.db.test.insert_one({ "test": "test" })

item_1 = {
    "_id" : "U1IT00001",
    "item_name" : "Blender",
    "max_discount" : "10%",
    "batch_number" : "RR450020FRG",
    "price" : 340,
    "category" : "kitchen appliance"
}

item_2 = {
    "_id" : "U1IT00002",
    "item_name" : "Egg",
    "category" : "food",
    "quantity" : 12,
    "price" : 36,
    "item_description" : "brown country eggs"
}

@application.route('/')
def adfsdf():
    return "test"

@application.route('/queryCollection', methods=['POST'])
def queryCollection():
    pass


@application.route('/getDocument')
def getDocument():
    return jsonify(
        status=True,
        message='Welcome to the Dockerized Flask MongoDB app!'
    )

@application.route('/deleteCollection')
def deleteCollection():
    pass




@application.route('/createDocument', methods=['POST'])
def createTodo():
    data = request.get_json(force=True)
    item = {
        'todo': data['todo']
    }
    db.todo.insert_one(item)

    return jsonify(
        status=True,
        message='To-do saved successfully!'
    ), 201