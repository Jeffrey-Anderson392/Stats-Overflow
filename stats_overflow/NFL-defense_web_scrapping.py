from bs4 import BeautifulSoup
import requests
from csv import writer

url = "https://www.cbssports.com/nfl/stats/player/defense/nfl/regular/qualifiers/"
result = requests.get(url)

doc = BeautifulSoup(result.content, "html.parser")
tbody = doc.find("tbody")
trs = tbody.find_all("tr")

id_counter = 1


with open('NFL-Defense.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['PlayerName', 'GamesPlayed', 'SoloTackles', 'AssistedTackles', 'TotalTackles', 'Interceptions', 'InterceptionYards', 'LongestInterceptions', 'InterceptionsReturnedForTouchdowns', 'ForcedFumbles', 'FumbleRecoveries', 'FumbleRecoveriesReturnedForTouchdowns', 'Sacks', 'PassesDefensed', 'Safties']
    thewriter.writerow(header)

    for tr in trs:
        tds = tr.find_all("td")
        if tds:
            # Extract data from each row
            PlayerName = tds[0].find("a").get_text(strip=True) if tds[0].find("a") else ''
            GamesPlayed = tds[1].get_text(strip=True)
            SoloTackles = tds[2].get_text(strip=True)
            AssistedTackles = tds[3].get_text(strip=True)
            TotalTackles = tds[4].get_text(strip=True)
            Interceptions = tds[5].get_text(strip=True)
            InterceptionYards = tds[6].get_text(strip=True)
            LongestInterception = tds[7].get_text(strip=True)
            InterceptionsReturnedForTouchdowns = tds[8].get_text(strip=True)
            ForcedFumbles = tds[9].get_text(strip=True)
            FumbleRecoveries = tds[10].get_text(strip=True)
            FumbleRecoveriesReturnedForTouchdowns = tds[11].get_text(strip=True)
            Sacks = tds[12].get_text(strip=True)
            PassesDefensed = tds[13].get_text(strip=True)
            Safeties = tds[14].get_text(strip=True)

        # Write data to CSV file

        thewriter.writerow([id_counter, PlayerName, GamesPlayed, SoloTackles, AssistedTackles, TotalTackles, Interceptions, InterceptionYards, LongestInterception, InterceptionsReturnedForTouchdowns, ForcedFumbles, FumbleRecoveries, FumbleRecoveriesReturnedForTouchdowns, Sacks, PassesDefensed, Safeties])

        id_counter += 1

