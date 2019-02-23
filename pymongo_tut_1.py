# importing required packages
from pymongo import MongoClient

# making a connection
client = MongoClient()
client = MongoClient('localhost', 27017)
print(client.list_database_names())