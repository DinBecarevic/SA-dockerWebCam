import cv2
import base64
import time
import flask
from flask import Flask, jsonify
import threading
import os
import numpy as np

app = Flask(__name__)

# globalna spremenljivka za zadnjo zajeto sliko
last_image = None

def capture_image():
    global last_image
    
    # save to last_image

@app.route('/get_image')
def get_image():
    # return the last image in json

if __name__ == '__main__':
    threading.Thread(target=capture_image, daemon=True).start()
    app.run(host='0.0.0.0', port=5000)