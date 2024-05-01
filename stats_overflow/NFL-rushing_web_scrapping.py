from bs4 import BeautifulSoup
import requests
from csv import writer

url = "https://www.cbssports.com/nfl/stats/player/rushing/nfl/regular/qualifiers/"
result = requests.get(url)

doc = BeautifulSoup(result.content, "html.parser")
tbody = doc.find("tbody")
trs = tbody.find_all("tr")

id_counter = 1


with open('NFL-Rushing.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['PlayerName','GamesPlayed', 'RushingAttempts', 'RushingYards', 'RushingYardsPerGame', 'AverageYardsPerRush', 'RushingTouchdowns', 'LongestRush']
    thewriter.writerow(header)

    for tr in trs:
        tds = tr.find_all("td")
        # Extract data from each row
        PlayerName = tds[0].find("a").get_text(strip=True)
        GamesPlayed = tds[1].get_text(strip=True)
        RushingAttempts = tds[2].get_text(strip=True)
        RushingYards = tds[3].get_text(strip=True)
        RushingYardsPerGame = tds[4].get_text(strip=True)
        AverageYardsPerRush = tds[5].get_text(strip=True)
        RushingTouchdowns = tds[6].get_text(strip=True)
        LongestRush = tds[7].get_text(strip=True)

        # Write data to CSV file

        thewriter.writerow([id_counter, PlayerName, GamesPlayed, RushingAttempts, RushingYards, RushingYardsPerGame, AverageYardsPerRush, RushingTouchdowns, LongestRush])

        id_counter += 1

