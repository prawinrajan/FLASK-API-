import json
from flask import Flask, Response, abort
from .utils import JSON_MIME_TYPE, sensor_details

app = Flask(__name__)

sensor_data=[{
     "HomeId":1 ,
    "time":13,
    "temperature":38,
    "Humidity":13,
    "ultrasonic_motion_sensor":1,
        "IR":1
}]

@app.route('/sensor_data')
def sensor():
    response = Response(json.dumps(sensor_data),status=200, mimetype=JSON_MIME_TYPE)
    return response


@app.route('/sensor_data/<int:HomeId>')
def sensor_detail(HomeId):
    sd= sensor_details(sensor_data,HomeId)
    if sd is None:
        abort(404)

    content = json.dumps(sd)
    return content, 200, {'Content-Type': JSON_MIME_TYPE}


@app.errorhandler(404)
def not_found(e):
    return '', 404
