# -*- coding: utf-8 -*-
from flask import Flask
from flask import jsonify
from bson.json_util import dumps
from pymongo import MongoClient
import RPi.GPIO as GPIO

app = Flask(__name__)
                          
# Set up GPIO with output to LED on pin 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

# Set up database access (MongoDB)
dbclient = MongoClient()
db = dbclient.wot
# Get the thing collection
thingscollection = db.thing.find()
# Create JSON-data from collection via a Python list
thingslist = list(thingscollection)
things = dumps(thingslist)

# Helper function to convert Mongo object(s) to JSON
def toJson(data):
    return dumps(data)

@app.route('/pingpong/api/v1.0/things', methods=['GET'])
def get_things():
    return things

@app.route('/pingpong/api/v1.0/things/<name>', methods=['GET'])
def get_thingstatus(name):
    thing = db.thing.find({"name": name })
    if thing.count() <= 0:
        return '{"Error:": "No such name"}'
    return toJson(thing)

@app.route('/pingpong/api/v1.0/things/<name>/<actor>/<value>', methods=['POST'])
def set_thingactor(name, actor, value):
    thing = db.thing.find({"$and": [{"name": name }, {"actors.name": actor}]})
    if thing.count() <= 0:
        return '{"Error:": "No such name"}'
    GPIO.output(18, int(value))
    return '{"Light": ' + value + '}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
