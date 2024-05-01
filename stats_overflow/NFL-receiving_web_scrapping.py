from bs4 import BeautifulSoup
import requests
from csv import writer

url = "https://www.cbssports.com/nfl/stats/player/receiving/nfl/regular/qualifiers/"
result = requests.get(url)

doc = BeautifulSoup(result.content, "html.parser")
tbody = doc.find("tbody")
trs = tbody.find_all("tr")

id_counter = 1


with open('NFL-Receiving.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['PlayerName','GamesPlayed', 'Receptions', 'ReceivingYards', 'ReceivingYardsPerGame', 'AverageYardsPerReception', 'LongestReception', 'ReceivingTouchdowns']
    thewriter.writerow(header)

    for tr in trs:
        tds = tr.find_all("td")
        # Extract data from each row
        PlayerName = tds[0].find("a").get_text(strip=True)
        GamesPlayed = tds[1].get_text(strip=True)
        Receptions = tds[2].get_text(strip=True)
        ReceivingYards = tds[3].get_text(strip=True)
        ReceivingYardsPerGame = tds[4].get_text(strip=True)
        AverageYardsPerReception = tds[5].get_text(strip=True)
        LongestReception = tds[6].get_text(strip=True)
        ReceivingTouchdowns = tds[7].get_text(strip=True)

        # Write data to CSV file

        thewriter.writerow([id_counter, PlayerName, GamesPlayed, Receptions, ReceivingYards, ReceivingYardsPerGame, AverageYardsPerReception, LongestReception, ReceivingTouchdowns])

        id_counter += 1

