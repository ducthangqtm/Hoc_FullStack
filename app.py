from flask import Flask, render_template
import os
import platform
import json
from datetime import datetime

app = Flask(__name__)

def check_ping(ip):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    # Gửi 1 gói tin, timeout 1 giây cho nhanh
    response = os.system(f"ping {param} 1 -w 1000 {ip} > nul")
    return "Online" if response == 0 else "Offline"

@app.route('/')
def index():
    # 1. Đọc danh sách thiết bị từ file JSON
    with open('devices.json', 'r', encoding='utf-8') as f:
        device_list = json.load(f)

    # 2. Kiểm tra trạng thái từng thiết bị
    servers = []
    for device in device_list:
        status = check_ping(device['ip'])
        servers.append({
            "name": device['name'],
            "ip": device['ip'],
            "status": status
        })

    # 3. Lấy thời gian hiện tại
    now = datetime.now().strftime("%H:%M:%S - %d/%m/%Y")
    
    return render_template('index.html', servers=servers, update_time=now)
from flask import jsonify
@app.route('/api/ping/<ip>')
def api_ping(ip):
    status = check_ping(ip)
    return jsonify({"ip": ip, "status": status, "time": datetime.now().strftime("%H:%M:%S")})
if __name__ == '__main__':
    app.run(debug=True, port=5000)