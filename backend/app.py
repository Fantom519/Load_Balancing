from flask import Flask
import os
import time
import random

app = Flask(__name__)

# Lấy tên node từ biến môi trường Docker
node_name = os.environ.get("NODE_NAME", "Unknown_Node")

@app.route('/ping')
def ping():
    # Endpoint nhẹ: Xử lý tức thì (dùng test Round Robin / Weighted)
    return {
        "status": "success",
        "node": node_name,
        "message": f"Hello from {node_name}"
    }

@app.route('/heavy')
def heavy():
    # Endpoint nặng: Giả lập thời gian xử lý ngẫu nhiên từ 0.5s - 1.5s (dùng test Least Connections)
    delay = random.uniform(0.5, 1.5)
    time.sleep(delay)
    return {
        "status": "success",
        "node": node_name,
        "delay_sec": round(delay, 2)
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)