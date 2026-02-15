
# ⚡ Smart Energy Intelligence Dashboard

![Python](https://img.shields.io/badge/python-3.11-blue?style=flat-square)
![Flask](https://img.shields.io/badge/flask-2.3.2-green?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-yellow?style=flat-square)
![GitHub last commit](https://img.shields.io/github/last-commit/yourusername/smart-energy-dashboard?style=flat-square)

> Monitor your home or office energy consumption in real-time! Detect devices on your network, estimate their power usage, calculate daily costs, track history, and download detailed reports — all from a modern, responsive web dashboard.

---

## 🌟 Features

- **Device Detection:** Auto-detect devices on your Wi-Fi network (phones, laptops, TVs, routers, unknown devices).  
- **Power Estimation:** Shows estimated power consumption in Watts per device.  
- **Daily Energy & Cost:** Calculates estimated daily kWh usage and cost per device.  
- **History Tracking:** Saves the last 5 network scans with timestamps.  
- **Download Reports:** Export scan data as CSV.  
- **Interactive Charts:**  
  - Bar chart → Power per device  
  - Pie chart → Device type distribution  
- **Dark/Light Mode:** Smooth theme toggle.  
- **Auto-Refresh:** Updates every 10 seconds.  
- **Responsive UI:** Works on desktop, tablet, and mobile.

---

## 💻 Tech Stack

- **Backend:** Python 3, Flask, Scapy  
- **Frontend:** HTML, CSS, JavaScript, Chart.js  
- **Deployment:** Local network or any accessible server  

---

## ⚙️ Installation & Setup

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/smart-energy-dashboard.git
cd smart-energy-dashboard
````

2. **Create a virtual environment (recommended)**

```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the application**

```bash
sudo python app.py
```

> ⚠ Scapy requires elevated privileges for network scanning.

5. **Open the dashboard in your browser**

```
http://127.0.0.1:8000
```

> Replace `8000` with your configured port if different.

---

## 🔧 Configuration

* **Network Range:** Update in `app.py`:

```python
target_ip = "192.168.1.1/24"
```

* **Electricity Tariff:** Set KES per kWh in `app.py`:

```python
TARIFF = 25
```

---

## 🗂 Project Structure

```
smart-energy-dashboard/
│
├── app.py            # Backend Flask app
├── requirements.txt  # Python dependencies
├── static/
│   ├── style.css     # Frontend CSS
│   └── script.js     # Frontend JS
└── templates/
    └── index.html    # HTML dashboard
```

---

## 📈 Future Improvements

* Weekly & monthly energy cost trends
* Integration with smart plugs or IoT sensors for real-time measurement
* Mobile app version for on-the-go monitoring
* Alerts for unusually high device energy consumption
* Predictive analytics for long-term cost planning
* Multi-user authentication for household monitoring

---

## 📝 License

MIT License © 2026 [sunjoe508]

```

