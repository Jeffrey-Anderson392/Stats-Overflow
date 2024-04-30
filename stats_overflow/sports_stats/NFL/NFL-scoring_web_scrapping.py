from bs4 import BeautifulSoup
import requests
from csv import writer

url = "https://www.cbssports.com/nfl/stats/player/scoring/nfl/regular/qualifiers/"
result = requests.get(url)

doc = BeautifulSoup(result.content, "html.parser")
tbody = doc.find("tbody")
trs = tbody.find_all("tr")

with open('NFL-scoring.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['PlayerName','GamesPlayed', 'RushingTouchdowns', 'ReceivingTouchdowns', 'PuntReturnTouchdowns', 'KickOffReturnedForTouchdowns', 'InterceptionsReturnedForTouchdowns', 'FumbleRecoveriesReturnedForTouchdowns', 'FieldGoals', 'ExtraPoints', 'Safeties', 'TwoPointConversions', 'TotalPoints', 'PointsPerGame']
    thewriter.writerow(header)

    for tr in trs:
        tds = tr.find_all("td")
        # Extract data from each row
        PlayerName = tds[0].find("a").get_text(strip=True)
        GamesPlayed = tds[1].get_text(strip=True)
        RushingTouchdowns = tds[2].get_text(strip=True)
        ReceivingTouchdowns = tds[3].get_text(strip=True)
        PuntReturnTouchdowns = tds[4].get_text(strip=True)
        KickOffReturnedTouchdowns = tds[5].get_text(strip=True)
        InterceptionsReturnedForTouchdowns = tds[6].get_text(strip=True)
        FumbleRecoveriesReturnedForTouchdowns = tds[7].get_text(strip=True)
        FieldGoals = tds[8].get_text(strip=True)
        ExtraPoints = tds[9].get_text(strip=True)
        Safeties = tds[10].get_text(strip=True)
        TwoPointConversions = tds[11].get_text(strip=True)
        TotalPoints = tds[12].get_text(strip=True)
        PointsPerGame = tds[13].get_text(strip=True)

        # Write data to CSV file
        thewriter.writerow([PlayerName, GamesPlayed, RushingTouchdowns, ReceivingTouchdowns, PuntReturnTouchdowns, KickOffReturnedTouchdowns, InterceptionsReturnedForTouchdowns, FumbleRecoveriesReturnedForTouchdowns, FieldGoals, ExtraPoints, Safeties, TwoPointConversions, TotalPoints, PointsPerGame])