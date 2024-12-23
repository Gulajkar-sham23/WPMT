# WPMT
<h1>Project: Website Performance Monitoring Tool</h1>

<h3>Objective: </h3>
Design a Python-based monitoring tool to track website uptime and response times using Prometheus.

<h1>Steps to Configure:</h1>

<h2>Step 1: Install Prometheus </h2>

Download and Extract Prometheus:

bash:

wget https://github.com/prometheus/prometheus/releases/download/v2.47.0/prometheus-2.47.0.linux-amd64.tar.gz
tar -xvzf prometheus-2.47.0.linux-amd64.tar.gz
cd prometheus-2.47.0.linux-amd64

<h2>Step 2: Set Up Python Exporter <h2>
    
Install Prometheus Client Library:

bash:
pip install prometheus_client requests
Create a Python Exporter (exporter.py):

python:
from prometheus_client import start_http_server, Gauge
import requests
import time

website_up = Gauge('website_up', 'Status of the website (1 = UP, 0 = DOWN)')
website_response_time = Gauge('website_response_time', 'Response time of the website')

def monitor_website():
    while True:
        try:
            response = requests.get("https://example.com", timeout=5)
            website_up.set(1)
            website_response_time.set(response.elapsed.total_seconds())
        except requests.exceptions.RequestException:
            website_up.set(0)
        time.sleep(10)

if __name__ == "__main__":
    start_http_server(8000)
    monitor_website()
    
Run the Exporter:
bash:
python exporter.py

Step 3: Configure Prometheus
Edit Prometheus Configuration (prometheus.yml):
yaml:

scrape_configs:
  - job_name: 'website_monitor'
    static_configs:
      - targets: ['localhost:8000']
      - 
Start Prometheus:

bash:
./prometheus --config.file=prometheus.yml

<h2> Step 4: Visualize in Prometheus Dashboard</h2>h2>
Access Prometheus Dashboard: http://localhost:9090.
Query Metrics:
website_up: Displays if the website is up (1) or down (0).
website_response_time: Shows the website's response time.
