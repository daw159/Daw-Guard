# Daw-Guard
DAW GUARD is a web-based network traffic analysis platform built with Python and Flask. Users upload CSV data to view, filter, and analyze packets by protocol, IP, or service. With clear stats, readable logs, and a clean interface, it transforms raw network data into useful insights.

________________________________________
🗺️ Overview
DAW GUARD is a single-page web application that runs locally on your machine via a Python Flask server. You load it in your browser, upload a CSV file of network traffic data, and the entire dashboard populates instantly — packet table, statistics, logs, and service labels all rendered together. There is no database, no cloud dependency, and no JavaScript framework. Everything is handled server-side using Flask and Jinja2 templating, keeping the architecture simple and easy to understand.
The application follows a clean client-server model. The Flask backend exposes routes for uploading data, applying filters, and serving the rendered HTML page. The frontend is a single index.html file that uses Jinja2 template variables to display whatever data Flask passes to it. Filters are submitted as HTML forms, the backend processes them, and the page re-renders with updated results — a straightforward request-response cycle that clearly demonstrates core web and networking concepts.
________________________________________
✨ Key Features
•	CSV Upload — Upload any properly formatted network traffic CSV file and load all packet data into the dashboard instantly
•	Live Packet Table — View packets with Time, Source IP, Destination IP, Protocol, Packet Size, Source Port, Destination Port, and Service columns
•	Multi-Field Filtering — Filter simultaneously by Protocol (TCP / UDP / ICMP), Source IP, Destination IP, and Service name
•	Auto Port-to-Service Mapping — Destination ports are automatically converted to service names (Port 80 → HTTP, Port 443 → HTTPS, Port 53 → DNS, Port 22 → SSH, Port 21 → FTP, Port 3306 → MySQL)
•	Statistics Panel — Real-time summary showing Total Packets, TCP Count, UDP Count, ICMP Count, Average Packet Size, Unique Source IPs, and Unique Destination IPs
•	Log Records — Auto-generated terminal-style log entries from packet data
•	Clear Filters — One-click reset to restore the full unfiltered packet view
•	Sidebar Navigation — Clean left sidebar with Dashboard link and system status indicator
•	Responsive Design — Layout adapts across different screen and window sizes
•	Black + Neon Orange UI — Professional cybersecurity-style dark theme throughout
________________________________________
🧰 Tech Stack
Layer	Technology	Purpose
Language	Python 3.7+	Core backend logic
Web Framework	Flask 3.0	Server, routing, request handling
Data Processing	Pandas 2.x	CSV reading, filtering, aggregation
Templating	Jinja2 (built into Flask)	Dynamic HTML rendering
Frontend Structure	HTML5	Single-page interface layout
Frontend Styling	CSS3	Black + neon orange dark theme
Cross-Origin	Flask-CORS	Frontend-backend communication
Utilities	Werkzeug	Secure file upload handling
________________________________________
🗂️ Project Structure
network-monitor/
│
├── app.py                    ← Flask backend — routes, CSV processing, filtering, stats
├── requirements.txt          ← All Python package dependencies
├── README.md                 ← Project documentation
├── .gitignore                ← Git ignore rules
│
├── templates/
│   └── index.html            ← Main single-page UI with Jinja2 template variables
│
├── static/
│   └── style.css             ← Full black + neon orange CSS theme
│
└── data/
    └── sample_traffic.csv    ← Sample dataset with 300 network packets
________________________________________
🖥️ Screenshots
Main Dashboard — After CSV Upload
<img width="1920" height="897" alt="image" src="https://github.com/user-attachments/assets/99a9bd27-8cb3-4bec-a22e-3393078ced92" />


 
Filters Applied — TCP Protocol
<img width="1894" height="840" alt="image" src="https://github.com/user-attachments/assets/1ec737f2-1ef7-499f-9992-81d9055e66ae" />




 
Statistics Panel and Log Records
<img width="1686" height="863" alt="image" src="https://github.com/user-attachments/assets/d7e63634-01d9-4c8a-8657-72bdd74fe227" />



 

________________________________________
⚙️ Installation & Setup
Prerequisites
•	Python 3.7 or higher
•	pip (Python package manager)
•	A modern web browser (Chrome, Firefox, Edge)
Step 1 — Clone the Repository
git clone https://github.com/your-username/network-monitor.git
cd network-monitor
Step 2 — Install Dependencies
pip install -r requirements.txt
Step 3 — Run the Application
python app.py
Step 4 — Open in Browser
http://127.0.0.1:5000
No build tools, no environment configuration, and no database setup required.
________________________________________
📋 How to Use
1.	Open http://127.0.0.1:5000 in your browser after starting the Flask server
2.	Click the 📤 Upload CSV button in the top header
3.	Select your .csv file — use data/sample_traffic.csv to test immediately
4.	The packet table, statistics panel, and log records populate automatically
5.	Use the Filter Panel to narrow results: 
o	Select a Protocol from the dropdown (All / TCP / UDP / ICMP)
o	Enter a Source IP address in the text field
o	Enter a Destination IP address in the text field
o	Select a Service from the dropdown (HTTP, DNS, SSH, HTTPS, etc.)
6.	Click 🔎 Apply Filters to update the table and recalculate statistics
7.	Click ✖ Clear to remove all active filters and return to the full dataset
8.	Check the Statistics Panel on the right for packet counts and averages
9.	Scroll down to the Log Records section to see terminal-style packet logs
________________________________________
📊 Dataset Format
Your CSV file must contain the following columns:
Column Name	Example Value	Description
Time	10:35:21	Timestamp of the captured packet
Source IP	192.168.1.5	IP address of the sender
Destination IP	8.8.8.8	IP address of the receiver
Protocol	TCP	Protocol type — TCP, UDP, or ICMP
Size	512	Packet size in bytes
Source Port	52341	Port number on the sender side
Dest Port	80	Port number on the receiver side
The Service column is derived automatically from Dest Port — you do not need to include it in your CSV file.
________________________________________
🗃️ Sample Data
A ready-to-use sample dataset is included at data/sample_traffic.csv with the following profile:
•	300 packets across TCP, UDP, and ICMP protocols
•	Source IPs from multiple private subnets: 192.168.1.x, 10.0.0.x, 172.16.0.x
•	Destination ports: 21, 22, 53, 80, 123, 443, 3306
•	Packet sizes: ranging from 64 to 1500 bytes
•	Timestamps: sequential entries starting from 10:35:21
You can also create your own CSV or use any publicly available network dataset — as long as it matches the column format described above.
________________________________________
🌐 API Routes
Route	Method	Description
/	GET	Serves the main dashboard with all loaded packet data
/api/upload	POST	Accepts CSV file upload, processes data, re-renders dashboard
/api/filter	GET	Accepts filter query parameters and returns filtered packet view
Filter Query Parameters — /api/filter
Parameter	Example	Description
protocol	TCP	Filter packets by protocol type
source_ip	192.168.1.5	Filter packets by source IP address
dest_ip	8.8.8.8	Filter packets by destination IP address
service	HTTP	Filter packets by mapped service name
________________________________________
🎓 Learning Outcomes
Building this project provided hands-on understanding of the following concepts:
•	The structure of network packets — IP addresses, port numbers, protocols, and payload sizes
•	How TCP, UDP, and ICMP differ in behavior and typical use cases across real networks
•	Port-to-service mapping and why application-layer services operate on well-known ports
•	Building a client-server web application using Flask and understanding the HTTP request-response cycle
•	Processing, filtering, and aggregating structured tabular data using the Pandas library
•	Using Jinja2 templating to render server-side data dynamically inside HTML pages
•	Designing and implementing a complete single-page UI from scratch using HTML5 and CSS3
•	How filtering and statistical aggregation work in the context of network traffic analysis
________________________________________
🚀 Future Enhancements
The following features are planned or could be added in future versions:
•	Real-Time Packet Sniffing — Integrate the scapy library to capture live packets from the network interface instead of relying on CSV uploads
•	Live Auto-Refresh — Use WebSockets or polling to automatically update the packet table every few seconds without a full page reload
•	Packet Export — Allow users to export filtered results back to a new downloadable CSV file
•	Traffic Charts — Add visual graphs for protocol distribution, traffic volume over time, and top talker IPs using Chart.js or Plotly
•	Alert System — Trigger visual warnings when suspicious IPs, unusual protocols, or abnormal packet volumes are detected
•	Pagination — Add page-based navigation for the packet table to handle very large datasets smoothly
•	PCAP Support — Allow direct upload of .pcap files and convert them internally to the required format
•	Theme Toggle — Add a light mode option alongside the existing dark theme
________________________________________
👤 Author
Muhamamd Dawood Student ID:BCSF24M030 Department: Computer Science Course: Computer Networks Semester: Spring 2025 University: Your University Name
________________________________________
📄 License
This project was developed for academic purposes as part of a Computer Networks course assignment. All code was written independently.
MIT License  Free to use for educational and academic purposes.


