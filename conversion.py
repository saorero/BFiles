import json
import csv

with open("convert.csv", "r") as f:
    reader = csv.reader(f)

    next(reader)#skips the header
    data = {"names": []}
    for row in reader:
        data["names"].append({"firstname":
         row[0], "age": row[1]})

with open("names.json", "w") as f:
    json.dump(data, f, indent=8)