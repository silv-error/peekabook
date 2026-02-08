import requests
from bs4 import BeautifulSoup
import re

def get_fb_name(url):
  headers = {
    "Host": "m.facebook.com",
    "Cookie": "datr=KhOIaROqhMHHt9PddRwnwRQ-; sb=KhOIad5SGuaS0gAMXle8QSwR; wd=1040x648; locale=en_US; fr=03YIKLNwhlLdZ2XDD..BpiBPL..AAA.0.0.BpiBWu.AWcdR_7afR8oqumXo1s611G5ZFw; ps_l=1; ps_n=1",
    "Dpr": "1",
    "Viewport-Width": "1040",
    "Sec-Ch-Ua": '"Not_A Brand";v="99", "Chromium";v="142"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Linux"',
    "Sec-Ch-Ua-Platform-Version": '""',
    "Sec-Ch-Ua-Model": '""',
    "Sec-Ch-Ua-Full-Version-List": "",
    "Sec-Ch-Prefers-Color-Scheme": "dark",
    "Accept-Language": "en-US,en;q=0.9",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "Accept-Encoding": "gzip, deflate, br",
    "Priority": "u=0, i"
  }

  response = requests.get(url, headers=headers)
  html_content = response.text

  soup = BeautifulSoup(html_content, "html.parser")
  div = soup.find("div", {"role": "dialog"})

  if div and div.has_attr("aria-label"):
      aria_label = div["aria-label"]
      match = re.search(r"See what (.*?) sent", aria_label)
      if match:
          return match.group(1)

  return None

