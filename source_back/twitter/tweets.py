from flask import Blueprint
from pymongo import MongoClient
import json

tweets = Blueprint('tweets', __name__)

@tweets.route('/tweets')
def home():
    client = MongoClient('mongodb://localhost:27017/')

    db = client['twitter']
    collection = db['twitter']

    documents = collection.find({})

    tweets = []

    for document in documents:
        tweets.append(document)

    res = json.dumps(tweets)
    return res