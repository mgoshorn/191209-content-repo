from flask import Flask
from flask import url_for
from flask import render_template

app = Flask(__name__)

# When a GET request is sent to the context "/"
# render the template file index.html as the
# response. NOTE: templates must be in a
# 'templates' folder.
@app.route("/index.html", methods=["GET"])
@app.route("/", methods=["GET"])
@app.route("/<name>", methods=["GET"])
def say_hello(name = None):
    if not name:
        name = "User"

    return render_template("index.html", name=name)

app.run(debug=True)

