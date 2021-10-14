# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 17:11:14 2021

@author: samridhamla
"""
from flask import Flask, request, jsonify
from liveTraffic import *
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/api")
@cross_origin()
def index():
    print("Brooo")
    myUrl =  request.args.get("url")
    myUrl = "https://www.youtube.com/watch?v=" + str(myUrl);
    #myUrl = "vDHtypVwbHQ"
    output = processVideo(myUrl) 
    #output["url"]  = myUrl
    #response.headers.add("Access-Control-Allow-Origin", "*")
    json_string = json.dumps(output)
    print(json_string)
    return json_string


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)