import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["rptutorials"] #rptutorials is a db name

tutorial1 = {
    "title": "Working With JSON Data in Python",
    "author": "Lucas",
    "contributors": [
        "Aldren",
        "Dan",
        "Joanna"
    ],
    "url": "https://realpython.com/python-json/"
}

tutorial = db.tutorial # tutorial is a instance of Collection and represents a physical collection of documents in db


result = tutorial.insert_one(tutorial1)

print(f"One tutorial: {result.inserted_id}")

tutorial2 = {
    "title": "Python's Requests Library (Guide)",
    "author": "Alex",
    "contributors": [
        "Aldren",
        "Brad",
        "Joanna"
    ],
    "url": "https://realpython.com/python-requests/"
}

tutorial3 = {
    "title": "Object-Oriented Programming (OOP) in Python 3",
    "author": "David",
    "contributors": [
        "Aldren",
        "Joanna",
        "Jacob"
    ],
    "url": "https://realpython.com/python3-object-oriented-programming/"
}

new_result = tutorial.insert_many([tutorial2, tutorial3])

print(f"Multiple tutorials: {new_result.inserted_ids}")