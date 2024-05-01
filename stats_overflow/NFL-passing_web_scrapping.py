from bs4 import BeautifulSoup
import requests
from csv import writer

url = "https://www.cbssports.com/nfl/stats/player/passing/nfl/regular/all/"
result = requests.get(url)

doc = BeautifulSoup(result.content, "html.parser")
tbody = doc.find("tbody")
trs = tbody.find_all("tr")
id_counter = 1

with open('NFL-Passing.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['ID', 'PlayerName','GamesPlayed', 'PassAttempts', 'PassCompletions', 'CompletionPercentages', 'PassingYards', 'PassingYardsPerGame', 'LongestCompletion', 'TouchdownPasses', 'Interceptions', 'TimesSacked', 'SackYardsLost']
    thewriter.writerow(header)

    for tr in trs:
        tds = tr.find_all("td")
        # Extract data from each row
        PlayerName = tds[0].find("a").get_text(strip=True)
        GamesPlayed = tds[1].get_text(strip=True)
        PassAttempts = tds[2].get_text(strip=True)
        PassCompletions = tds[3].get_text(strip=True)
        CompletionPercentage = tds[4].get_text(strip=True)
        PassingYards = tds[5].get_text(strip=True)
        PassingYardsPerGame = tds[6].get_text(strip=True)
        LongestCompletion = tds[7].get_text(strip=True)
        TouchdownPasses = tds[8].get_text(strip=True)
        Interceptions = tds[9].get_text(strip=True)
        TimesSacked = tds[10].get_text(strip=True)
        SackYardsLost = tds[11].get_text(strip=True)


        # Write data to CSV file
        thewriter.writerow([id_counter, PlayerName, GamesPlayed, PassAttempts, PassCompletions, CompletionPercentage, PassingYards, PassingYardsPerGame, LongestCompletion, TouchdownPasses, Interceptions, TimesSacked, SackYardsLost])

        id_counter += 1

#    PassAttempts[fixed_GP] = fixed_PA

#print(PassAttempts)
#print(doc.prettify())
#print(tags)
#print(tbody)