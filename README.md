# Python Multi-Threaded Port Scanner

A fast TCP port scanner built in Python to identify open ports on a target host. 

## How It Works

1. The script takes the target IP address you provide in the terminal and verifies it.
2. It creates an empty list in the background to store any open ports it discovers.
3. It uses Python's threading library to scan all 65,535 ports simultaneously rather than one by one, which makes the scan incredibly fast.
4. For each port, it attempts a quick connection. If the connection is successful, it prints the open port to the screen and adds it to our list. If the port is closed, it silently ignores the error so the terminal doesn't get cluttered.
5. Once every port is checked, the script creates a new .txt file named after the target IP, writes the date and time, and saves the sorted list of open ports for your records.

## Usage

1. Find your local IP address to use as a target. On Windows, open Command Prompt and type: ipconfig, Look for the line that says "IPv4 Address". 

2. Run the scanner from your terminal by typing python followed by the script name and your target IP. 
Example: python scanner.py <target_ip>

## Acknowledgments

This script was built as a lab project while following TCM Security's Programming 100: Fundamentals course.
I am sharing it here to document my cybersecurity learning journey and hands-on practice with Python networking.

Disclaimer: This tool was created strictly for educational purposes and authorized lab testing.
