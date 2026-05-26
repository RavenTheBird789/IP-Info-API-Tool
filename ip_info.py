# IP Info API Tool
import requests
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
emptySpace = "  "
x = 3
y = 0.5

def trademark(ip_info_func):
    def wrapper():
        print(green(equalSign * 20))
        print(green(bold(emptySpace + "IP Info API Tool")))
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
    token = "defb5d2969542e"
    url = f"https://api.ipinfo.io/lite/{ip_address}?token={token}"
    response = requests.get(url)
    
    if response.status_code == 200:
        print(green(response.json()))
        time.sleep(x)
        user_request();
    else:
        print(red({"error": "Unable to fetch IP information."}))
        time.sleep(y)
        user_request();

@trademark 
def main():
    ip_address = input(green("Enter an IP address: "))
    info = get_ip_info(ip_address)
    print(green(info))
main();
