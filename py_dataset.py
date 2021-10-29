import json
from csv import DictWriter
import pandas as pd
import numpy
data = []
with open('dataset.jsonl') as f:
    for line in f:
        data.append(json.loads(line))
        

names = []
for x in data[0].keys():
    names.append(x)
    
names2 = tuple(names)

df = pd.DataFrame.from_dict(data)

print (df)

df.to_excel('players.xlsx')