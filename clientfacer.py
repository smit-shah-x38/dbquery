import mysql.connector
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

# Create a connection object
mydb = mysql.connector.connect(
    host="localhost",
    user="root"
)

# Create a cursor object
mycursor = mydb.cursor()

# Execute a query to create a database
mycursor.execute("CREATE DATABASE IF NOT EXISTS exampledb")

# Execute a query to use the database
mycursor.execute("USE exampledb")


def ask(question):
    question = "You are a helpful assistant that specializes in creating queries for databases. Your queries will run on a table called customers with the schema customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255)). Now answer the question: " + str(
        question) + " if it relates to the subject matter of sql queries and return the query, else return Please ask a relevant question."

    response = llm(question)
    response = response.replace("\n", "")

    print("Original response: " + str(response))

    return response


def exec(query):

    mycursor.execute(str(query))

    res = mycursor.fetchall()

    return res


def query(qry):

    myresult = exec(qry)

    print(myresult)

    return myresult


def validate(sql):
    # Parse the query
    sql_query = sqlvalidator.parse(sql)

    # Check if the query is valid
    if sql_query.is_valid():
        return True
    else:
        return False


@app.route("/respond/sql", methods=["POST"])
@cross_origin()
def resp():

    question = request.json["question"]
    response = ask(question=question)

    if validate(response):
        result = query(response)
        return jsonify({"Success": str(result)})
    else:
        return jsonify({"Error": "Internal", "Response": str(response)})


@app.route("/respond/close", methods=["POST"])
@cross_origin()
def respond():

    # Close the cursor and connection objects
    mycursor.close()
    mydb.close()

    return "closed"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
