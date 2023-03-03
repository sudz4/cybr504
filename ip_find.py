# import requests

# def get_location_info(ip_address):
#     url = f"https://ipapi.co/{ip_address}/json/"
#     response = requests.get(url)
#     data = response.json()
#     return {
#         "ip": data["ip"],
#         "city": data["city"],
#         "region": data["region"],
#         "country": data["country_name"],
#         "latitude": data["latitude"],
#         "longitude": data["longitude"]
#     }

# def check_vpn():
#     ip_before = requests.get('https://api.ipify.org').text
#     location_before = get_location_info(ip_before)
#     print("Location before VPN connection: ")
#     print(location_before)

#     # Connect to VPN here using your preferred method
#     ip_after = requests.get('https://api.ipify.org').text
#     location_after = get_location_info(ip_after)
#     print("Location after VPN connection: ")
#     print(location_after)

#     if ip_before == ip_after:
#         print("VPN not working")
#     else:
#         print("VPN working")

# check_vpn()

import requests
import time

def get_location_info(ip_address):
    url = f"https://ipapi.co/{ip_address}/json/"
    response = requests.get(url)
    data = response.json()
    return {
        "ip": data["ip"],
        "city": data["city"],
        "region": data["region"],
        "country": data["country_name"],
        "latitude": data["latitude"],
        "longitude": data["longitude"]
    }

def check_vpn():
    ip_before = requests.get('https://api.ipify.org').text
    location_before = get_location_info(ip_before)
    print("Location before VPN connection: ")
    print(location_before)

    print("Please connect to the VPN now.")
    for i in range(30, 0, -1):
        print(f"Connecting to VPN in {i} seconds...")
        time.sleep(1)  # Wait for 1 second

    ip_after = requests.get('https://api.ipify.org').text
    location_after = get_location_info(ip_after)
    print()
    print("Location before VPN connection (2): ")
    print(location_before)

    print("Location after VPN connection: ")
    print(location_after)

    if ip_before == ip_after:
        print("VPN not working")
    else:
        print("VPN working")

check_vpn()

