# import mysql.connector
from flask import Flask, request, jsonify
import langchain
from langchain.llms import OpenAI
from langchain import PromptTemplate, LLMChain
from flask_cors import CORS, cross_origin
import sqlvalidator

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"

llm = OpenAI(
    openai_api_key="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")

# # Create a connection object
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root"
# )

# # Create a cursor object
# mycursor = mydb.cursor()

# # Execute a query to create a database
# mycursor.execute("CREATE DATABASE IF NOT EXISTS exampledb")

# # Execute a query to use the database
# mycursor.execute("USE exampledb")


# def ask(question, tablename, schema):
#     question = "You are a helpful assistant that specializes in creating queries for databases. Your queries will run on a table called " + tablename + " with the schema " + schema + ". Now answer the question: " + str(
#         question) + " if it relates to the subject matter of interacting with a database and return only the query in a runnable format to perform the action requested, else return Please ask a relevant question."

#     response = llm(question)
#     response = response.replace("\n", "")

#     print("Original response: " + str(response))

#     return response


def askmongo(question, tablename, schema):
    question = "You are a helpful assistant that specializes in creating queries for MongoDB databases. Your queries will run on a table called " + tablename + " with the schema " + schema + ". Now answer the question: " + str(
        question) + " if it relates to the subject matter of interacting with a database and return only the Mongo query in a runnable format to perform the action requested."

    response = llm(question)
    response = response.replace("\n", "")

    print("Original response: " + str(response))

    return response


# def exec(query):

#     mycursor.execute(str(query))

#     res = mycursor.fetchall()

#     return res


# def query(qry):

#     myresult = exec(qry)

#     print(myresult)

#     return myresult


# def validate(sql):
#     # Parse the query
#     sql_query = sqlvalidator.parse(sql)

#     # Check if the query is valid
#     if sql_query.is_valid():
#         return True
#     else:
#         return False


# @app.route("/respond/sql", methods=["POST"])
# @cross_origin()
# def resp():

#     question = request.json["question"]
#     tablename = request.json["tablename"]
#     schema = request.json["schema"]
#     response = ask(question=question, tablename=tablename, schema=schema)

#     if validate(response):
#         result = query(response)
#         return jsonify({"Success": str(result)})
#     else:
#         return jsonify({"Error": "Internal", "Response": str(response)})


@app.route("/respond/mongo", methods=["POST"])
@cross_origin()
def responder():

    question = request.form["question"]
    tablename = request.form["tablename"]
    schema = str(request.form["schema"])
    response = askmongo(question=question, tablename=tablename, schema=schema)

    if response:
        return jsonify({"Success": str(response)})
    else:
        return jsonify({"Error": "Internal", "Response": str(response)})


# @app.route("/respond/close", methods=["POST"])
# @cross_origin()
# def respond():

#     # Close the cursor and connection objects
#     mycursor.close()
#     mydb.close()

#     return "closed"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
