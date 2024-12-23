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
