# web_security_scanner.py

import requests
from bs4 import BeautifulSoup

def scan_web_application(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        print(f"Scanning {url} - Completed")
    except Exception as e:
        print(f"Error scanning web application: {e}")
