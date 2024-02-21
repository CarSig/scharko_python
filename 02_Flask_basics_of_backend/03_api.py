# what is API?
# API is a set of rules that allows one software application to communicate with another.

# what is REST API?
# REST API is a set of rules that allows one software application to communicate with another. It is a stateless architecture that runs on HTTP. It is a standard way of building web services that uses HTTP methods such as GET, POST, PUT, DELETE, etc. to perform operations on the data.

# what is the use of Flask in API?
# Flask is a micro web framework for building web applications. It is used to build web services and web APIs. It provides tools, libraries, and technologies to build web applications and web APIs.

# what is the use of jsonify() in Flask?
# The jsonify() function is used to convert a Python dictionary to a JSON response. It is used to return JSON responses from the server.

# example of calling an API using Flask

from flask import Flask, jsonify,request
import requests

app = Flask(__name__)

baseUrl = 'https://jsonplaceholder.typicode.com'

@app.route("/api", methods=["GET"])
def api():
    data = {"name": "John", "age": 25}
    return jsonify(data)

#  get all users from the API
@app.route("/users", methods=["GET"])
def users():
    
    response = requests.get(f"{baseUrl}/users")
    return response.json()

#  get a user by id from the API   
@app.route("/user/<int:id>", methods=["GET"])
def user(id):
    response = requests.get(f"{baseUrl}/users/{id}")
    return response.json()



if __name__ == "__main__":
    app.run()
