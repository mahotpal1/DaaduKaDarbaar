from flask import Flask, render_template, request, jsonify
from urllib.request import urlopen as uReq

app = Flask(__name__)

@app.route("/", methods=['GET'])
@cross_origin()
def DaaduKitchen():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)