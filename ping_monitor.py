import os
import platform

def check_ping(hostname):
    # Xác định tham số lệnh ping tùy theo hệ điều hành (Windows là -n, Linux là -c)
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    
    # Thực hiện lệnh ping (chỉ gửi 1 gói tin để chạy cho nhanh)
    command = f"ping {param} 1 {hostname}"
    response = os.system(command)

    if response == 0:
        print(f"[OK] {hostname} is UP")
    else:
        print(f"[ERROR] {hostname} is DOWN")

# Danh sách IP Server của bạn trên Web
list_server = ["172.168.1.1", "172.16.1.14"]

print("--- ĐANG KIỂM TRA HỆ THỐNG NETWORK ---")
for ip in list_server:
    check_ping(ip)