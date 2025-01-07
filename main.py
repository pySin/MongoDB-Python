# Start with Python to MongoDB connection
from pymongo import MongoClient
from bson import ObjectId

# client = MongoClient("localhost", 27017)
client = MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000")

db = client.bookstore
books = db.books

# books.insert_one({"title": "Big Mamma", "author": "Sammy Some", "rating": 4, "genres":
#                   ["Drama", "Thriller"]})
# books.insert_one({"title": "Small Mamma", "author": "Grande Cheritos", "rating": 6, "genres":
#                  ["Comedy"]})

carla_id = books.insert_one({"title": "New Mamma", "author": "Carla Sveda", "rating": 7, "genres":
                            ["Musical"]}).inserted_id

# for book in books.find():
#     print(f"Book: {book}")
#
# print(f"ID just inserted: {carla_id}")

# print([b for b in books.find({"author": "Dante", "copies.go": {"$in": [1, 2, 3]}})])
# print(*books.find({"author": "Kristo"}))
# print([b for b in books.find({"_id": ObjectId('645fcad776c659ebddbdd80d')})])

print([b for b in books.find({"gender": {"$gt": 1}})])
