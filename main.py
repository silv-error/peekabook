import sys
import argparse
import requests
from colorama import Fore, Style, init
from get_location_url import get_location_url
from get_fb_name import get_fb_name

# Initialize colorama
init(autoreset=True)

VERSION = "1.0"
AUTHOR = "silv"

BANNER = r"""
   ______     ______     ______     __                            
  /\  == \   /\  ___\   /\  ___\   /\ \                           
  \ \  __<   \ \  __\   \ \  __\   \ \ \____                      
   \ \_\ \_\  \ \_____\  \ \_____\  \ \_____\                     
    \/_/ /_/   \/_____/   \/_____/   \/_____/                     

   ______   ______     ______     __  __     ______     ______    
  /\  == \ /\  ___\   /\  ___\   /\ \/ /    /\  ___\   /\  == \   
  \ \  _-/ \ \  __\   \ \  __\   \ \  _"-.  \ \  __\   \ \  __<   
   \ \_\    \ \_____\  \ \_____\  \ \_\ \_\  \ \_____\  \ \_\ \_\ 
    \/_/     \/_____/   \/_____/   \/_/\/_/   \/_____/   \/_/ /_/ 
                            
                                                  REEL PEEKER v{version}
                                                  Author: {author}
""".format(version=VERSION, author=AUTHOR)
print(Fore.CYAN + BANNER + Style.RESET_ALL)

def main():
    parser = argparse.ArgumentParser(description="Extract Facebook Full Name from a shared reel or post.")
    parser.add_argument("--url", help="Facebook shared reel/post URL")
    args = parser.parse_args()

    try:
        # Input URL
        url = args.url or input(Fore.YELLOW + "Enter shared reel: " + Style.RESET_ALL).strip()
        if not url:
            print(Fore.RED + "[!] No URL provided. Exiting.")
            sys.exit(1)

        print(Fore.CYAN + "[*] Retrieving the FB name of the user...")

        # Process
        location_url = get_location_url(url)
        victim_name = get_fb_name(location_url)

        if not victim_name:
            print(Fore.RED + "[!] Shared post probably deleted or link expired. Try another one.")
            return

        # Success output
        print(Fore.GREEN + "[+] FB Name Found: " + Fore.WHITE + victim_name)

        # Save result
        with open("results.txt", "a", encoding="utf-8") as f:
            f.write(f"{url} -> {victim_name}\n")

        print(Fore.CYAN + f"[*] Saved to results.txt")

    except KeyboardInterrupt:
        print(Fore.RED + "\n[!] Interrupted by user. Exiting...")
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"[!] Network error: {e}")
        sys.exit(1)
    except Exception as e:
        print(Fore.RED + f"[!] Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
  while True:
    main()
