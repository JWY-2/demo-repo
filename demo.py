###########################################################
# Project Name: Simple API endpoint
# Purpose: Demo for interview
# Author: Jiawei Yao
# Date: August 28, 2023
###########################################################

import json

import os

import sys

from flask import Flask, request, jsonify

###########################################################
#  Flask-related config params
###########################################################
app = Flask(__name__)
counter = 0
args = sys.argv

###########################################################
#  Welcome Page
###########################################################
@app.route("/")
def welcome():
    return "Welcome to demo!"


###########################################################
#  Use `Post` method to upload file and get fileId generated
###########################################################
@app.route("/file", methods=["POST"])
def rest_post():
    try:
        my_json = request.get_json()
        json_obj = json.dumps(my_json)

        global counter
        temp = counter + 1
        counter = temp

        with open(f"file_{temp}.json", "w") as f:
            f.write(json_obj)
        f.close()
        return jsonify(fileId=temp)
    except Exception as e:
        return e


###########################################################
#  Use `Get` method to retrieve any file based on fileIds
###########################################################
@app.route("/file/<int:file_id>", methods=["GET"])
def rest_get(file_id):
    try:
        if not os.path.exists(f"file_{file_id}.json"):
            return "No such file."
        else:
            data = ""
            with open(f"file_{file_id}.json", "r") as f:
                data = json.load(f)
            f.close()
            return data["data"]
    except Exception as e:
        print(e)
        return e


###########################################################
#  API Version
###########################################################
@app.route("/version", methods=["GET"])
def version():
    try:
        global args
        return jsonify(version=args[1])
    except Exception as e:
        print(e)
        return "Wrong Arguments"


###########################################################
#  Run API server
###########################################################
app.run(host='0.0.0.0', port='5000')
