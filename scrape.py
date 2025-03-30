"""
Author: Trevor Corcoran
License: MIT License
"""

from bs4 import BeautifulSoup as bs
import urllib.request

def scrape(url):
    # Scrapes a specific URL
    try:
        html_download = urllib.request.urlopen(url).read()
    except:
        return None

    soup = bs(html_download, "html.parser")

    print(soup.prettify())


if __name__ == "__main__":
    scrape("https://www.trevorcorc.com/")

