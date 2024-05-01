from bs4 import BeautifulSoup
import requests
from csv import writer

url = "https://www.cbssports.com/nfl/stats/player/kick-returns/nfl/regular/qualifiers/"
result = requests.get(url)

doc = BeautifulSoup(result.content, "html.parser")
tbody = doc.find("tbody")
trs = tbody.find_all("tr")

id_counter = 1


with open('NFL-Kick_Returns.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['PlayerName', 'GamesPlayed', 'KickOffReturns', 'KickOffReturnYards', 'AverageYardsPerKickOffReturn', 'LongestKickOffReturn', 'KickOffReturnTouchdowns']
    thewriter.writerow(header)

    for tr in trs:
        tds = tr.find_all("td")
        if tds:
            # Extract data from each row
            PlayerName = tds[0].find("a").get_text(strip=True) if tds[0].find("a") else ''
            GamesPlayed = tds[1].get_text(strip=True)
            KickOffReturns = tds[2].get_text(strip=True)
            KickOffReturnYards = tds[3].get_text(strip=True)
            AverageYardsPerKickOffReturn = tds[4].get_text(strip=True)
            LongestKickOffReturn = tds[5].get_text(strip=True)
            KickOffReturnTouchdowns = tds[6].get_text(strip=True)
        

        # Write data to CSV file

        thewriter.writerow([id_counter, PlayerName, GamesPlayed, KickOffReturns, KickOffReturnYards, AverageYardsPerKickOffReturn, LongestKickOffReturn, KickOffReturnTouchdowns])

        id_counter += 1

