# Basic Network Sniffer

## 1. Project Overview

This project is a beginner-friendly Python network sniffer built with **Scapy**. It captures IP packets visible to the computer, analyzes basic packet information, and displays:

- Source IP address
- Destination IP address
- Protocol
- Source and destination ports
- Packet length
- A short hexadecimal payload preview

The project is intended for cybersecurity learning and understanding how data travels through a network.

## 2. Objectives

1. Capture network traffic packets using Python.
2. Understand the structure of network packets.
3. Identify common protocols such as TCP, UDP and ICMP.
4. Display source and destination addresses.
5. Inspect a limited payload preview for educational analysis.
6. Learn basic packet-flow concepts.

## 3. Technologies Used

- Python 3
- Scapy
- TCP/IP networking concepts
- Command-line interface

## 4. Project Structure

```text
basic_network_sniffer/
│
├── network_sniffer.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 5. Installation

### Step 1: Check Python

```bash
python --version
```

### Step 2: Install Scapy

```bash
pip install -r requirements.txt
```

### Windows

Scapy packet capture may require **Npcap** to be installed. Run the terminal with the privileges required by your system.

### Linux/macOS

Packet capture may require elevated privileges depending on the interface and operating-system configuration.

## 6. Run the Project

```bash
python network_sniffer.py
```

The program asks:

```text
How many packets should be captured? [20]:
```

Enter a number such as `20`.

Example output:

```text
------------------------------------------------------------------------
Time      : 2026-10-16 21:00:00
Protocol  : TCP
Source    : 192.168.1.10:54321
Destination: 142.250.195.14:443
Length    : 74 bytes
Payload   : -
```

## 7. How It Works

### Packet Capture

Scapy's `sniff()` function listens for packets that match the `ip` filter.

### Packet Analysis

For every captured packet, the program checks whether it contains:

- TCP
- UDP
- ICMP
- IPv4/IPv6 information
- A raw payload

### Information Display

The program extracts the source and destination addresses, ports, protocol and packet size.

## 8. Protocols

### TCP

TCP provides reliable, connection-oriented communication and is commonly used by web applications and other network services.

### UDP

UDP is connectionless and has lower overhead than TCP. It is used by applications such as DNS and streaming-related services.

### ICMP

ICMP is used for network control and diagnostic messages, such as those associated with `ping`.

## 9. Security and Privacy

Only capture traffic on systems or networks that you own or have explicit permission to monitor.

The program intentionally limits payload output to a short hexadecimal preview. Do not use packet capture to collect passwords, private messages, cookies, or other sensitive information.

## 10. Possible Improvements

Future versions could add:

- Packet filtering by protocol
- CSV/JSON export
- Packet counters
- A graphical user interface
- Protocol statistics
- Interface selection
- PCAP export for authorized lab analysis
- Charts showing traffic distribution

## 11. Conclusion

The Basic Network Sniffer demonstrates how Python and Scapy can be used to observe and analyze network packets. It provides practical understanding of IP addresses, ports, protocols, packet sizes and the flow of data across a network.
