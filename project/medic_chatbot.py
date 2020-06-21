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

app = Flask(__name__)
CORS(app)

def json_response(response):
    response_obj = {"result":response,"status":"success"}
    resp = make_response(json.dumps(response_obj,indent=4))
    return resp
    

@app.route('/')
@app.route('/chatbot', methods=['GET','POST'])
def chat_print():
    msg = request.args.get('msg','')
    previous_msg = request.args.get('previous_msg','')
    print("I am connected and working..." + msg)
    res = "returned..."
    #return json_response({"resp":res})
    data = process(msg,previous_msg)
    resp = make_response(jsonify(data), 201)
    #print(resp)
    return resp


if __name__ == "__main__":
    #app.debug = True
    #run_simple('0.0.0.0',7777,app)
    app.run(host="0.0.0.0",port=7777)
