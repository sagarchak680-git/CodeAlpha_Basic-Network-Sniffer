"""
Basic Network Sniffer
Educational cybersecurity project.

Use only on networks/devices you own or have explicit permission to monitor.
"""

from datetime import datetime
from scapy.all import sniff, IP, IPv6, TCP, UDP, ICMP, Raw


def protocol_name(packet):
    if packet.haslayer(TCP):
        return "TCP"
    if packet.haslayer(UDP):
        return "UDP"
    if packet.haslayer(ICMP):
        return "ICMP"
    if packet.haslayer(IP) or packet.haslayer(IPv6):
        return "IP"
    return "Other"


def get_addresses(packet):
    if packet.haslayer(IP):
        return packet[IP].src, packet[IP].dst
    if packet.haslayer(IPv6):
        return packet[IPv6].src, packet[IPv6].dst
    return "-", "-"


def get_ports(packet):
    if packet.haslayer(TCP):
        return packet[TCP].sport, packet[TCP].dport
    if packet.haslayer(UDP):
        return packet[UDP].sport, packet[UDP].dport
    return "-", "-"


def payload_preview(packet, limit=32):
    if not packet.haslayer(Raw):
        return "-"
    data = bytes(packet[Raw].load)
    preview = data[:limit]
    return preview.hex(" ") + (" ..." if len(data) > limit else "")


def analyze_packet(packet):
    src, dst = get_addresses(packet)
    sport, dport = get_ports(packet)
    protocol = protocol_name(packet)

    print("-" * 72)
    print("Time      :", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("Protocol  :", protocol)
    print("Source    :", f"{src}:{sport}")
    print("Destination:", f"{dst}:{dport}")
    print("Length    :", len(packet), "bytes")
    print("Payload   :", payload_preview(packet))


def start_sniffer(packet_count=20):
    print("=" * 72)
    print(" BASIC NETWORK SNIFFER")
    print("=" * 72)
    print("Capturing IP packets on this machine.")
    print("Press Ctrl+C to stop early.")
    print()

    sniff(
        filter="ip",
        prn=analyze_packet,
        count=packet_count,
        store=False
    )


if __name__ == "__main__":
    try:
        count = input("How many packets should be captured? [20]: ").strip()
        packet_count = int(count) if count else 20

        if packet_count <= 0:
            raise ValueError

        start_sniffer(packet_count)

    except ValueError:
        print("Please enter a positive whole number.")
    except KeyboardInterrupt:
        print("\nCapture stopped by user.")
    except PermissionError:
        print("\nPermission denied. Run the terminal with the required privileges.")
    except Exception as exc:
        print(f"\nError: {exc}")
