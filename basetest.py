from flask import Flask, request, jsonify
import langchain
from langchain.llms import OpenAI
from langchain import PromptTemplate, LLMChain
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"

llm = OpenAI(openai_api_key="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")
conversation_history = [
    "You are a helpful assistant that specializes in creating queries for databases. If what the user asks is related to querying a database, return the query in both MongoDB and SQL, otherwise simply return Please ask a relevant question"
]


@app.route("/ask", methods=["POST"])
@cross_origin()
def ask():
    global conversation_history
    question = request.json["question"]
    prompt = PromptTemplate(
        template="\n".join(conversation_history) + "\nQ: {question}\n A: ",
        input_variables=["question"],
    )

    llm_chain = LLMChain(prompt=prompt, llm=llm)
    response = llm_chain.run(question)
    conversation_history.append(f"Q: {question}\nA: {response}")

    return jsonify({"response": response})


@app.route("/ask_nc", methods=["POST"])
@cross_origin()
def ask_nc():
    question = request.json["question"]
    prompt = PromptTemplate(
        template="\nQ: {question}\n A: ",
        input_variables=["question"],
    )

    llm_chain = LLMChain(prompt=prompt, llm=llm)
    response = llm_chain.run(question)

    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
