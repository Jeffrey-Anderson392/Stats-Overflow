from bs4 import BeautifulSoup
import requests
from csv import writer

url = "https://www.cbssports.com/nfl/stats/player/punt-returns/nfl/regular/qualifiers/"
result = requests.get(url)

doc = BeautifulSoup(result.content, "html.parser")
tbody = doc.find("tbody")
trs = tbody.find_all("tr")

with open('NFL-Punt_Returns.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['ID', 'PlayerName', 'GamesPlayed', 'PuntReturns', 'PuntReturnYards', 'AverageYardsPerPuntReturn', 'LongestPuntReturn', 'PuntReturnTouchdowns', 'FairCatches']
    thewriter.writerow(header)

    for tr in trs:
        tds = tr.find_all("td")
        if tds:
            # Extract data from each row
            PlayerName = tds[0].find("a").get_text(strip=True) if tds[0].find("a") else ''
            GamesPlayed = tds[1].get_text(strip=True)
            PuntReturns = tds[2].get_text(strip=True)
            PuntReturnYards = tds[3].get_text(strip=True)
            AverageYardsPerPuntReturn = tds[4].get_text(strip=True)
            LongestPuntReturn = tds[5].get_text(strip=True)
            PuntReturnTouchdowns = tds[6].get_text(strip=True)
            FairCatches = tds[7].get_text(strip=True)
        

        # Write data to CSV file
        thewriter.writerow([1, PlayerName, GamesPlayed, PuntReturns, PuntReturnYards, AverageYardsPerPuntReturn, LongestPuntReturn, PuntReturnTouchdowns, FairCatches])