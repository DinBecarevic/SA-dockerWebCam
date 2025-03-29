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
    
    while True:
        try:
            cap = cv2.VideoCapture(0)
            time.sleep(1)
            ret, frame = cap.read()
            
            if ret:
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                cv2.putText(frame, timestamp, (10, 30), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                
                # pretvori sliko v base64
                _, buffer = cv2.imencode('.jpg', frame)
                last_image = base64.b64encode(buffer).decode('utf-8')
                print(f"Slika zajeta ob {timestamp}")
            else:
                print("Napaka pri zajemu slike")
                
            cap.release()
            
        except Exception as e:
            print(f"Napaka: {str(e)}")
            
        time.sleep(10)

@app.route('/get_image')
def get_image():
    if last_image:
        return jsonify({'image': last_image})
    return jsonify({'image': None})

if __name__ == '__main__':
    threading.Thread(target=capture_image, daemon=True).start()
    
    app.run(host='0.0.0.0', port=5000)