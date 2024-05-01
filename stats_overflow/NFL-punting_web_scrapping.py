from bs4 import BeautifulSoup
import requests
from csv import writer

url = "https://www.cbssports.com/nfl/stats/player/punting/nfl/regular/qualifiers/"
result = requests.get(url)

doc = BeautifulSoup(result.content, "html.parser")
tbody = doc.find("tbody")
trs = tbody.find_all("tr")

id_counter = 1


with open('NFL-Punting.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['ID', 'PlayerName', 'GamesPlayed', 'Punts', 'PuntingYards', 'LongestPunts', 'AverageYardsPerPunt', 'NetPuntingAverage', 'PuntsInside20', 'Touchbacks', 'PuntsResultingInAFairCatch', 'PuntsReturned', 'PuntReturnYardsAgainst', 'AverageYardsPerPuntReturn', 'PuntsBlocked']
    thewriter.writerow(header)

    for tr in trs:
        tds = tr.find_all("td")
        if tds:
            # Extract data from each row
            PlayerName = tds[0].find("a").get_text(strip=True) if tds[0].find("a") else ''
            GamesPlayed = tds[1].get_text(strip=True)
            Punts = tds[2].get_text(strip=True)
            PuntingYards = tds[3].get_text(strip=True)
            LongestPunts = tds[4].get_text(strip=True)
            AverageYardsPerPunt = tds[5].get_text(strip=True)
            NetPuntingAverage = tds[6].get_text(strip=True)
            PuntsInside20 = tds[7].get_text(strip=True)
            Touchbacks = tds[8].get_text(strip=True)
            PuntsResultingInAFairCatch = tds[9].get_text(strip=True)
            PuntsReturned = tds[10].get_text(strip=True)
            PuntReturnYardsAgainst = tds[11].get_text(strip=True)
            AverageYardsPerPuntReturn = tds[12].get_text(strip=True)
            PuntsBlocked = tds[13].get_text(strip=True)

        

        # Write data to CSV file

        thewriter.writerow([id_counter, PlayerName, GamesPlayed, Punts, PuntingYards, LongestPunts, AverageYardsPerPunt, NetPuntingAverage, PuntsInside20, Touchbacks, PuntsResultingInAFairCatch, PuntsReturned, PuntReturnYardsAgainst, AverageYardsPerPuntReturn, PuntsBlocked])
        
        id_counter += 1
