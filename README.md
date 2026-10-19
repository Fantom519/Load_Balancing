# ⚖️ NT533 - High-Availability Load Balancing System

[![Docker](https://img.shields.io/badge/Containerization-Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![HAProxy](https://img.shields.io/badge/Load%20Balancer-HAProxy-00A88F?style=for-the-badge&logo=haproxy&logoColor=white)](https://www.haproxy.org/)
[![Python](https://img.shields.io/badge/Backend-Python%20Flask-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://flask.palletsprojects.com/)
[![Ubuntu](https://img.shields.io/badge/OS-Ubuntu%20WSL2-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)](https://ubuntu.com/)
[![Architecture](https://img.shields.io/badge/Architecture-Distributed%20System-blueviolet?style=for-the-badge)](https://github.com/Fantom519/Load_Balancing)

Hệ thống **Cân bằng tải (Load Balancing)** và **Chịu lỗi (Fault Tolerance)** cho ứng dụng Web phân tán. Dự án được đóng gói hoàn chỉnh bằng **Docker Compose**, sử dụng **HAProxy 2.4** làm thuật toán điều phối luồng và cụm **Python Flask** làm Web Backend Services.

---

## 🛠️ Công nghệ & Kỹ năng sử dụng

### Hạ tầng & Điều phối (Infrastructure & Orchestration)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Docker Compose](https://img.shields.io/badge/Docker%20Compose-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![HAProxy](https://img.shields.io/badge/HAProxy-00A88F?style=for-the-badge&logo=haproxy&logoColor=white)
![WSL2](https://img.shields.io/badge/Linux_WSL2-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)

### Backend, Giám sát & Bắn tải (Backend, Monitoring & Testing)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=prometheus&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white)
![k6](https://img.shields.io/badge/k6-7D4646?style=for-the-badge&logo=k6&logoColor=white)

---

## 📌 Tính năng cốt lõi (Core Features)

- [x] **Dynamic Traffic Distribution**: Điều phối request linh hoạt giữa 3 backend node sử dụng các thuật toán `Round Robin`, `Least Connections`, và `Weighted`.
- [x] **Active Health Checking**: HAProxy tự động gửi nhịp tim (heartbeat) kiểm tra trạng thái backend mỗi 2000ms (`inter 2000ms fall 2 rise 2`).
- [x] **Zero-Downtime Failover**: Tự động phát hiện và ngắt node bị sự cố out-of-service mà không gây gián đoạn cho người dùng cuối.
- [x] **Dual-Network Isolation**: Phân vùng mạng an toàn giữa `frontend-net` (tiếp nhận request public) và `backend-net` (mạng nội bộ kín).
- [x] **Real-time Monitoring Dashboard**: Màn hình quản trị trực quan hiển thị số liệu Throughput, Latency, Active Sessions tại cổng `8404`.

---

## 🏗️ Kiến trúc Hệ thống (System Architecture)

```
                       [ Client / Browser ]
                                |
                   (Port 8080)  |  (Port 8404)
                                v
                      +-------------------+
                      |   frontend-net    |
                      +---------+---------+
                                |
                                v
                     +---------------------+
                     |  HAProxy LoadBal    | <--- Stats Dashboard
                     +----------+----------+
                                |
                      +---------+---------+
                      |    backend-net    |
                      +----+----+----+----+
                           |    |    |
           +---------------+    |    +---------------+
           |                    |                    |
           v                    v                    v
  +-----------------+  +-----------------+  +-----------------+
  |  Flask Backend  |  |  Flask Backend  |  |  Flask Backend  |
  |     Node 1      |  |     Node 2      |  |     Node 3      |
  |   (Port 5000)   |  |   (Port 5000)   |  |   (Port 5000)   |
  +-----------------+  +-----------------+  +-----------------+
```

---

## 📂 Cấu trúc Thư mục Dự án

```
load_balancing_project/
├── backend/
│   ├── app.py              # Flask REST API (Endpoints: /ping, /heavy)
│   ├── Dockerfile          # Containerization cho Python 3.9 Alpine
│   └── requirements.txt    # Thư viện Flask dependencies
├── haproxy/
│   └── haproxy.cfg         # Cấu hình HAProxy (Algorithms, Health Check, Stats)
├── docker-compose.yml      # Orchestration file phân vùng Dual-Network
└── README.md               # Tài liệu dự án
```

---

## 🚀 Hướng dẫn Cài đặt & Triển khai (1-Click Deployment)

### Yêu cầu Hệ thống (Prerequisites)
* **Docker Desktop** (đã bật WSL 2 Backend trên Windows).
* **Git** Command Line.

### Các bước thực hiện

1. **Clone Repository:**
   ```bash
   git clone https://github.com/Fantom519/Load_Balancing.git
   cd Load_Balancing
   ```

2. **Khởi chạy toàn bộ cụm Container:**
   ```bash
   docker compose up -d --build
   ```

3. **Kiểm tra trạng thái các Container:**
   ```bash
   docker compose ps
   ```

---

## 🌐 Danh sách Endpoint & Dashboard

| Dịch vụ | Đường dẫn (URL) | Mô tả Chi tiết |
| :--- | :--- | :--- |
| **API Ping Test** | `http://localhost:8080/ping` | Test thuật toán Round Robin (Phản hồi JSON ngẫu nhiên từ Node 1, 2, 3) |
| **API Heavy Test** | `http://localhost:8080/heavy` | Giả lập tác vụ nặng (Delay 0.5s - 1.5s) để test thuật toán Least Connections |
| **HAProxy Dashboard** | `http://localhost:8404/stats` | Trang quản trị Realtime hiển thị chỉ số sức khỏe của từng Backend Node |

---

## 👥 Phân công Vai trò Nhóm (NT533)

* 👑 **Trưởng nhóm (System & Architecture Lead)**: Thiết kế kiến trúc tổng thể, viết `docker-compose.yml`, cấu hình phân vùng mạng `networks`, cấu hình HAProxy Baseline và giải quyết xung đột hạ tầng.
* 💻 **Backend Developer**: Viết ứng dụng Flask REST API, đóng gói Dockerfile backend nhẹ và xây dựng các endpoint giả lập tải.
* 📊 **Observability & Test Engineer**: Xây dựng kịch bản k6/Locust bắn tải và cấu hình bộ giám sát Prometheus & Grafana.
* 📝 **Data Analyst & Reporter**: Thu thập log, tính toán độ công bằng Jain's Fairness Index, hoàn thiện file báo cáo Word và làm video demo.