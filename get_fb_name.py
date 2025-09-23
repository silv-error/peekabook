import requests
from bs4 import BeautifulSoup
import re

def get_fb_name(url):
    headers = {
        "Host": "m.facebook.com",
        "Cookie": "datr=iYXKaFjl9KXNCgPGmTIVtIdh; sb=sIXKaDxEv07EQIBFhuLZijhF; ps_l=1; ps_n=1; locale=en_US; fr=04pNrlWHaIKGUor6F..Boyobb..AAA.0.0.Bo0kGJ.AWeJtUGOzfyZLve5STOWyFrlZTo; wd=1908x788",
        "Accept-Language": "en-US,en;q=0.9",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Dpr": "1",
        "Viewport-Width": "1908",
        "Sec-Ch-Ua": "\"Chromium\";v=\"139\", \"Not;A=Brand\";v=\"99\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Linux\"",
        "Sec-Ch-Prefers-Color-Scheme": "dark",
        "Accept-Encoding": "identity", # forcing server to send plain text
        "Priority": "u=0, i"
    }

    # Just fetch normally, Requests will decode plain text
    resp = requests.get(url, headers=headers, allow_redirects=False)
    resp.encoding = resp.encoding or "utf-8"
    body_text = resp.text

    # Parse HTML
    soup = BeautifulSoup(body_text, "html.parser")
    div = soup.find("div", {"role": "dialog"})

    if div and div.has_attr("aria-label"):
        aria_label = div["aria-label"]
        match = re.search(r"See what (.*?) sent", aria_label)
        if match:
            return match.group(1)

    return None
