import json
import csv
x=input("Name?")
f=open(x+"_data.txt")
data=f.readlines()
with open(x+"_data.csv", 'w',newline='', encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile,fieldnames=["Entities","Labels","Confidence","Count"])
    for i in data:
        
        d = json.loads(i)
        for x in range(len(d['entities'])):
            en=d['entities'][x]['normalized']
            l=d['entities'][x]['sentiment']['label']
            confi=d['entities'][x]['sentiment']['confidence']*100
            count=d['entities'][x]['count']
            writer.writerow({"Entities":en,"Labels":l,"Confidence":confi,"Count":count})
        
    f.close()
    //hello Kritika
