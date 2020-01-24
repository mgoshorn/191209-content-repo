from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def landing_page():
    return render_template("index.html")

@app.route("/hello", methods=["GET"])
def say_hello():
    name = request.args["name"]
    color = request.args["color"]
    print(name, color)
    return render_template("response.html", name=name, color=color)

app.run(debug=True)