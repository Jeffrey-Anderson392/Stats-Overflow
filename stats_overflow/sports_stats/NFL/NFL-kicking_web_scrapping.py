from bs4 import BeautifulSoup
import requests
from csv import writer

url = "https://www.cbssports.com/nfl/stats/player/kicking/nfl/regular/qualifiers/"
result = requests.get(url)

doc = BeautifulSoup(result.content, "html.parser")
tbody = doc.find("tbody")
trs = tbody.find_all("tr")

with open('NFL-Kicking.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Name', 'GP', 'FGM', 'FGP', 'LFG', 'YRDG', 'EXPM', 'EXP', 'KP']
    thewriter.writerow(header)

    for tr in trs:
        tds = tr.find_all("td")
        # Extract data from each row
        PlayerName = tds[0].find("a").get_text(strip=True) if tds[0].find("a") else 'No Name'
        GamesPlayed = tds[1].get_text(strip=True)
        FieldGoalsMade = tds[2].get_text(strip=True)
        FieldGoalPercentge = tds[3].get_text(strip=True)
        LongestFieldGoal = tds[4].get_text(strip=True)
        ExtraPointsMade = tds[5].get_text(strip=True)
        ExtraPointPercentage = tds[6].get_text(strip=True)
        KickingPoints = tds[7].get_text(strip=True)

        # Write data to CSV file
        thewriter.writerow([PlayerName, GamesPlayed, FieldGoalsMade, FieldGoalPercentge, LongestFieldGoal, ExtraPointsMade, ExtraPointPercentage, KickingPoints])