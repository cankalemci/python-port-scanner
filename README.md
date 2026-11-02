# Python TCP Port Scanner

A Python TCP port scanner that uses `socket` and `threading` to check ports 1–65,535 on a target host.

## How It Works
1. Takes a target IPv4 address or hostname as a command-line argument and resolves it via `socket.gethostbyname()`.
2. Spawns a separate thread for each port (1–65,535) to run TCP connection attempts concurrently.
3. Each thread tries to connect with a 1-second timeout. Open ports (`connect_ex == 0`) are printed to the terminal in real time and saved to a global list. Closed ports and errors are silently ignored.
4. Once all threads finish, if any open ports were found, the script writes a sorted summary to a `.txt` file.

* **Note:** This is a full TCP connect scanner. It does not do SYN scans or distinguish between closed, filtered, or unreachable ports.
* **Limitation:** Because it attempts to spawn 65,535 threads at once, you may hit OS thread or file-descriptor limits before the scan finishes.

## Usage
`python scanner.py <target>`

**Examples:**
* Scan a specific lab target: `python scanner.py 192.168.1.10`
* Scan your own machine: `python scanner.py 127.0.0.1`

*(Tip: Running `ipconfig` on Windows shows your own local IP, not your target's. Make sure you use the target machine's IP in lab environments.)*

## Output
Open ports print to the terminal as they are found. If at least one open port is discovered, the script saves a report named `scan_<target_ip>.txt` containing the target IP, completion timestamp, and numerically sorted list of open ports.

*(Existing reports with the same name are overwritten. If no open ports are found, no file is created.)*

## Acknowledgments
Built as a lab project during TCM Security's *Programming 100: Fundamentals* course to practice Python networking.

**Disclaimer:** For educational and authorized lab testing only. Only scan systems you own or have permission to test.
