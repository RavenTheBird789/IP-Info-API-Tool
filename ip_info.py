# IP Info Swiper
import requests
import json
import time
import os

def green(text: str) -> str: 
    # Wrap text in ANSI codes for green color
    return f"\033[92m{text}\033[0m"

def bold(text: str) -> str: 
    # Wrap text in ANSI codes for bold formatting
    return f"\033[1m{text}\033[0m"

def red(text: str) -> str: 
    # Wrap text in ANSI codes for red color
    return f"\033[91m{text}\033[0m"

# Global variables
equalSign = "="
emptySpace = " "
Wh = '\033[1;37m' # White color for API data returned
Gr = '\033[1;32m' # Green color for API data returned
x = 3
y = 0.5
z = 2

def trademark(ip_info_func):
    def wrapper():
        print(green(equalSign * 20))
        print(green(bold((emptySpace * 3) + "IP Info Swiper")))
        print(green(equalSign * 20))
        print(red("By: RavenTheBird789"))
        print(green(equalSign * 20))
        ip_info_func()
    return wrapper

def user_request():
    prompt = input(green("\nWould you like to use the tool again? (yes/no): "))
    if prompt == "yes":
        os.system('clear')
        main()
    elif prompt == "no":
        os.system('clear')
        print(green("Exiting"))
        time.sleep(y)
        os.system('clear')
        print(green("Exiting."))
        time.sleep(y)
        os.system('clear')
        print(green("Exiting.."))
        time.sleep(y)
        os.system('clear')
        print(green("Exiting..."))
        time.sleep(y)
        os.system('clear')
        os._exit(0);
    else:
        os.system('clear')
        print(red("Invalid input"))
        time.sleep(x)
        os.system('clear')
        user_request()

def get_ip_info(ip_address):
    """Fetch information about the given IP address using an external API."""
    req_api = requests.get(f"http://ipwho.is/{ip_address}")  # API IPWHOIS.IS
    if req_api.status_code == 200:
        ip_data = json.loads(req_api.text)
        time.sleep(z)
        print(f"{Wh}\n IP target       :{Gr}", ip_address)
        print(f"{Wh} Type IP         :{Gr}", ip_data["type"])
        print(f"{Wh} Country         :{Gr}", ip_data["country"])
        print(f"{Wh} Country Code    :{Gr}", ip_data["country_code"])
        print(f"{Wh} City            :{Gr}", ip_data["city"])
        print(f"{Wh} Continent       :{Gr}", ip_data["continent"])
        print(f"{Wh} Continent Code  :{Gr}", ip_data["continent_code"])
        print(f"{Wh} Region          :{Gr}", ip_data["region"])
        print(f"{Wh} Region Code     :{Gr}", ip_data["region_code"])
        print(f"{Wh} Latitude        :{Gr}", ip_data["latitude"])
        print(f"{Wh} Longitude       :{Gr}", ip_data["longitude"])
        lat = int(ip_data['latitude'])
        lon = int(ip_data['longitude'])
        print(f"{Wh} Maps            :{Gr}", f"https://www.google.com/maps/@{lat},{lon},8z")
        print(f"{Wh} EU              :{Gr}", ip_data["is_eu"])
        print(f"{Wh} Postal          :{Gr}", ip_data["postal"])
        print(f"{Wh} Calling Code    :{Gr}", ip_data["calling_code"])
        print(f"{Wh} Capital         :{Gr}", ip_data["capital"])
        print(f"{Wh} Borders         :{Gr}", ip_data["borders"])
        print(f"{Wh} Country Flag    :{Gr}", ip_data["flag"]["emoji"])
        print(f"{Wh} ASN             :{Gr}", ip_data["connection"]["asn"])
        print(f"{Wh} ORG             :{Gr}", ip_data["connection"]["org"])
        print(f"{Wh} ISP             :{Gr}", ip_data["connection"]["isp"])
        print(f"{Wh} Domain          :{Gr}", ip_data["connection"]["domain"])
        print(f"{Wh} ID              :{Gr}", ip_data["timezone"]["id"])
        print(f"{Wh} ABBR            :{Gr}", ip_data["timezone"]["abbr"])
        print(f"{Wh} DST             :{Gr}", ip_data["timezone"]["is_dst"])
        print(f"{Wh} Offset          :{Gr}", ip_data["timezone"]["offset"])
        print(f"{Wh} UTC             :{Gr}", ip_data["timezone"]["utc"])
        time.sleep(z)
        user_request();
    else:
        print(red({"error": "Unable to fetch IP information."}))
        time.sleep(x)
        user_request();

@trademark 
def main():
    ip_address = input(green("Enter an IP address: "))
    info = get_ip_info(ip_address)
    print(green(info))
main();
