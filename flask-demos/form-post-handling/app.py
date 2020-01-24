from flask import Flask, render_template, request

app = Flask(__name__)

users = {
    "Abby": "abby1234",
    "Billy": "billy777",
    "Cindy": "cindy000"
}


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    if username not in users.keys():
        return render_template("login-error.html"), 401

    if password == users[username]:
        return render_template("success.html", username=username)

    return render_template("login-error.html"), 401

app.run(debug=True)