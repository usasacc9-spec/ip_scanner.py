#!/usr/bin/env python3

import os
import platform
import threading

# Detect OS (Windows / Linux / Termux)
PARAM = "-n" if platform.system().lower() == "windows" else "-c"
NULL = "nul" if platform.system().lower() == "windows" else "/dev/null"

active_ips = []

# Banner
def banner():
    print("""
=================================
        IP SCANNER TOOL
=================================
    """)

# Scan function
def scan(ip):
    response = os.system(f"ping {PARAM} 1 {ip} > {NULL} 2>&1")
    if response == 0:
        print(f"[+] {ip} is ACTIVE")
        active_ips.append(ip)

# Main function
def main():
    banner()
    
    base_ip = input("Enter base IP (example 192.168.1): ").strip()
    
    if not base_ip:
        print("[-] Invalid input!")
        return
    
    print("\n[~] Scanning network...\n")
    
    threads = []
    
    for i in range(1, 255):
        ip = f"{base_ip}.{i}"
        t = threading.Thread(target=scan, args=(ip,))
        threads.append(t)
        t.start()
    
    # Wait for all threads
    for t in threads:
        t.join()
    
    print("\n=================================")
    print(f"[✓] Scan Complete")
    print(f"[✓] Active devices found: {len(active_ips)}")
    print("=================================")

# Run program
if __name__ == "__main__":
    main()