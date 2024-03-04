import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

### Create database
db = client["example_database"]
customers = db["customers"]
items = db["items"]

# create mongo documents
customers_data = [{ "firstname": "Bob", "lastname": "Adams" },
                  { "firstname": "Amy", "lastname": "Smith" },
                  { "firstname": "Rob", "lastname": "Bennet" },]
items_data = [{ "title": "USB", "price": 10.2 },
              { "title": "Mouse", "price": 12.23 },
              { "title": "Monitor", "price": 199.99 },]

customers.insert_many(customers_data)
items.insert_many(items_data)


# add "boughtitems" to the customer where the firstname is Bob
bob = customers.update_many(
        {"firstname": "Bob"},
        {
            "$set": {
                "boughtitems": [
                    {
                        "title": "USB",
                        "price": 10.2,
                        "currency": "EUR",
                        "notes": "Customer wants it delivered via FedEx",
                        "original_item_id": 1
                    }
                ]
            },
        }
    )

# add "boughtitems" to the customer where the firstname is Amy
amy = customers.update_many(
        {"firstname": "Amy"},
        {
            "$set": {
                "boughtitems":[
                    {
                        "title": "Monitor",
                        "price": 199.99,
                        "original_item_id": 3,
                        "discounted": False
                    }
                ]
            } ,
        }
    )

# perform queries, to start- can create an index (optional but speeds up queries):
customers.create_index([("name", pymongo.DESCENDING)])

# retrieve the customer names sorted in ascending order:
items = customers.find().sort("name", pymongo.ASCENDING)

#loop over
for item in items:
    print(item.get('boughtitems'))

#get list of unique names
customers.distinct("firstname")

for i in customers.find({"$or": [{'firstname':'Bob'}, {'firstname':'Amy'}]},
                                 {'firstname':1, 'boughtitems':1, '_id':0}):
    print(i)