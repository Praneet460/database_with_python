# import required packages
from pymongo import MongoClient
import pprint

# making a connection
client = MongoClient()
client = MongoClient('localhost', 27017)

# list down the databases
print(client.list_database_names())
print('#'*40)

# create a reference to a database
db = client.my_first_database

# list down the collections we have inside the 'db' database
print(db.collection_names(include_system_collections=False))
print('#'*40)

# create a reference to a collection
coll = db.my_first_collection

# print all the documents inside our 'coll'
for doc in coll.find():
    pprint.pprint(doc)
print('#'*40)

# deleting a single document from our collection
query_1 = coll.delete_one({'author': 'Suneet'})
for doc in coll.find():
    pprint.pprint(doc)
print('#'*40)

# updating a single document in our collection
query2 = coll.update_one({"author": "Alex"}, {"$set": {"author": "Sam"}})
for doc in coll.find():
    pprint.pprint(doc)
print('#'*40)

# set the limit function in the 'coll'
for doc in coll.find().limit(3):
    pprint.pprint(doc)

# delete the collections from our database
coll.drop()

# check if there is still any collection left
print(len(db.collection_names(include_system_collections=False)))
print('#'*40)

# check the database present
print(client.list_database_names())
print('#'*40)

# delete the database
client.drop_database('my_first_database')

# recheck the database exist
print(client.list_database_names())