from bs4 import BeautifulSoup
import requests

url = "https://www.cbssports.com/nfl/stats/player/passing/nfl/regular/all/"

result = requests.get(url)

my_data = []

doc = BeautifulSoup(result.text, "html.parser")
articles = doc.select('a.post-card')

tags = doc.find_all(class_="TableBase-bodyTd TableBase-bodyTd--number")

tbody = doc.tbody
trs = tbody.contents

for tr in trs:
    GamesPlayed, PassAttempts = tr.contents[1:3]
    fixed_GP = GamesPlayed.string
    fixed_PA = PassAttempts.string

#    PassAttempts[fixed_GP] = fixed_PA

#print(PassAttempts)
    

for articles in articles:

    title = rticle.select('.card-title')[0].get_text()
    excerpt = article.select('card-text')[0].get_text()
    pub_date = article.select('.card-footer small')[0],get_text()


    my_data.append({"title": title, "excerpt": excerpt, "pub_date": pub_date})

#print(doc.prettify())
#print(tags)
#print(tbody)