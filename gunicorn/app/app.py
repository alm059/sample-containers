from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
import os

application = Flask(__name__)

application.config["MONGO_URI"] = 'mongodb://' + os.environ['MONGODB_USERNAME'] + ':' + os.environ['MONGODB_PASSWORD'] + '@' + os.environ['MONGODB_HOSTNAME'] + ':27017/' + os.environ['MONGODB_DATABASE']
chat_db = PyMongo(application).db

if "users" not in chat_db.list_collection_names():
    chat_db.create_collection("users")

if "conversations" not in chat_db.list_collection_names():
    chat_db.create_collection("conversations")

users = chat_db.users
conversations =  chat_db.conversations


@application.route('/', methods=['GET'])
def index():
    return jsonify(status=True, message="""
        /createUser: create a new user document
        /authUser: verify if a user exists
        /getConversations: get conversations a user has created
        /getContactList: get options to create conversations with 
        /getMessages: get all (or newer) messages of a conversation (find_one_or_404)
        /sendMessage: send a message to a conversation
        /patchMessage: edit or delete message
    """), 201

@application.route('/createUser', methods=['POST'])
def createUser():
    create_user_required_fields = {"username"}
    if not create_user_required_fields.issubset(set(request.form.keys())):
        return jsonify(
        status=400,
        message="Username field required")
    
    if users.find_one({"username": request.form.get("username")}) != None:
        return jsonify(
        status=400,
        message="User already exists")

    return jsonify(
        status=201,
        response=str(users.insert_one(request.form.to_dict())),
        message="User has been created")

@application.route('/authUser', methods=['POST'])
def authUser():
    user = users.find_one({"username": request.form.get("username")})
    if user != None:
        return jsonify(
        status=201,
        response=str(user),
        message="User exists")
    else:
        return jsonify(
        status=400,
        message="Could not find user")

@application.route('/getContactList', methods=['GET'])
def getContactList():
    user_list = users.find()
    list_in_string = "[" + ", ".join([str(element) for element in users.find()]) + "]"
    return jsonify(
        status=201,
        response=list_in_string,
        message="Retrieving user list")

@application.route('/getConversations', methods=['GET'])
def getConversations():
    if request.args["username"] == None:
        return jsonify(
        status=400,
        message="A username is needed to get their conversations")

    user_query = {"participants": request.args["username"]}

    conversations.find()
    return books.find("")



@application.route('/getMessages', methods=['POST', 'PUT', 'PATCH'])
def getMessages():
    pass


@application.route('/sendMessage', methods=['POST', 'DELETE'])
def sendMessage():
    pass

@application.route('/patchMessage', methods=['POST', 'DELETE'])
def patchMessage():
    pass