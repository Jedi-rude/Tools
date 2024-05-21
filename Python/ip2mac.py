from scapy.all import ARP, Ether, srp
import argparse

def get_mac(ip_address, interface):
    # Create an ARP request packet
    arp_request = ARP(pdst=ip_address)

    # Create Ethernet frame
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")

    # Combine Ethernet frame and ARP request packet
    packet = ether / arp_request

    # Send the packet and capture the response
    result = srp(packet, timeout=3, iface=interface, verbose=False)[0]

    # Extract the MAC address from the response
    if result:
        return result[0][1].hwsrc
    else:
        return None

# Example usage
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MAC Address Finder")
    parser.add_argument("-ip", type=str, required=True, help="IP address to find MAC address, 192.168.1.1")
    parser.add_argument("-I", type=str, required=True, help="Interface to find")
    args = parser.parse_args()
    target_ip = args.ip  # Specify the IP address you want to find the MAC address for
    interface = args.I
    mac_address = get_mac(target_ip, interface)
    if mac_address:
        print_colored_text(f"The MAC address of {target_ip} is {mac_address}", "green")
    else:
        print_colored_text(f"The MAC address resolution is failed {target_ip}", "red")
