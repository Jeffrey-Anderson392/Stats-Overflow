from bs4 import BeautifulSoup
import requests
from csv import writer

url = "https://www.cbssports.com/nfl/stats/player/passing/nfl/regular/all/"
result = requests.get(url)

doc = BeautifulSoup(result.content, "html.parser")
tbody = doc.find("tbody")
trs = tbody.find_all("tr")

with open('Passing.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Name','GP', 'PA', 'PC']
    thewriter.writerow(header)

    for tr in trs:
        tds = tr.find_all("td")
        # Extract data from each row
        PlayerName = tds[0].find("a").get_text(strip=True)
        GamesPlayed = tds[1].get_text(strip=True)
        PassAttempts = tds[2].get_text(strip=True)
        PassCompletions = tds[3].get_text(strip=True)

        # Write data to CSV file
        thewriter.writerow([PlayerName, GamesPlayed, PassAttempts, PassCompletions])

#    PassAttempts[fixed_GP] = fixed_PA

#print(PassAttempts)
#print(doc.prettify())
#print(tags)
#print(tbody)