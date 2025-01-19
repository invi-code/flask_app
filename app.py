from flask import Flask
from flask_restx import Api, Resource

# Initialize Flask app
app = Flask(__name__)
api = Api(app, title="Flask-RESTx Example", version="1.0", description="A simple Flask-RESTx API")

# Define a namespace
ns = api.namespace("example", description="Example operations")



@ns.route("/hello")
class HelloWorld(Resource):
    def get(self):
        """Returns a simple greeting"""
        return {"message": "Hello, World!"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
