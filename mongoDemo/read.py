from pymongo import MongoClient
client = MongoClient("localhost", 27017)
database = client["mydb"]
collection = database["product"]
#print(collection.find_one())             #Find the first one
"""cursor = collection.find()             #Find all
for eac_doc in cursor:
    print(eac_doc)"""
cursor = collection.find({"name":"Dell"}) #Find only Dell
for eac_doc in cursor:
    print(eac_doc)

