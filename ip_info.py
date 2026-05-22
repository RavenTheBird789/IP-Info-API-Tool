# IP Info API Tool
import requests

def green(text: str) -> str: 
    # Wrap text in ANSI codes for green color
    return f"\033[92m{text}\033[0m"

def bold(text: str) -> str: 
    # Wrap text in ANSI codes for bold formatting
    return f"\033[1m{text}\033[0m"

def red(text: str) -> str: 
    # Wrap text in ANSI codes for red color
    return f"\033[91m{text}\033[0m"

equalSign = "="
emptySpace = "  "

print(green(equalSign * 20))
print(green(bold(emptySpace + "IP Info API Tool")))
print(green(equalSign * 20))
print(red("By: RavenTheBird789"))
print(green(equalSign * 20))

def get_ip_info(ip_address):
    """Fetch information about the given IP address using an external API."""
    token = "defb5d2969542e"
    url = f"https://api.ipinfo.io/lite/{ip_address}?token={token}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return green(response.json())
    else:
        return red({"error": "Unable to fetch IP information."})
    
def main():
    ip_address = input(green("Enter an IP address: "))
    info = get_ip_info(ip_address)
    print(green(info))
main();
