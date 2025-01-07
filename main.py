# Start with Python to MongoDB connection
from pymongo import MongoClient

client = MongoClient("localhost", 27017)
db = client.bookstore
books = db.books

for book in books.find():
    print(f"Book: {book}")

