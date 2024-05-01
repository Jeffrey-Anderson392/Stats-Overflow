from bs4 import BeautifulSoup
import requests
from csv import writer

url = "https://www.cbssports.com/nhl/stats/player/penalties/nhl/regular/all-pos/qualifiers/"
result = requests.get(url)

doc = BeautifulSoup(result.content, "html.parser")
tbody = doc.find("tbody")
trs = tbody.find_all("tr")

id_counter = 1


with open('NHL-penalties.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['ID', 'PlayerName', 'GamesPlayed', 'PenaltyMinutes', 'MajorPenalties', 'MinorPenalties']
    thewriter.writerow(header)

    for tr in trs:
        tds = tr.find_all("td")
        if tds:
            # Extract data from each row
            PlayerName = tds[0].find("a").get_text(strip=True) if tds[0].find("a") else ''
            GamesPlayed = tds[1].get_text(strip=True)
            PenaltyMinutes = tds[2].get_text(strip=True)
            MajorPenalties = tds[3].get_text(strip=True)
            MinorPenalties = tds[4].get_text(strip=True)


        # Write data to CSV file

        thewriter.writerow([id_counter, PlayerName, GamesPlayed, PenaltyMinutes, MajorPenalties, MinorPenalties])

        id_counter += 1

