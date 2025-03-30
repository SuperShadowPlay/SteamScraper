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

    result = {}

    # Game title
    title = soup.find("div", id="appHubAppName", class_="apphub_AppName").text.strip()
    result.update({"title" : title})

    # Tags
    tags = []
    
    tag_list = soup.find_all('a', {'class': 'app_tag'})
    
    if tag_list:
        if len(tag_list) > 1:
            for tag in tag_list:
                tags.append(tag.text.strip())

    result.update({"tags" : tags})

    return result
    

if __name__ == "__main__":
    result = scrape("https://store.steampowered.com/app/440/")

    print(result["title"])
    print(result["tags"])
