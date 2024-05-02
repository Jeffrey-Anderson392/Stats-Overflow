from bs4 import BeautifulSoup
import requests
from csv import writer

url = "https://www.cbssports.com/nba/stats/player/scoring/nba/regular/all-pos/qualifiers/"
result = requests.get(url)

doc = BeautifulSoup(result.content, "html.parser")
tbody = doc.find("tbody")
trs = tbody.find_all("tr")

id_counter = 1


with open('NBA-Scoring.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['ID', 'Name', 'GamesPlayed', 'GamesStarted', 'MinutesPerGame', 'PointsPerGame', 'FieldGoalsMade', 'FieldGoalsAttempted', 'FieldGoalPercentage', 'ThreePointFieldGoalsMade', 'ThreePointFieldGoalsAttempted', 'ThreePointFieldGoalPercentage', 'FreeThrowsMade', 'FreeThrowsAttempted', 'FreeThrowsPercentage']
    thewriter.writerow(header)

    for tr in trs:
        tds = tr.find_all("td")
        if tds:
            # Extract data from each row
            PlayerName = tds[0].find("a").get_text(strip=True) if tds[0].find("a") else ''
            GamesPlayed = tds[1].get_text(strip=True)
            GamesStarted = tds[2].get_text(strip=True)
            MinutesPerGame = tds[3].get_text(strip=True)
            PointsPerGame = tds[4].get_text(strip=True)
            FieldGoalsMade = tds[5].get_text(strip=True)
            FieldGoalsAttempted = tds[6].get_text(strip=True)
            FieldGoalPercentage = tds[7].get_text(strip=True)
            ThreePointFieldGoalsMade = tds[8].get_text(strip=True)   
            ThreePointFieldGoalsAttempted = tds[9].get_text(strip=True)
            ThreePointFieldGoalPercentage = tds[10].get_text(strip=True)
            FreeThrowsMade = tds[11].get_text(strip=True)
            FreeThrowsAttempted = tds[12].get_text(strip=True)
            FreeThrowPerentage = tds[13].get_text(strip=True)


        # Write data to CSV file

        thewriter.writerow([id_counter, PlayerName, GamesPlayed, GamesStarted, MinutesPerGame, PointsPerGame, FieldGoalsMade, FieldGoalsAttempted, FieldGoalPercentage, ThreePointFieldGoalsMade, ThreePointFieldGoalsAttempted, ThreePointFieldGoalPercentage, FreeThrowsMade, FreeThrowsAttempted, FreeThrowPerentage])

        id_counter += 1

