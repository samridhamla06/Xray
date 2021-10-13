# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 17:11:14 2021

@author: samridhamla
"""
from flask import Flask, request, jsonify
from liveTraffic import *
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/hello")
@cross_origin()
def index():
    print("Brooo")
    #myUrl =  request.args.get("url")
    #myUrl = "https://www.youtube.com/watch?v=" + myUrl;
    myUrl = "vDHtypVwbHQ"
    #output = processVideo(myUrl) 
    #output["url"]  = myUrl
    mydict = {}
    mydict["1"] = "car"
    mydict["2"] = "person"
    response = jsonify(mydict)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


if __name__ == "__main__":
    #app.run(host="127.0.0.1", port=8080, debug=True)
    app.run(host="0.0.0.0", port=5000, debug=True)