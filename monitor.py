import os
import requests
import time
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)

def check_network():
    
    targets = os.getenv("MONITOR_TARGETS", "https://google.com,https://github.com")
    url_list = [url.strip() for url in targets.split(",")]

    logging.info(f"Starting NetGuard-CI Monitor on: {url_list}")

    for url in url_list:
        try:
            # We set a timeout so the app doesn't hang (Reliability)
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                logging.info(f"UP   | {url} - Status: {response.status_code}")
            else:
                logging.warning(f"DOWN | {url} - Status: {response.status_code}")
        except requests.exceptions.RequestException as e:
            logging.error(f"FAIL | {url} - Error: {str(e)}")

if __name__ == "__main__":
    check_network()