# IP Info API Tool
import requests

def get_ip_info(ip_address):
    """Fetch information about the given IP address using an external API."""
    token = "defb5d2969542e"
    url = f"https://api.ipinfo.io/lite/{ip_address}?token={token}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Unable to fetch IP information."}
    
def main():
    ip_address = input("Enter an IP address: ")
    info = get_ip_info(ip_address)
    print(info)
main();