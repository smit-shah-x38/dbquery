# import mysql.connector
from flask import Flask, request, jsonify
import langchain
from langchain.llms import OpenAI
from langchain import PromptTemplate, LLMChain
from flask_cors import CORS, cross_origin
# from flask_sqlalchemy import SQLAlchemy
# from graphene import ObjectType, String, Schema
# from graphene import graphql_sync

from ariadne import QueryType, graphql_sync, make_executable_schema

# from api import app, db
# from api import models

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"


type_defs = """
type Query {
  hello(name: String = "world"): String!
}
"""
query = QueryType()


@query.field("hello")
def resolve_hello(_, info, name):
    return f"Hello, {name}!"


schema = make_executable_schema(type_defs, query)

# app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://asaedtrl:hkc5KYSYHHyEr82eW_lwTPk5WSf8vfME@john.db.elephantsql.com/asaedtrl"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# db = SQLAlchemy(app)


# class Query(ObjectType):
#     hello = String(name=String(default_value="stranger"))

#     def resolve_hello(self, info, name):
#         return f"Hello {name}"


# @app.route("/graphql", methods=["POST"])
# @cross_origin()
# def graphql():
#     # Get the query from the request body
#     data = request.get_json()
#     # Execute the query using the schema
#     success, result = graphql_sync(schema, data)
#     # Set the status code depending on the success
#     status_code = 200 if success else 400
#     # Return the result as JSON
#     return jsonify(result), status_code

@app.route("/graphql", methods=["POST"])
@cross_origin()
def graphql_server():
    # Get the query from the request body
    data = request.get_json()
    schema = make_executable_schema(type_defs, query)
    # Execute the query using the schema
    success, result = graphql_sync(schema, data)
    # Set the status code depending on the success
    status_code = 200 if success else 400
    # Return the result as JSON
    return jsonify(result), status_code


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
