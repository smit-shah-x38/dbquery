# Import pymongo library
from pymongo import MongoClient

# Create a MongoClient object with the connection string
client = MongoClient(
    "mongodb+srv://madara:uchiha@cluster0.udl8rnv.mongodb.net/")

db = client.sample_analytics
collection = db.accounts

documents = list(collection.find())

print(len(documents))
print(documents[0])

# invbooks = []

# for i in range(len(documents)):
#     if "InvestmentStock" in list(documents[i].products):
#         invbooks.append(documents[i])

# print(len(invbooks))
