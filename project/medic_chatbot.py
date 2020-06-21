from adapt.intent import IntentBuilder
from adapt.engine import IntentDeterminationEngine
from werkzeug.serving import run_simple
from flask import Flask
from flask import request
from flask_cors import CORS
import requests
from flask import make_response, jsonify
import json
from core import *

#Application with CORS to reduce network security isssues
app = Flask(__name__)
CORS(app)

#To communicate with frontend in json type
def json_response(response):
    """Used to format to jason data type"""
    response_obj = {"result":response,"status":"success"}
    resp = make_response(json.dumps(response_obj,indent=4))
    return resp
    
#decorator to receive inputs from frontend
@app.route('/chatbot', methods=['GET','POST'])
def chat_print():
    """this functions receives data from front end and process it"""
    msg = request.args.get('msg','')
    previous_msg = request.args.get('previous_msg','')
    print("I am connected and working..." + msg)
    res = "returned..."
    #return json_response({"resp":res})
    #main program to do all processing
    data = process(msg,previous_msg)
    resp = make_response(jsonify(data), 201)
    #print(resp)
    return resp


if __name__ == "__main__":
    #app.debug = True
    #run_simple('0.0.0.0',7777,app)
    #local host ip for development 
    app.run(host="0.0.0.0",port=7777)
