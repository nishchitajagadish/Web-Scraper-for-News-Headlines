# scraper.py
# Simple News Headlines Scraper

import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com"   # change to any news site
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})

soup = BeautifulSoup(response.text, "html.parser")

headlines = []
for tag in soup.find_all("h2"):
    text = tag.get_text(strip=True)
    if text:
        headlines.append(text)

with open("headlines.txt", "w", encoding="utf-8") as f:
    for h in headlines:
        f.write(h + "\n")

print(f"Saved {len(headlines)} headlines to headlines.txt")
