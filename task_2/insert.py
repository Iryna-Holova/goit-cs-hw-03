from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
MONGO_SERVER_API = os.getenv("MONGO_SERVER_API")

client = MongoClient(MONGO_URI, server_api=ServerApi(MONGO_SERVER_API))

db = client.cats
collection = db.cats_collection

cats = [
    {
        "name": "Barsik",
        "age": 3,
        "features": ["walks in slippers", "likes to be petted", "red"]
    },
    {
        "name": "Whiskers",
        "age": 2,
        "features": ["sleeps a lot", "loves tuna", "gray"]
    },
    {
        "name": "Mittens",
        "age": 5,
        "features": ["hunts birds", "enjoys sunbathing", "black and white"]
    },
    {
        "name": "Snowball",
        "age": 4,
        "features": ["loves playing", "chases laser pointer", "white"]
    }
]

collection.insert_many(cats)
