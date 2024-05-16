from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
import os

application = Flask(__name__)

application.config["MONGO_URI"] = 'mongodb://' + os.environ['MONGODB_USERNAME'] + ':' + os.environ['MONGODB_PASSWORD'] + '@' + os.environ['MONGODB_HOSTNAME'] + ':27017/' + os.environ['MONGODB_DATABASE']
books_db = PyMongo(application).db

if "books" not in books_db.list_collection_names():
    books_db.create_collection("books")

books = books_db.books

required_fields = {"title", "author", "published_year","genre", "do_i_have_it"}

book_1 = {
    "title": "",
    "author": "",
    "published_year": "",
    "genre": "",
    "do_i_have_it": ""
}

@application.route('/', methods=['GET']))
def index():
    return jsonify(status=True, message="""
        /createBook 
        /getBooks
        /getBook
        /updateBook
        /deleteBook
    """), 201

@application.route('/createBook', methods=['POST'])
def createBook():
    if not required_fields.issubset(set(request.form.keys())):
        return "error"
    
    return " ".join([element for element in request.form.keys()])

@application.route('/getBooks', methods=['GET'])
def getBooksList():
    return books.find("")

@application.route('/getBook', methods=['GET']))
def getBookInfo():
    return jsonify(
        status=True,
        message='Welcome to the Dockerized Flask MongoDB app!'
    )

@application.route('/updateBook', methods=['POST', 'PUT', 'PATCH'])
def updateBook():
    pass


@application.route('/deleteBook', methods=['POST', 'DELETE'])
def deleteBook():
    pass