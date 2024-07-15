import sys
from datetime import datetime as dt
import socket

# List of common port numbers to scan
common_ports = [
    20, 21, 22, 23, 25, 53, 67, 68, 69, 80,
    110, 123, 143, 161, 162, 179, 194, 443, 445, 465,
    514, 515, 587, 631, 636, 989, 990, 993, 995, 1080,
    1194, 1433, 1434, 1521, 1723, 1812, 1813, 2049, 2082, 2083,
    3128, 3260, 3306, 3389, 5432, 5900, 8080, 8443, 9000, 10000, 139, 135
]

# Check if the user has provided the correct number of arguments
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])  # Translates the host to its IPv4 address
else:
    print("Invalid number of args")
    print("Syntax: python3 port_scanner.py [ip/hostname]")
    sys.exit()

# Print the target and the time the scan started
print("Scanning target: " + target)
print("Time started: " + str(dt.now()))
print('-' * 50)

try:
    # Scan common ports
    for port in common_ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket object
        socket.setdefaulttimeout(0.5)  # Set a timeout for the connection attempt
        print(f"Scanning port {port}...", end="\r")  # Print the current port being scanned
        result = s.connect_ex((target, port))  # Try to connect to the port
        if result == 0:
            print(f"\nPort {port} is open")  # If the connection was successful, the port is open
        s.close()  # Close the socket
    print("\nScanning complete.")
except KeyboardInterrupt:
    # Handle the user interrupting the script (Ctrl+C)
    print('\nExiting...')
    sys.exit()
except socket.gaierror:
    # Handle errors when the hostname could not be resolved
    print("Hostname couldn't be resolved")
    sys.exit()
except socket.error:
    # Handle errors when the socket could not connect to the server
    print("Couldn't connect to server")
    sys.exit()
