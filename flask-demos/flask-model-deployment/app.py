from flask import Flask, render_template, request
from model_init import init, preprocess_img, value_mapper

import tensorflow as tf
import base64

model = init("2020-01-09-model")
sig = model.signatures["serving_default"]

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def inference():
    if not request.files["img"]:
        return "No image uploaded"

    for item in request.form:
        print(item)

    # Load image from multipart upload and get bytes
    file = request.files["img"]
    content_type = file.content_type
    bytes = file.read()

    # Convert raw bytes to a tensor
    img = tf.image.decode_image(bytes, channels=1)
    img = preprocess_img(img)
    result = model(img)

    mapping = value_mapper(result)
    b64_string = base64.b64encode(bytes)

    b64_data = "data:" + content_type + ";base64," + str(b64_string)[2:-1]

    return render_template("result.html", result=mapping, img_b64=b64_data)

# app.run(debug=True)