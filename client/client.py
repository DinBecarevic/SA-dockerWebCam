import requests
from flask import Flask, render_template, jsonify
import time
import os

app = Flask(__name__)


@app.route('/')
def index():
    # show html

@app.route('/get_current_image')
def get_current_image():
    #return current image

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)