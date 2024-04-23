#!/usr/bin/env python3
import json

file = open('ex5.json', 'r')
sample = json.load(file)
file.close()  

for i in sample:
    if i["name"] == "Old Fashioned" and i["type"] == "donut": 
        i["batters"]["batter"].append({"id": "1005", "type": "Tea"})
        break

file = open('ex5.json', 'w')
json.dump(sample, file, indent=2)
file.close()  
