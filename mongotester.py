import pymongo

# Connect to the MongoDB server
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Get the database and the collection
db = client["test"]
books = db["books"]

# Query the collection for books with genre "fantasy"
query = {"genre": "fantasy"}
results = books.find(query)

# Print the results
for book in results:
    print(book)
