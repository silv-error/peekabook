import requests

def get_location_url(url):
  headers = {
    "Host": "www.facebook.com",
    "Cookie": "datr=iYXKaFjl9KXNCgPGmTIVtIdh; sb=sIXKaDxEv07EQIBFhuLZijhF; ps_l=1; ps_n=1; locale=en_US; wd=1918x798; fr=04pNrlWHaIKGUor6F..Boyobb..AAA.0.0.Bo0iy9.AWfDrjnvmGEjuUH-5uqMD-xJndQ",
    "Dpr": "1",
    "Viewport-Width": "1918",
    "Sec-Ch-Ua": "\"Chromium\";v=\"139\", \"Not;A=Brand\";v=\"99\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Linux\"",
    "Sec-Ch-Ua-Platform-Version": "\"\"",
    "Sec-Ch-Ua-Model": "\"\"",
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

  response = requests.get(url, headers=headers, allow_redirects=False)
  location = response.headers.get("Location")
  
  return location