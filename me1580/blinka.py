# -*- coding: utf-8 -*-
from flask import Flask
import RPi.GPIO as GPIO, signal, sys, requests 

# Set up signal handler to shut down gracefully
def signal_handler(signal, frame):
        print('Shutting down...')
        GPIO.cleanup()
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

# Initialize Flask app
app = Flask(__name__)
                          
# Set up GPIO with output to LED on pin 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

@app.route('/pingpong/light1/on', methods=['GET'])
def light1_on():
    GPIO.output(18, 1)
    return "Tände lampan"

@app.route('/pingpong/light1/off', methods=['GET'])
def light1_off():
    GPIO.output(18, 0)
    return "Släckte lampan"
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True)
