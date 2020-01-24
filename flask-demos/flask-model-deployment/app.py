from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def inference():
    if not request.files["img"]:
        return "No image uploaded"

    file = request.files["img"]
    bytes = file.read()
    return bytes
    




app.run(debug=True)