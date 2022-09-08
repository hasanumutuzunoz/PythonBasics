from pymongo import MongoClient
client = MongoClient("localhost",27017)
database = client['mydb']
print("Database Created")
collection = database["product"]
print("Collection created")

#Insert a single product to collection "product"
"""
product1 = {
    "name":"IPhone",
    "price":1000
}
result = collection.insert_one(product1)
print(result.inserted_id)
"""

#Insert many products
products = [{
    "name":"IPhone",
    "price":1000
},{
    "name":"Macbook",
    "price":2000
},{
    "name":"Dell",
    "price":1500
}
]

result = collection.insert_many(products)
print(result.inserted_ids)
