import argparse
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


def read_all_cats():
    """Read all cat records from the collection."""
    cats = collection.find()
    for cat in cats:
        print(cat)


def read_cat_by_name(name):
    """Read a cat record by name."""
    cat = collection.find_one({"name": name})
    if cat:
        print(cat)
    else:
        print("Cat not found!")


def update_cat_age(name, new_age):
    """Update the age of a cat by name."""
    collection.update_one({"name": name}, {"$set": {"age": new_age}})
    print("Cat age updated successfully!")


def add_feature_to_cat(name, new_feature):
    """Add a new feature to a cat by name."""
    collection.update_one({"name": name}, {"$push": {"features": new_feature}})
    print("New feature added to the cat!")


def delete_cat_by_name(name):
    """Delete a cat record by name."""
    collection.delete_one({"name": name})
    print("Cat deleted successfully!")


def delete_all_cats():
    """Delete all cat records from the collection."""
    collection.delete_many({})
    print("All cats deleted successfully!")


def main():
    try:
        parser = argparse.ArgumentParser(description="CRUD operations on cats")
        parser.add_argument(
            "operation",
            choices=[
                "read_all",
                "read",
                "update",
                "add_feature",
                "delete",
                "delete_all"
            ],
            help="Operation to perform"
        )
        parser.add_argument("--name", help="Name of the cat")
        parser.add_argument("--age", type=int, help="New age of the cat")
        parser.add_argument("--feature", help="New feature to add to the cat")

        args = parser.parse_args()

        match args.operation:
            case "read_all":
                read_all_cats()
            case "read":
                read_cat_by_name(args.name)
            case "update":
                update_cat_age(args.name, args.age)
            case "add_feature":
                add_feature_to_cat(args.name, args.feature)
            case "delete":
                delete_cat_by_name(args.name)
            case "delete_all":
                delete_all_cats()
            case _:
                print("Invalid operation. Please specify a valid operation.")
    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    main()
