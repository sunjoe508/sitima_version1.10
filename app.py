from flask import Flask, render_template, jsonify, send_file
from scapy.all import ARP, Ether, srp
import socket, csv, io, datetime

app = Flask(__name__)

# Power and tariff
device_power_map = {
    "phone": 10,
    "laptop": 65,
    "tv": 120,
    "router": 15,
    "unknown": 50
}
TARIFF = 25  # KES per kWh

# Store last 5 scans
scan_history = []

def scan_network():
    target_ip = "192.168.1.1/24"  # update for your router
    arp = ARP(pdst=target_ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    result = srp(packet, timeout=2, verbose=0)[0]
    devices = []

    for sent, received in result:
        ip = received.psrc
        mac = received.hwsrc
        try:
            hostname = socket.gethostbyaddr(ip)[0]
        except:
            hostname = ip

        device_type = classify_device(hostname.lower())
        power = device_power_map.get(device_type, 50)
        daily_kwh = power * 24 / 1000  # daily estimate
        cost = daily_kwh * TARIFF

        devices.append({
            "ip": ip,
            "mac": mac,
            "hostname": hostname,
            "type": device_type,
            "estimated_power": power,
            "daily_kwh": round(daily_kwh,2),
            "daily_cost": round(cost,2)
        })

    # Save scan history
    scan_history.insert(0, {"timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "devices": devices})
    if len(scan_history) > 5:
        scan_history.pop()

    return devices

def classify_device(name):
    if "iphone" in name or "android" in name:
        return "phone"
    if "laptop" in name or "pc" in name:
        return "laptop"
    if "tv" in name:
        return "tv"
    if "router" in name:
        return "router"
    return "unknown"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/scan")
def scan():
    devices = scan_network()
    return jsonify(devices)

@app.route("/history")
def history():
    return jsonify(scan_history)

@app.route("/download")
def download():
    if not scan_history:
        return "No scans available", 404

    latest_scan = scan_history[0]["devices"]
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["Hostname","IP","MAC","Type","Power (W)","Daily kWh","Daily Cost (KES)"])
    for d in latest_scan:
        writer.writerow([d['hostname'], d['ip'], d['mac'], d['type'], d['estimated_power'], d['daily_kwh'], d['daily_cost']])
    
    output.seek(0)
    return send_file(io.BytesIO(output.getvalue().encode()), 
                     mimetype="text/csv", 
                     as_attachment=True, 
                     download_name="smart_energy_report.csv")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
