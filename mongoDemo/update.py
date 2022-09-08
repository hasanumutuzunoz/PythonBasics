"""
() brackets
[] square brackets
{} curly bracket
, comma
. dot
: colon
; semicolon
"" quotation mark
'' single quotation mark
"""

from pymongo import MongoClient
client = MongoClient("localhost", 27017)
database = client["mydb"]
collection = database["product"]

filter = {"name": "IPhone"}
result = collection.update_many(filter, {"$set":{"price":5555}})
print(result.modified_count)

cursor = collection.find({"name":"IPhone"})
for eac_doc in cursor:
    print(eac_doc)