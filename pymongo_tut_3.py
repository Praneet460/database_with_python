# importing required packages
from pymongo import MongoClient
import pprint

# creating a connection
client = MongoClient()
client = MongoClient('localhost', 27017)

# list out databases
db_list = client.list_database_names()
print(db_list)
print('-'*30)

# create our collection instance
db = client.my_first_database
coll = db.my_first_collection

# listing all the collections in our database
coll_list = db.collection_names(include_system_collections = False)
print(coll_list)
print('-'*30)

# print first document 
# stored inside the 'my_first_collection'
pprint.pprint(coll.find_one())
print('-'*30)

# print all the documents stored 
# inside the 'my_first_collection'
for doc in coll.find():
    pprint.pprint(doc)
print('-'*30)

# print a specific query from the 
# 'my_first_collection' created
pprint.pprint(coll.find_one({"author": "Alex"}))
print('-'*30)

# quering using 'regex' function
for doc in coll.find({"author": {"$regex": "^S"}}):
    pprint.pprint(doc)


