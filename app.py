from flask import Flask, request, render_template, redirect, url_for
from flask_cors import CORS
import pandas as pd
import os

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'data'
ALLOWED_EXTENSIONS = {'csv'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024

packets_data = []
filtered_packets = []

PORT_SERVICE_MAP = {
    21: 'FTP',
    22: 'SSH',
    23: 'Telnet',
    25: 'SMTP',
    53: 'DNS',
    80: 'HTTP',
    110: 'POP3',
    143: 'IMAP',
    123: 'NTP',
    443: 'HTTPS',
    445: 'SMB',
    3306: 'MySQL',
    3389: 'RDP',
    5432: 'PostgreSQL',
    6379: 'Redis',
    27017: 'MongoDB',
    8080: 'HTTP-Alt',
    8443: 'HTTPS-Alt'
}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_service_from_port(port):
    try:
        port_num = int(port)
        return PORT_SERVICE_MAP.get(port_num, f'Port {port}')
    except:
        return 'Unknown'

def process_csv_data(df):
    try:
        required_columns = ['Time', 'Source IP', 'Destination IP', 'Protocol', 'Size', 'Source Port', 'Dest Port']
        
        for col in required_columns:
            if col not in df.columns:
                return None, f"Missing column: {col}"
        
        packets = []
        for idx, row in df.iterrows():
            packet = {
                'id': idx,
                'Time': str(row['Time']),
                'Source IP': str(row['Source IP']),
                'Destination IP': str(row['Destination IP']),
                'Protocol': str(row['Protocol']),
                'Size': int(row['Size']),
                'Source Port': int(row['Source Port']),
                'Dest Port': int(row['Dest Port']),
                'Service': get_service_from_port(int(row['Dest Port']))
            }
            packets.append(packet)
        
        return packets, None
    except Exception as e:
        return None, str(e)

def calculate_stats(packets):
    if not packets:
        return {
            'total': 0,
            'tcp': 0,
            'udp': 0,
            'icmp': 0,
            'avg_size': 0,
            'total_size': 0
        }
    
    total = len(packets)
    tcp_count = len([p for p in packets if p['Protocol'] == 'TCP'])
    udp_count = len([p for p in packets if p['Protocol'] == 'UDP'])
    icmp_count = len([p for p in packets if p['Protocol'] == 'ICMP'])
    total_size = sum([p['Size'] for p in packets])
    avg_size = round(total_size / total, 2) if total > 0 else 0
    
    return {
        'total': total,
        'tcp': tcp_count,
        'udp': udp_count,
        'icmp': icmp_count,
        'avg_size': avg_size,
        'total_size': total_size
    }
    
def generate_logs(packets, limit=10):
    """Generate log entries from packets"""
    if not packets:
        return []
    
    logs = []
    for packet in packets[:limit]:
        log_entry = f"[{packet['Time']}] {packet['Protocol']} packet from {packet['Source IP']}:{packet['Source Port']} → {packet['Destination IP']}:{packet['Dest Port']} ({packet['Size']} bytes) - {packet['Service']}"
        logs.append(log_entry)
    
    return logs

def get_unique_services(packets):
    """Get unique services from packets"""
    if not packets:
        return []
    
    services = set()
    for packet in packets:
        services.add(packet['Service'])
    
    return sorted(list(services))

@app.route('/')
def index():
    global packets_data
    stats = calculate_stats(packets_data)
    logs=generate_logs(packets_data)
    services=get_unique_services(packets_data)
    return render_template('index.html', packets=packets_data, stats=stats,logs=logs,services=services)

@app.route('/api/upload', methods=['POST'])
def upload_file():
    global packets_data
    
    try:
        if 'file' not in request.files:
            return render_template('index.html', error='No file provided'), 400
        
        file = request.files['file']
        
        if file.filename == '':
            return render_template('index.html', error='No file selected'), 400
        
        if not allowed_file(file.filename):
            return render_template('index.html', error='Only CSV files allowed'), 400
        
        try:
            df = pd.read_csv(file)
        except Exception as e:
            return render_template('index.html', error=f'Error reading CSV: {str(e)}'), 400
        
        packets, error = process_csv_data(df)
        
        if error:
            return render_template('index.html', error=error), 400
        
        packets_data = packets
        stats = calculate_stats(packets_data)
        logs = generate_logs(packets_data)
        services = get_unique_services(packets_data)
        
        
        return render_template('index.html', packets=packets_data, stats=stats,logs=logs,services=services,success=f'Successfully uploaded {stats["total"]} packets!')
    
    except Exception as e:
        return render_template('index.html', error=f'Server error: {str(e)}'), 500

@app.route('/api/filter', methods=['GET'])
def filter_packets():
    global packets_data
    
    try:
        if not packets_data:
            stats = calculate_stats([])
            return render_template('index.html', packets=[], stats=stats)
        
        protocol = request.args.get('protocol', 'All')
        source_ip = request.args.get('source_ip', '')
        dest_ip = request.args.get('dest_ip', '')
        service = request.args.get('service', 'All')
        
        filtered = packets_data.copy()
        
        if protocol != 'All':
            filtered = [p for p in filtered if p['Protocol'] == protocol]
        
        if source_ip:
            filtered = [p for p in filtered if p['Source IP'] == source_ip]
        
        if dest_ip:
            filtered = [p for p in filtered if p['Destination IP'] == dest_ip]
        
        if service != 'All':
            filtered = [p for p in filtered if p['Service'] == service]
        
        stats = calculate_stats(filtered)
        
        logs = generate_logs(filtered)
        services = get_unique_services(packets_data)
        
        return render_template('index.html', packets=filtered, stats=stats,logs=logs,services=services,filter_applied=f'Showing {stats["total"]} filtered packets')
    
    except Exception as e:
        stats = calculate_stats(packets_data)
        return render_template('index.html',packets=packets_data,stats=stats,error=str(e)), 500

@app.errorhandler(404)
def not_found(error):
    return render_template('index.html', error='Page not found'), 404

@app.errorhandler(500)
def server_error(error):
    return render_template('index.html', error='Internal server error'), 500

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    
    app.run(debug=True, host='127.0.0.1', port=5000)