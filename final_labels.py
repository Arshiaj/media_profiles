import pandas as pd
import csv

def WriteDictToCSV(csv_file,csv_columns,dict_data):
    with open(csv_file, 'w', encoding="utf-8",newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in dict_data:
            writer.writerow(data)
    return 

x = input("Name?")

with open(x+"_data.csv", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    my_list=[]
    my_dict={}

    aljazeera = pd.read_csv(x+"_data.csv",names=["Entities","Label","Confidence","Count"], encoding="utf-8")
    for i in range(len(aljazeera)):
        name = aljazeera["Entities"][i]
        if name in my_dict:
            d = my_dict[name]
            label = aljazeera["Label"][i]
            d[label]+=1
            d["Count"]+=aljazeera["Count"][i]
#            d["Count"]+=1
        else:
            d = {"Entities":name,"neg":0,"pos":0,"neu":0,"Count":aljazeera["Count"][i]}
            label = aljazeera["Label"][i]
            d[label]+=1
            my_dict[name]=d
            print(aljazeera["Count"][i])
            
csv_columns = ['Entities','neg','pos','neu','Count']

myList=[]
for key in my_dict:
    myList+=[my_dict[key]]


WriteDictToCSV(x+"_count.csv",csv_columns,myList)
        
        
        
    
    
    

#    with open('flabels_count.csv', 'w',newline='') as csvfile:
#        writer = csv.DictWriter(csvfile,fieldnames=["entities","count","pos","neu","neg"])    
#        for row in reader:
                                    
#import csv
##import fileinput
#
#data = {}
#
#for row in csv.reader('entities_aljazeera.csv'):
#    values = [set(col.split(',')) for col in row]
#    for key in values.pop(0):   # Numbers in column 0
#        data[key] = [
#            new_col.union(old_col)
#            for new_col, old_col in zip(values, data.get(key, values))
#        ]
#
#for key, values in data.items():
#    print('\t'.join([key] + [','.join(col) for col in values]))