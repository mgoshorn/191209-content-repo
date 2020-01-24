from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def basic_route():
    """Render the base template"""
    return render_template("index.html")

@app.route("/special")
def special_route():
    """Render an extended version of the base template"""
    return render_template("balloon-animal.html")


app.run(debug=True)