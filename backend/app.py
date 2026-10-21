from flask import Flask, jsonify
import time
import random
import os

app = Flask(__name__)

# Lấy ID của server từ biến môi trường
SERVER_ID = os.getenv("SERVER_ID", "Node_Unknown")

@app.route('/ping', methods=['GET'])
def ping():
    """Endpoint phản hồi tức thì để test Round Robin và Weighted."""
    return jsonify({
        "server": SERVER_ID, 
        "status": "success", 
        "message": "Pong!"
    })

@app.route('/heavy', methods=['GET'])
def heavy_task():
    """Endpoint giả lập tính toán nặng để ép tải Least Connections."""
    delay = random.uniform(0.5, 1.5)
    time.sleep(delay)
    return jsonify({
        "server": SERVER_ID, 
        "status": "success", 
        "delay_seconds": round(delay, 2),
        "message": "Heavy task completed"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)