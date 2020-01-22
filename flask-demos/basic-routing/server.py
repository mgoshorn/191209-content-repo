from flask import Flask

app = Flask(__name__)

cats = ["Felix", "Fluffy", "Max", "Sylvester", "Tom", "Garfield"]

@app.route("/cats", methods=["GET"])
def get_cats():
    return {
        "data": cats
    }

@app.route("/cats/<id>")
def get_cat(id):
    if(not id.isnumeric()):
        return "", 404

    int_id = int(id)

    if(int_id < 1 or int_id > len(cats)):
        return "", 404

    cat = cats[int_id-1]
    return cat, 200


app.run(debug=True)