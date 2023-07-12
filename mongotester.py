# Import pymongo library
import pandas as pd
from pymongo import MongoClient

# Create a MongoClient object with the connection string
client = MongoClient(
    "mongodb+srv://madara:uchiha@cluster0.udl8rnv.mongodb.net/")

db = client.sample_analytics
collection = db.accounts

documents = list(collection.find())

# print(documents)

# invbooks = []

# for i in range(len(documents)):
#     if "InvestmentStock" in list(documents[i].products):
#         invbooks.append(documents[i])

# print(len(invbooks))

df = pd.DataFrame(documents)

df = df.explode("products")

data = df
one_hot = pd.get_dummies(data['products'])
data = data.drop('products', axis=1)
data = data.join(one_hot)

# assuming data is the DataFrame with one-hot encoded columns
data2 = data.groupby('_id').any()  # group by ID and apply the any function

counts = data2.sum()  # get the sum of each column
print(counts)
