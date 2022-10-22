import json
from os import listdir, path

from flask import Flask, abort, jsonify, request, send_file
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return "Hello world!"

@app.route("/sample_dataframe", methods=['GET'])
def sample_dataframe():
    data = {
        "question": "Does the image portrait a cat?",
        "data":  "/data"
    }
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route("/data/images", methods = ["GET"])
def get_image():
    args = request.args
    if(args["image_name"] and path.isfile(f"./Project/images/{args['image_name']}")):
        p = f"./images/{args['image_name']}"
        return send_file(p)
    abort(404, description="Image not found")

def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()
