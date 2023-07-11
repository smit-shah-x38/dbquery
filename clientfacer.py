import mysql.connector
from flask import Flask, request, jsonify
import langchain
from langchain.llms import OpenAI
from langchain import PromptTemplate, LLMChain
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"

llm = OpenAI(
    openai_api_key="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")
conversation_history = [
    "You are a helpful assistant that specializes in creating queries for databases. If what the user asks is related to querying a database, return the query in SQL, otherwise simply return Please ask a relevant question"
]

# Create a connection object
mydb = mysql.connector.connect(
    host="localhost",
    user="root"
)


def ask(question):
    global conversation_history
    question = str(question)
    prompt = PromptTemplate(
        template="\n".join(conversation_history) + "\nQ: {question}\n A: ",
        input_variables=["question"],
    )

    llm_chain = LLMChain(prompt=prompt, llm=llm)
    response = llm_chain.run(question)
    conversation_history.append(f"Q: {question}\nA: {response}")

    response = response.replace("\n", "")

    return response


def query(query):
    # Create a cursor object
    mycursor = mydb.cursor()

    # Execute a query to create a database
    mycursor.execute("CREATE DATABASE IF NOT EXISTS exampledb")

    # Execute a query to use the database
    mycursor.execute("USE exampledb")

    # Execute a query to select all data
    mycursor.execute(str(qry))

    # Fetch all the rows from the result set
    myresult = mycursor.fetchall()

    # Close the cursor and connection objects
    mycursor.close()
    mydb.close()

    return jsonify({"response": myresult})


@app.route("/respond/sql", methods=["POST"])
@cross_origin()
def resp():

    question = request.json["question"]
    response = ask(question=question)

    # if response.contains("relevant"):
    #     return jsonify({"Error": response})

    return jsonify({"Success": response})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
