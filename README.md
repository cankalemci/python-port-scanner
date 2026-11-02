# Python Multi-Threaded TCP Port Scanner

A TCP port scanner built in Python to identify open ports on a target host. The script uses socket programming and multithreading to perform TCP connection attempts across ports 1–65,535.

## How It Works

1. The script accepts an IPv4 address or hostname that resolves to an IPv4 address as a command-line argument.
2. It resolves the target into an IPv4 address using Python's socket.gethostbyname().
3. It initializes an empty list to store discovered open ports.
4. Using Python's threading library, it attempts to start a separate thread for each port in the range 1–65,535, allowing multiple TCP connection attempts to run concurrently.
5. Each thread attempts to establish a TCP connection to its assigned port, using a one-second connection timeout. If the connection succeeds, the port is identified as open and added to the results list. Unsuccessful connection attempts are ignored.
6. Once all threads have finished, the script checks whether any open ports were discovered.
7. If open ports are found, a .txt report is generated containing the target IP address, completion timestamp, and numerically sorted list of discovered open ports.

Note: This is a TCP connect scanner. It does not perform SYN scanning or distinguish between closed, filtered, and unreachable ports.

Implementation Note: This implementation attempts to create up to 65,535 threads, so system resource limitations may prevent the scan from completing successfully.

## Usage

Run the script from your terminal by providing a target IP address or hostname:
python scanner.py <target>

Example:
python scanner.py 192.168.1.10

To scan your own machine, you can use the loopback address:
python scanner.py 127.0.0.1

(On Windows, you can use ipconfig in Command Prompt to view your machine's local IPv4 address. Note: The IP address obtained through ipconfig belongs to your own machine, not necessarily the system you intend to scan. For lab environments, use the IP address of the target machine).

## Output

If one or more open ports are discovered, the script automatically generates a text report named: scan_<target_ip>.txt

The report contains the discovered open ports and the scan completion timestamp. Note: Existing reports with the same filename will be overwritten. If no open ports are discovered, no report is generated.

## Acknowledgments

This script was developed as a lab project while following TCM Security's Programming 100: Fundamentals course. I'm sharing it to document my cybersecurity learning journey and hands-on practice with Python networking.

Disclaimer: This tool was developed strictly for educational purposes and authorized lab testing. Only scan systems you own or have explicit permission to test.
