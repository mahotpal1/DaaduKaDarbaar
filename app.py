from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
import request
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq

app = Flask(__name__)

@app.route("/", methods=['GET'])
@cross_origin()
def DaaduKitchen():
    return render_template("style_index.html")

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8001, debug=True)