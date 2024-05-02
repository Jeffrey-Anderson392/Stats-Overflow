from bs4 import BeautifulSoup
import requests
from csv import writer

url = "https://www.vlr.gg/stats"
result = requests.get(url)

doc = BeautifulSoup(result.content, "html.parser")
tbody = doc.find("tbody")
trs = tbody.find_all("tr")

id_counter = 1


with open('Valorant-Player.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['ID', 'PlayerName', 'Agents', 'RoundsPlayed', 'Rating', 'AverageCombatScore', 'KillsToDeaths', 'KillAssistsPercentage', 'AverageDamagePerRound', 'KillPerRound', 'AssistsPerRound', 'FirstKillsPerRound', 'FirstDeathPerRound', 'HeadShotPercentage', 'ClutchSuccessRate', 'Clutches', 'MaxKillsInAMap', 'Kills', 'Deaths', 'Assists', 'FirstKills', 'FirstDeaths']
    thewriter.writerow(header)

    for tr in trs:
        tds = tr.find_all("td")
        if tds:
            # Extract data from each row
            PlayerName = tds[0].find("a").get_text(strip=True) if tds[0].find("a") else ''
            Agents = tds[1].get_text(strip=True)
            RoundsPlayed = tds[2].get_text(strip=True)
            Rating = tds[3].get_text(strip=True)
            AverageCombatScore = tds[4].get_text(strip=True)
            KillsToDeaths = tds[5].get_text(strip=True)
            KillAssistsPercentage = tds[6].get_text(strip=True)
            AverageDamagePerRound = tds[7].get_text(strip=True)
            KillPerRound = tds[8].get_text(strip=True)   
            AssistsPerRound = tds[9].get_text(strip=True)
            FirstKillsPerRound = tds[10].get_text(strip=True)
            FirstDeathPerRound = tds[11].get_text(strip=True)
            HeadShotPercentage = tds[12].get_text(strip=True)
            ClutchSuccessRate = tds[13].get_text(strip=True)
            Clutches = tds[14].get_text(strip=True)
            MaxKillsInAMap = tds[15].get_text(strip=True)
            Kills = tds[16].get_text(strip=True)
            Deaths = tds[17].get_text(strip=True)
            Assists = tds[18].get_text(strip=True)
            FirstKills = tds[19].get_text(strip=True)
            FirstDeaths = tds[20].get_text(strip=True)


        # Write data to CSV file

        thewriter.writerow([id_counter, PlayerName, Agents, RoundsPlayed, Rating, AverageCombatScore, KillsToDeaths, KillAssistsPercentage, AverageDamagePerRound, KillPerRound, AssistsPerRound, FirstKillsPerRound, FirstDeathPerRound, HeadShotPercentage, ClutchSuccessRate, Clutches, MaxKillsInAMap, Kills, Deaths, Assists, FirstKills, FirstDeaths])

        id_counter += 1

