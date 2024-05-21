from scapy.all import ARP, Ether, srp
import argparse

def scan_network(ip_range):
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    result = srp(packet, timeout=3, verbose=False)[0]

    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})
    
    return devices

def find_mac(mac_address, devices):
    for device in devices:
        if device['mac'] == mac_address:
            return device['ip']
    return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MAC Address Tracker")
    parser.add_argument("--ip", type=str, required=True, help="IP address range to scan, 192.168.1.1/24")
    parser.add_argument("--mac", type=str, required=True, help="MAC address to track")
    args = parser.parse_args()

    ip_range = args.ip
    devices = scan_network(ip_range)
    target_mac = args.mac 
    ip_address = find_mac(target_mac, devices)
    if ip_address:
        print(f"MAC address {target_mac} found at IP address {ip_address}")
        print("Target is in our local network")
    else:
        print(f"MAC address {target_mac} not found in the network.")
