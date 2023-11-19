# ssl_certificate_scanner.py

import ssl
import socket
from datetime import datetime

def scan_ssl_certificate(hostname, port=443):
    try:
        context = ssl.create_default_context()
        with context.wrap_socket(socket.create_connection((hostname, port)), server_hostname=hostname) as sock:
            cert = sock.getpeercert()

        expiration_date = datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')
        today = datetime.now()

        print(f"SSL Certificate Information for {hostname}:{port}")
        print(f"Subject: {cert['subject'][0][0][1]}")
        print(f"Issuer: {cert['issuer'][0][0][1]}")
        print(f"Valid From: {cert['notBefore']}")
        print(f"Valid Until: {cert['notAfter']}")

        if today < expiration_date:
            print("Certificate is valid.")
        else:
            print("Certificate has expired.")

    except Exception as e:
        print(f"Error scanning SSL certificate: {e}")
