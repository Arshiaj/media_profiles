import pandas as pd
from newspaper import Article
import csv

x = input("NAME?")
f = pd.read_csv("../fnc-1-baseline/fnc-1/"+x+"_qatar.csv",names=["URL","MobileURL","Date","Title"], encoding="utf-8")

with open("../fnc-1-baseline/fnc-1/"+x+"_bodies.csv", 'w',newline='', encoding="utf-8") as csvfile:
    ID=0
    writer = csv.DictWriter(csvfile,fieldnames=["Body ID","articleBody"])
    writer.writeheader()
    for i in range(len(f)):
        url = f["URL"][i]
        article1=Article(link)
        article1.download()
        article1.parse()
        a=article1.text
        writer.writerow({"Body ID":ID,"articleBody":a})
        ID+=1
