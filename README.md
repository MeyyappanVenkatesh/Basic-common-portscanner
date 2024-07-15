# Port Scanner

This Python script performs a basic port scan on a specified host to check for open ports. It can scan a range of ports or specific ports from a predefined list of common ports.

Notes
- This is a basic and slow version of port scanning intended for educational purposes.
- Port scanning can only be performed if you know the host's IP address or have permission to scan the hostname.
- Ensure you have the necessary permissions to scan the target host.
- Use responsibly and respect the security and privacy of others.

## Features

- Scans a specified host (IPv4 address or hostname) for open ports.
- Supports scanning of specific ports from a predefined list of common ports.
- Displays verbose output indicating the progress and results of the scan.

## Usage

1. **Installation**
   - Clone the repository:

     ```
     git clone https://github.com/yourusername/port-scanner.git
     ```

2. **Running the Script**
   - Navigate to the directory containing `port_scanner.py`.
   - Run the script with Python 3, providing the target host as an argument:

     ```
     python3 port_scanner.py [ip/hostname]
     ```

   Replace `[ip/hostname]` with the IP address or hostname you want to scan.

3. **Output**
   - The script will display which ports are open on the specified host.

## Example

```bash
$ python3 port_scanner.py example.com
Scanning target: 93.184.216.34
Time started: 2024-07-15 12:00:00
--------------------------------------------------
Scanning port 80...
Port 80 is open
Scanning port 443...
Port 443 is open
Scanning complete.


