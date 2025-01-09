# Start with Python to MongoDB connection
from pymongo import MongoClient
from bson import ObjectId
from bson.son import SON

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

# print([b for b in books.find({"gender": {"$gt": 1}})])
# print([b for b in books.find({"gender": {"$gt": 1}})])
# print(books.count_documents({"gender": {"$gt": 1}}))

# books.update_one({"_id": ObjectId("6460300076c659ebddbdd81c")}, {"$set": {"name": "Sophia_2"}})
# books.delete_many({"_id": {"$in": [ObjectId("6460300076c659ebddbdd830"),
#                                   ObjectId("6460300076c659ebddbdd832")]}})

pipeline = [
    {
        "$group": {
            # "_id": "$name",
            "_id": "$location",  # Divide the results by location groups. Grouped by what?
            "averageGender": {"$avg": "$gender"}  # The aggregation itself
        }
    }

    # {
        # "$sort": SON([("averageGender", -1), ("_id", -1)])
    #     "$sort": SON([("averageGender", -1)])
    # }
]

results = books.aggregate(pipeline)

# for result in results:
#     print(f"Result: {result}")
print(*results)

books.update_one(
    {"title": "Super Store"},
    {"$set": {"author": "Kristo the Second"}}
)

print("Record updated!")

# --

pipeline_2 = [
    {
        "$match": {
            "id": {"$gt": 3046}
        }
    },
    {
        "$group": {
            "_id": "null",  # Divide the results by location groups. Grouped by what?
            "averageGender": {"$avg": "$gender"}  # The aggregation itself
        }
    }
]

results_2 = books.aggregate(pipeline_2)
print(results_2)
print(*results_2)

db_3 = client.Bookstore_12_2024
books_3 = db_3.books

pipeline_3 = [
    {
        "$match": { # Match documents where Pages are grater than 200
            "Pages": {"$gt": 200}
        }
    },
    {
        "$group": {
            "_id": "$Author", # Get the average rating per author for the matching results.
            "avgRating": {"$avg": "$rating"}
        }
    }
]

results_3 = books_3.aggregate(pipeline_3)
[print(r) for r in results_3]

