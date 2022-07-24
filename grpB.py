
#converting Json to csv
import json
import csv


with open("generated.json", "r") as f:
    data = json.load(f)
    profile = data["profile"]

with open("generated.csv", "w" ,newline="") as f:
    fieldnames = profile[0].keys()
    writer = csv.DictWriter( f, fieldnames=fieldnames)#creates the header
    writer.writeheader()

    for name in profile:
        writer.writerow(name)


#CSV to JSON

