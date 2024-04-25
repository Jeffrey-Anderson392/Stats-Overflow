from bs4 import BeautifulSoup
import requests
from csv import writer

url = "https://www.cbssports.com/nba/stats/player/steals/nba/regular/all-pos/qualifiers/"
result = requests.get(url)

doc = BeautifulSoup(result.content, "html.parser")
tbody = doc.find("tbody")
trs = tbody.find_all("tr")

with open('NBA-Blocks.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Name', 'GP', 'GS', 'BLK', 'BPG']
    thewriter.writerow(header)

    for tr in trs:
        tds = tr.find_all("td")
        if tds:
            # Extract data from each row
            PlayerName = tds[0].find("a").get_text(strip=True) if tds[0].find("a") else ''
            GamesPlayed = tds[1].get_text(strip=True)
            GamesStarted = tds[2].get_text(strip=True)
            TotalBlocks = tds[3].get_text(strip=True)
            BlocksPerGame = tds[4].get_text(strip=True)


        # Write data to CSV file
        thewriter.writerow([PlayerName, GamesPlayed, GamesStarted, TotalBlocks, BlocksPerGame])