from bs4 import BeautifulSoup
import requests
from csv import writer

url = "https://www.cbssports.com/nhl/stats/player/scoring/nhl/regular/all-pos/qualifiers/"
result = requests.get(url)

doc = BeautifulSoup(result.content, "html.parser")
tbody = doc.find("tbody")
trs = tbody.find_all("tr")

id_counter += 1


with open('NHL-Scoring.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['PlayerName', 'GamesPlayed', 'Goals', 'Assists', 'Points', 'PlusMinusGoalsScoredForOrAgainstTotal', 'PenaltyMinutes', 'PowerPlayGoals', 'PowerPlayAssists', 'ShortHandedGoals', 'OverTimeGoals', 'GameWinningGoals', 'ShortHandedAssists', 'ShotsOnGoal', 'ShotsOnGoalPercentage', 'TimeOnIcePerGame', 'ShootoutGoalsMadeAndAttempted']
    thewriter.writerow(header)

    for tr in trs:
        tds = tr.find_all("td")
        if tds:
            # Extract data from each row
            PlayerName = tds[0].find("a").get_text(strip=True) if tds[0].find("a") else ''
            GamesPlayed = tds[1].get_text(strip=True)
            Goals = tds[2].get_text(strip=True)
            Assists = tds[3].get_text(strip=True)
            Points = tds[4].get_text(strip=True)
            PlusMinusGoalsScoredForOrAgainstTotal = tds[5].get_text(strip=True)
            PenaltyMinutes = tds[6].get_text(strip=True)
            PowerPlayGoals = tds[7].get_text(strip=True)
            PowerPlayAssists = tds[8].get_text(strip=True)
            ShortHandedGoals = tds[9].get_text(strip=True)
            OverTimeGoals = tds[10].get_text(strip=True)
            GameWinningGoals = tds[11].get_text(strip=True)
            ShortHandedAssists = tds[12].get_text(strip=True)
            ShotsOnGoal = tds[13].get_text(strip=True)
            ShotsOnGoalPercentage = tds[14].get_text(strip=True)
            TimeOnIcePerGame = tds[15].get_text(strip=True)
            ShootoutGoalsMadeAndAttempted = tds[16].get_text(strip=True)

        

        # Write data to CSV file

        thewriter.writerow([id_counter, PlayerName, GamesPlayed, Goals, Assists, Points, PlusMinusGoalsScoredForOrAgainstTotal, PenaltyMinutes, PowerPlayGoals, PowerPlayAssists, ShortHandedGoals, OverTimeGoals, GameWinningGoals, ShortHandedAssists, ShotsOnGoal, ShotsOnGoalPercentage, TimeOnIcePerGame, ShootoutGoalsMadeAndAttempted])

        id_counter += 1
