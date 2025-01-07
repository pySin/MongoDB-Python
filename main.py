# Start with Python to MongoDB connection
from pymongo import MongoClient

# client = MongoClient("localhost", 27017)
client = MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000")

db = client.bookstore
books = db.books

for book in books.find():
    print(f"Book: {book}")

