
# 🛡️ DAW GUARD

DAW GUARD is a web-based network traffic analysis platform built with Python and Flask. Users upload CSV data to view, filter, and analyze packets by protocol, IP, or service. It transforms raw network data into clear, useful insights.

---

## 🗺️ Overview

DAW GUARD is a **single-page web application** that runs locally using a Flask server.

- Upload a CSV file of network traffic
- Instantly view packet table, statistics, and logs
- No database or cloud required
- No JavaScript frameworks used

The app follows a simple **client-server model**:
- Flask handles backend logic and routing
- Jinja2 renders dynamic HTML
- Filters work via request-response cycle

---

## ✨ Key Features

- 📤 **CSV Upload** – Load network traffic data instantly  
- 📊 **Packet Table** – View packet details (IP, protocol, ports, size, etc.)  
- 🔍 **Multi-Field Filtering** – Filter by protocol, IP, or service  
- 🔄 **Port-to-Service Mapping** – Converts ports (80 → HTTP, 443 → HTTPS, etc.)  
- 📈 **Statistics Panel** – Packet counts, averages, unique IPs  
- 🧾 **Log Records** – Terminal-style packet logs  
- ❌ **Clear Filters** – Reset dataset instantly  
- 📑 **Sidebar Navigation** – Clean UI structure  
- 📱 **Responsive Design** – Works on different screen sizes  
- 🎨 **Dark Theme UI** – Black + neon orange cybersecurity style  

---

## 🧰 Tech Stack

| Layer              | Technology        | Purpose                          |
|-------------------|------------------|----------------------------------|
| Language          | Python 3.7+      | Backend logic                   |
| Framework         | Flask            | Server & routing                |
| Data Processing   | Pandas           | CSV handling & filtering        |
| Templating        | Jinja2           | Dynamic HTML rendering          |
| Frontend          | HTML5, CSS3      | UI layout & styling             |
| Utilities         | Werkzeug         | Secure file handling            |

---

## 🗂️ Project Structure

```

network-monitor/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── data/
└── sample_traffic.csv

````

---

## 🖥️ Screenshots

### Dashboard
<img width="1920" height="897" alt="image" src="https://github.com/user-attachments/assets/0361f091-db65-4d9e-9523-94b43b6ea2f5" />


### Filters Applied
!<img width="1894" height="840" alt="image" src="https://github.com/user-attachments/assets/a8fc66da-3e43-4d09-aeac-f8aa998be5f6" />


### Statistics & Logs
<img width="1686" height="863" alt="image" src="https://github.com/user-attachments/assets/17a46553-7508-4c0f-94cf-319965ba1950" />


---

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.7+
- pip
- Browser (Chrome, Firefox, Edge)

### Steps

```bash
git clone https://github.com/your-username/network-monitor.git
cd network-monitor
pip install -r requirements.txt
python app.py
````

Open in browser:

```
http://127.0.0.1:5000
```

---

## 📋 How to Use

1. Start the Flask server
2. Open browser at `127.0.0.1:5000`
3. Upload a CSV file
4. View packet table, stats, and logs
5. Apply filters:

   * Protocol (TCP / UDP / ICMP)
   * Source IP
   * Destination IP
   * Service
6. Click **Apply Filters**
7. Click **Clear** to reset

---

## 📊 Dataset Format

Required CSV columns:

| Column         | Description         |
| -------------- | ------------------- |
| Time           | Packet timestamp    |
| Source IP      | Sender IP           |
| Destination IP | Receiver IP         |
| Protocol       | TCP / UDP / ICMP    |
| Size           | Packet size (bytes) |
| Source Port    | Sender port         |
| Dest Port      | Receiver port       |

⚠️ Service column is auto-generated from destination port

---

## 🗃️ Sample Data

Included file: `data/sample_traffic.csv`

* 300 packets
* Protocols: TCP, UDP, ICMP
* Ports: 21, 22, 53, 80, 443, 3306
* Packet size: 64–1500 bytes

---

## 🌐 API Routes

| Route         | Method | Description    |
| ------------- | ------ | -------------- |
| `/`           | GET    | Main dashboard |
| `/api/upload` | POST   | Upload CSV     |
| `/api/filter` | GET    | Apply filters  |

---

## 🎓 Learning Outcomes

* Network packet structure
* TCP vs UDP vs ICMP
* Port-to-service mapping
* Flask web development
* Data processing with Pandas
* Jinja2 templating
* UI design with HTML & CSS


## 👤 Author

**Muhammad Dawood**
Student ID: BCSF24M030
Department: Computer Science
Course: Computer Networks

---

## 📄 License

MIT License – Free for educational use


