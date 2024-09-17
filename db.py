
import os
from pymongo import MongoClient

# Set up the MongoDB client
client = MongoClient(os.environ["MONGODB_URI"])
db = client[os.environ["MONGODB_NAME"]]

# Define the collection for storing chat data
chat_collection = db["chats"]

# Define functions for inserting and retrieving chat data
def insert_chat(chat_id, data):
    chat_collection.update_one({"_id": chat_id}, {"$set": data}, upsert=True)

def get_chat(chat_id):
    return chat_collection.find_one({"_id": chat_id})

