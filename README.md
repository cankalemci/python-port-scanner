# Python Multi-Threaded TCP Port Scanner

A TCP port scanner built in Python to identify open ports on a target host. The script uses socket programming and multithreading to perform TCP connection attempts across ports 1–65,535.

## How It Works
1. The script initializes a global list to store discovered open ports and accepts an IPv4 address or hostname that resolves to an IPv4 address as a command-line argument.
2. It resolves the target into an IPv4 address using Python's `socket.gethostbyname()` and prints the scan initialization details (target IP and start timestamp) to the terminal.
3. Using Python's `threading` library, it attempts to start a separate thread for each port in the range 1–65,535, allowing multiple TCP connection attempts to run concurrently.
4. Each thread attempts to establish a TCP connection to its assigned port, using a one-second connection timeout. If the connection succeeds (`connect_ex` returns `0`), the port is printed to the terminal in real time and added to the results list. Unsuccessful connection attempts and exceptions are ignored.
5. Once all threads have finished, the script checks whether any open ports were discovered.
6. If open ports are found, a `.txt` report is generated containing the target IP address, completion timestamp, and a numerically sorted list of discovered open ports.

**Note:** This is a TCP connect scanner. It does not perform SYN scanning or distinguish between closed, filtered, and unreachable ports.

**Implementation Note:** This implementation attempts to create up to 65,535 threads, so system resource limitations may prevent the scan from completing successfully.

## Usage
Run the script from your terminal by providing a target IP address or hostname:
`python scanner.py <target>`

**Example:**
`python scanner.py 192.168.1.10`

To scan your own machine, you can use the loopback address:
`python scanner.py 127.0.0.1`

*(On Windows, you can use `ipconfig` in Command Prompt to view your machine's local IPv4 address. Note: The IP address obtained through `ipconfig` belongs to your own machine, not necessarily the system you intend to scan. For lab environments, use the IP address of the target machine).*

## Output
During execution, the script prints the scan start time and displays any open ports in the terminal as they are discovered.

If one or more open ports are discovered, the script also automatically generates a text report upon completion named: `scan_<target_ip>.txt`

The report contains the target IP address, the scan completion timestamp, and the numerically sorted list of discovered open ports. 
**Note:** Existing reports with the same filename will be overwritten. If no open ports are discovered (or if the scan is interrupted with `Ctrl+C`), no report is generated.

## Acknowledgments
This script was developed as a lab project while following TCM Security's Programming 100: Fundamentals course. I'm sharing it to document my cybersecurity learning journey and hands-on practice with Python networking.

**Disclaimer:** This tool was developed strictly for educational purposes and authorized lab testing. Only scan systems you own or have explicit permission to test.
