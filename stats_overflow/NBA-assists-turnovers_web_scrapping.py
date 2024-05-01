from bs4 import BeautifulSoup
import requests
from csv import writer

url = "https://www.cbssports.com/nba/stats/player/assists-turnovers/nba/regular/all-pos/qualifiers/"
result = requests.get(url)

doc = BeautifulSoup(result.content, "html.parser")
tbody = doc.find("tbody")
trs = tbody.find_all("tr")

with open('NBA-Assists-Turnovers.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['PlayerName', 'GamesPlayed', 'GamesStarted', 'TotalAssists', 'AssistsPerGame', 'Turnover', 'TurnoversPerGame', 'AssistsPerTurnover']
    thewriter.writerow(header)
    id_counter =1

    for tr in trs:
        tds = tr.find_all("td")
        if tds:
            # Extract data from each row
            PlayerName = tds[0].find("a").get_text(strip=True) if tds[0].find("a") else ''
            GamesPlayed = tds[1].get_text(strip=True)
            GamesStarted = tds[2].get_text(strip=True)
            TotalAssists = tds[3].get_text(strip=True)
            AssistsPerGame = tds[4].get_text(strip=True)
            Turnovers = tds[5].get_text(strip=True)
            TurnoversPerGame = tds[6].get_text(strip=True)
            AssistsPerTurnover = tds[7].get_text(strip=True)


        # Write data to CSV file
        thewriter.writerow([id_counter, PlayerName, GamesPlayed, GamesStarted, TotalAssists, AssistsPerGame, Turnovers, TurnoversPerGame, AssistsPerTurnover])

        id_counter += 1