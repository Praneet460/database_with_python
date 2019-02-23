# importing requied packages
from pymongo import MongoClient

# making a connection
client = MongoClient()
client = MongoClient('localhost', 27017)

# creating a database
db = client.my_first_database

# creating a collection
collection = db.my_first_collection

# creating document
post = [
    {
        "id": 1,
        "author": "Mike",
        "location": "USA"
    },
    {
        "id": 2,
        "author": "Suneet",
        "location": "India"
    },
    {
        "id": 3,
        "author": "Alex",
        "location": "Texas"
    }
]

# inserting a document inside collection
posts = collection.insert_many(post)

# print created database
print(client.list_database_names())