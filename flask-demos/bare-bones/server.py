from flask import Flask

app = Flask(__name__)

# Tells server that whenever a request is received that matches the route
# configuration, the function below will be called to handle that request.
# The return value of the function is evaluated as the response
@app.route("/", methods=["GET"])
def hello_world():
    # Creates a response with the response body "Hello World" and status code 201
    return ("Hello World", 201)

app.run(debug=True)