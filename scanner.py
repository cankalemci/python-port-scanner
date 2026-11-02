import sys
import socket
from datetime import datetime
import threading 

# Global list to store discovered open ports for reporting
open_ports = []

# Attempt connection to a specific target port
def scan_port(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))
        
        # A result of 0 means the port is open
        if result == 0:
            print(f"Port {port} is open")
            open_ports.append(port) 
        s.close()
        
    except socket.error:
        pass # Silenced to keep the terminal output clean during fast scans
    except Exception:
        pass

# Validate arguments, resolve target, and execute threading
def main():
    # Ensure the user provides exactly one argument (the target IP/Hostname)
    if len(sys.argv) == 2:
        target = sys.argv[1]
    else:
        print("Invalid number of arguments.")
        print("Usage: python scanner.py <target>")
        sys.exit(1)

    # Translate the provided hostname into an IPv4 address
    try:
        target_ip = socket.gethostbyname(target)    
    except socket.gaierror:
        print(f"Error: Unable to resolve hostname {target}")
        sys.exit(1)

    # Display scan initialization details
    print("-" * 50)
    print(f"Scanning target {target_ip}")
    print(f"Time started: {datetime.now()}")
    print("-" * 50)

    try: 
        # Spin up concurrent threads for all 65,535 ports
        threads = []
        for port in range(1, 65536):
            thread = threading.Thread(target=scan_port, args=(target_ip, port))
            threads.append(thread)
            thread.start()

        # Keep the main program running until all threads finish
        for thread in threads:
            thread.join()

    # Handle the user pressing Ctrl+C safely
    except KeyboardInterrupt:
        print("\nExiting program.")
        sys.exit(0)

    except socket.error as e:
        print(f"Socket error: {e}")
        sys.exit(1)

    print("\nScan completed!")

    # --- File Reporting Feature ---
    # Automatically generate a .txt log if any open ports were found
    if open_ports:
        filename = f"scan_{target_ip}.txt"
        
        with open(filename, "w") as file:
            file.write(f"Port Scan Results for {target_ip}\n")
            file.write(f"Completed at: {datetime.now()}\n")
            file.write("-" * 50 + "\n")
            
            # Sort the findings numerically so the report is easy to read
            for p in sorted(open_ports):
                file.write(f"Port {p} is open\n")
                
        print(f"[*] Report successfully saved to {filename}")

if __name__ == "__main__":
    main()