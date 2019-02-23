# importing required packages
from pymongo import MongoClient
import pprint

# making a connection
client = MongoClient()
client = MongoClient('localhost', 27017)

# list down the databases
print(client.list_database_names())
print('*'*40)

# creating our collection instance
db = client.my_first_database
coll = db.my_first_collection

# list down the collections
print(db.collection_names(include_system_collections = False))
print('*'*40)

# print all the documents inside 'coll'
# in ascending/ descending order of 'name' attribute
query_1 = coll.find().sort('author', 1)
query_2 = coll.find().sort('id', -1)
for doc in query_2:
    pprint.pprint(doc)