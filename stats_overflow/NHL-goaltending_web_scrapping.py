from bs4 import BeautifulSoup
import requests
from csv import writer

url = "https://www.cbssports.com/nhl/stats/player/goaltending/nhl/regular/all-pos/qualifiers/"
result = requests.get(url)

doc = BeautifulSoup(result.content, "html.parser")
tbody = doc.find("tbody")
trs = tbody.find_all("tr")
id_counter = 1

with open('NHL-Goaltending.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['ID', 'PlayerName', 'GamesPlayed', 'GamesStarted', 'GoalsAgainstAverage', 'SavesPercentage', 'GoalsAgainst', 'ShotsAgainst', 'Wins', 'Losses', 'OvertimeLoss', 'Shutout', 'ShootoutGoalsMadeAndAttempted']
    thewriter.writerow(header)

    for tr in trs:
        tds = tr.find_all("td")
        if tds:
            # Extract data from each row
            PlayerName = tds[0].find("a").get_text(strip=True) if tds[0].find("a") else ''
            GamesPlayed = tds[1].get_text(strip=True)
            GamesStarted = tds[2].get_text(strip=True)
            GoalsAgainstAverage = tds[3].get_text(strip=True)
            SavesPercentage = tds[4].get_text(strip=True)
            GoalsAgainst = tds[5].get_text(strip=True)
            ShotsAgainst = tds[6].get_text(strip=True)
            Wins = tds[7].get_text(strip=True)
            Losses = tds[8].get_text(strip=True)
            OvertimeLoss = tds[9].get_text(strip=True)
            Shutout = tds[10].get_text(strip=True)
            ShootoutGoalsMadeAndAttempted = tds[11].get_text(strip=True)

        # Write data to CSV file
        thewriter.writerow([id_counter, PlayerName, GamesPlayed, GamesStarted, GoalsAgainstAverage, SavesPercentage, GoalsAgainst, ShotsAgainst, Wins, Losses, OvertimeLoss, Shutout, ShootoutGoalsMadeAndAttempted])

        id_counter += 1