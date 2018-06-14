import requests
import json
from newspaper import Article
import csv





#get page
response = requests.get("https://api.gdeltproject.org/api/v2/doc/doc?query=domain:aljazeera.com%20qatar%20blockade&sourcelang:english&maxrecords=250&format=json&startdatetime=20170106000000&enddatetime=20180611000000")
data = response.json()


articles = data['articles']

with open("../fnc-1-baseline/fnc-1/aljazeera_blockade_bodies.csv", 'w',newline='', encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile,fieldnames=["Body ID","articleBody"])
    writer.writeheader()
    ID=0
    for i in articles:
        #i = articles[0]
            link = i['url']
        #    print(link)
            article1=Article(link)
            article1.download()
            article1.parse()
            a=article1.text
            writer.writerow({"Body ID":ID,"articleBody":a})
            ID+=1
        #    article1.nlp()
        #    print(article1.keywords)
    