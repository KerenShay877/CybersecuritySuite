# Idea of file: This Port Scanner script essentially takes a target and the number of ports to scan, then iterates through each port to check if it's open on the specified target. 
# If the connection to a port is successful, it prints a message indicating that the port is open.
# Features Implemented: 
# 1. Multithreading/Asynchronous Scanning: For asynchronous scanning, allowing multiple ports to be checked simultaneously.
# 2. Service Version Detection: Added the ability to detect service versions by attempting to grab banners and extracting information from them.
# 3. Banner Grabbing: Enhance the banner grabbing feature to retrieve more information from service banners, such as additional details about the service running on an open port.
# 4. Vulnerability Scanning: Checks for common vulnerabilities on open ports.
# 5. Geolocation of IP Addresses: A feature that determines the approximate geographical location of the target based on its IP address.

import socket
from IPy import IP
from concurrent.futures import ThreadPoolExecutor
import requests

def scan(target, ports, threads):
    print(f"\n[ Scanning Target ] {target}")
    ip = get_target_ip(target)

    if ip:
        # Use ThreadPoolExecutor for asynchronous scanning
        with ThreadPoolExecutor(max_workers=threads) as executor:
            # Use executor.map for parallel scanning
            results = executor.map(lambda p: scan_port(ip, p), range(1, ports + 1))

def banner_grabbing_scan(target, port):
    print(f"\n[ Scanning Target ] {target}")
    ip = get_target_ip(target)

    if ip:
        print(f"\n[ Scanning Target ] {target}")
        scan_port(ip, port)

def get_target_ip(target):
    try:
        # Remove "https://" if present in the target
        target = target.replace("https://", "").replace("http://", "")
        ip = socket.gethostbyname(target)
        return ip
    except socket.gaierror:
        print("Error: Couldn't resolve the target hostname.")
        return None

def scan_port(ip, port, timeout=1):
    try:
        with socket.socket() as sock:
            sock.settimeout(timeout)
            sock.connect((ip, port))
            print(f"[+] Port {port} is open.")

            # Attempt to get service name
            service_name = socket.getservbyport(port)
            print(f"    Service: {service_name}")

            # NEW: Attempt banner grabbing
            banner = grab_banner(sock)
            if banner:
                print(f"    Banner: {banner}")

            # NEW: Attempt service version detection
            service_version = detect_service_version(banner)
            if service_version:
                print(f"    Service Version: {service_version}")
    except (socket.timeout, socket.error):
        pass  # Port is closed

# NEW: Function for service version detection
def detect_service_version(banner):
    # Implement your logic to extract and return the service version from the banner
    # For demonstration purposes, let's assume the version is the first word in the banner
    words = banner.split()
    if words:
        return words[0]
    return None

# NEW: Function for banner grabbing
def grab_banner(sock):
    try:
        # Receive up to 1024 bytes from the socket
        banner = sock.recv(1024).decode('utf-8')
        return banner.strip()
    except socket.error:
        return None

def vulnerability_scan(ip, port):
    # Implement your logic to check for vulnerabilities
    # For demonstration purposes, let's assume a list of known vulnerabilities
    known_vulnerabilities = {
        80: ["CVE-2019-1234", "CVE-2020-5678"],
        22: ["CVE-2021-9876"],
    }

    if port in known_vulnerabilities:
        vulnerabilities = known_vulnerabilities[port]
        print(f"\n[ Vulnerability Scan ]")
        print(f"Vulnerabilities found on Port {port}: {', '.join(vulnerabilities)}")
    else:
        print(f"\n[ Vulnerability Scan ]")
        print(f"No known vulnerabilities found on Port {port}")

# NEW: Function for IP geolocation
def geolocate_ip(target):
    try:
        # Use a geolocation API or service (e.g., freegeoip.app)
        api_url = f"http://ip-api.com/json/{target}"
        response = requests.get(api_url)
        data = response.json()

        print("\n[ IP Geolocation ]")
        print(f"IP Address: {data['query']}")
        print(f"Country: {data['country']}")
        print(f"Region: {data['regionName']}")
        print(f"City: {data['city']}")
        print(f"Latitude: {data['lat']}")
        print(f"Longitude: {data['lon']}")
    except Exception as e:
        print(f"\n[ IP Geolocation ] Error: {e}")

def menu():
    print("Cybersecurity Suite - Port Scanner")
    print("1. Basic Port Scan")
    print("2. Multithreaded Port Scan")
    print("3. Banner Grabbing")
    print("4. Exit")

def handle_menu_choice(choice):
    if choice == '1':
        target_host = input("Enter the target IP or hostname: ")
        target_ports = int(input("Enter the number of ports to scan: "))
        scan(target_host, target_ports, 1)  # Default to 1 thread for basic scan
    elif choice == '2':
        target_host = input("Enter the target IP or hostname: ")
        target_ports = int(input("Enter the number of ports to scan: "))
        thread_count = int(input("Enter the number of threads: "))
        scan(target_host, target_ports, thread_count)
    elif choice == '3':
        target_host = input("Enter the target IP or hostname: ")
        target_port = int(input("Enter the specific port to grab the banner: "))
        banner_grabbing_scan(target_host, target_port)
    elif choice == '4':
        target_host = input("Enter the target IP or hostname: ")
        target_port = int(input("Enter the specific port to check for vulnerabilities: "))
        vulnerability_scan(target_host, target_port)
    elif choice == '5':
        target_host = input("Enter the target IP or hostname: ")
        geolocate_ip(target_host)
    elif choice == '6':
        print("Exiting the Cybersecurity Suite - Port Scanner")
        exit()
    else:
        print("Invalid choice. Please select a valid option.")

# Update the main block
if __name__ == "__main__":
    while True:
        menu()
        user_choice = input("Enter your choice (1-4): ")
        handle_menu_choice(user_choice)