from pymongo import MongoClient
client = MongoClient("localhost", 27017)
database = client["mydb"]
collection = database["product"]

filter = {"name":"IPhone"}
collection.delete_many(filter)

cursor = collection.find()
for eac_doc in cursor:
    print(eac_doc)