import requests
from flask import Flask, render_template, jsonify
import time
import os

app = Flask(__name__)

SERVER_URL = 'http://server:5000/get_image' # server je ime Docker vsebnika, ki se razreši v pravilen IP naslov v Docker omrežju

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_current_image')
def get_current_image():
    try:
        response = requests.get(SERVER_URL)
        data = response.json()
        return jsonify(data)
    except Exception as e:
        print(f"Error getting image: {str(e)}")
        return jsonify({'error': str(e), 'image': None})

if __name__ == '__main__':
    print("Počakam, da bo strežnik na voljo...")
    time.sleep(5)
    
    app.run(host='0.0.0.0', port=5000)