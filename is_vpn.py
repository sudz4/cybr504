import ipaddress
import requests

def is_vpn_used():
    # Get the IP address being used by the device
    ip_address = requests.get('https://api.ipify.org').text
    
    # Check if the IP address belongs to a known VPN provider
    vpn_ips = [
        ipaddress.IPv4Network('103.192.152.0/22'),  # ExpressVPN
        ipaddress.IPv4Network('45.65.0.0/20'),     # NordVPN
        ipaddress.IPv4Network('198.18.0.0/15'),    # Private Internet Access
        # Add more VPN IP address ranges as needed
    ]
    
    for vpn_ip in vpn_ips:
        if ipaddress.IPv4Address(ip_address) in vpn_ip:
            return True
    
    return False

if is_vpn_used():
    print("A VPN is being used")
else:
    print("No VPN detected")

