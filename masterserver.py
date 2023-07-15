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

schemavar = """{
        productId: {
            type: 'Number',
            required: true,
            unique: true
        },
        listedOn: {
            type: 'Number',
            required: true
        },
        listingType: {
            type: 'String',
            required: true
        },
        productType: {
            type: 'String',
            required: true
        },
        quantity: {
            type: 'Number',
            required: true
        },
        status: {
            type: 'String',
            required: true
        },
        sellerDetails: {
            userId: {
                type: 'Number',
                required: true
            },
            name: {
                type: 'String',
                required: true
            },
            profilePic: {
                type: 'String',
                required: true
            },
            city: {
                type: 'String',
                required: true
            },
            role: {
                type: 'String',
                required: true
            },
            verified: {
                type: 'Number',
                required: true
            },
            location: {
                pincode: {
                    type: 'String',
                    required: true
                },
                pickupAddressId: {
                    type: 'Number',
                    required: true
                },
                addressLocation: {
                    latitude: {
                        type: 'String'
                    },
                    longitude: {
                        type: 'String'
                    }
                }
            }
        },
        category: {
            categoryString: {
                type: 'String',
                required: true
            },
            categoryName: {
                type: 'String',
                required: true
            },
            categoryId: {
                type: 'Number',
                required: true
            },
            categoryIdString: {
                type: 'String',
                required: true
            },
        },
        collections: {
            type: [
                'String'
            ],
            required: true
        },
        details: {
            title: {
                type: 'String',
                required: true
            },
            description: {
                type: 'String',
                required: true
            },
            condition: {
                type: 'String',
                required: true
            },
            brand: {
                type: 'String',
                required: true
            },
            variantAttribute: {
                type: 'String',
                required: true
            },
            productAttributes: {
                type: [
                    'Mixed'
                ],
                required: true
            },
            variants: {
                type: [
                    'Mixed'
                ],
                required: true
            }
        },
        images: {
            submittedImages: {
                type: [
                    'String'
                ],
                required: true
            },
            thumbImages: {
                type: [
                    'String'
                ],
                required: true
            },
            mainImages: {
                type: [
                    'String'
                ],
                required: true
            }
        },
        filters: {},
        activeRank: {
            type: 'Number',
            required: true
        },
        baseProduct: {
            type: 'Number',
            required: true
        },
        productLogs: {
            type: [
                'Mixed'
            ],
            required: true
        },
        promoted: {
            type: 'Number'
        },
        promotionDetails: {
            impressions: {
                type: 'Number'
            },
            views: {
                type: 'Number',
            },
        }
    }"""

conversation_history = [
    str("You are a helpful assistant that specializes in creating queries for databases. If what the user asks is related to querying a database, return the query in MongoDB, otherwise simply return Please ask a relevant question. The database is called sample_analytics and the collection is called customers. The schema of customers is " +
        schemavar)
]

# Import the mysql-connector-python module

# Create a connection object
mydb = mysql.connector.connect(
    host="localhost",
    user="root"
)


@app.route("/ask", methods=["POST"])
@cross_origin()
def ask():
    global conversation_history
    question = request.json["question"]
    prompt = PromptTemplate(
        template=" ".join(conversation_history) + "\nQ: {question}\n A: ",
        input_variables=["question"],
    )

    llm_chain = LLMChain(prompt=prompt, llm=llm)
    response = llm_chain.run(question)
    return jsonify({"response": response.replace("\n", "")})


@app.route("/query", methods=["POST"])
@cross_origin()
def query():

    qry = request.json["query"]
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
