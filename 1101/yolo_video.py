from flask import Flask, render_template, request, jsonify
from ultralytics import YOLO
import os
from werkzeug.utils import secure_filename
import cv2
import base64
import re
import numpy as np


app = Flask(__name__)
model = YOLO("yolov8n.pt")

@app.route("/")
def index():
    return render_template("yolo_video.html")

@app.route("/analyze_frame", methods=['POST'])
def analyze_frame():
    try:
        data_url = request.form['image']
        image_data = re.sub('data:image/.+;base64,','',data_url)
        image = np.frombuffer(base64.b64decode(image_data), np.uint8)
        frame = cv2.imdecode(image, cv2.IMREAD_COLOR)
        frame = cv2.resize(frame, (320, 320))
        results = model(frame)
        annotated_frame = results[0].plot(show=False)
        _, buffer = cv2.imencode('.jpg', annotated_frame)
        result_image = base64.b64encode(buffer).decode('utf-8')
        result_url = 'data:image/jpeg;base64,' + result_image
        return jsonify({'result_image' : result_url})
    except Exception as e:
        print(f'err:{e}')
        return jsonify({'error':'failed to process image'}, 500)


if __name__ == '__main__':
    app.run(debug=True,  host="0.0.0.0")
    # app.run(debug=True, ssl_context="adhoc", host="0.0.0.0")
