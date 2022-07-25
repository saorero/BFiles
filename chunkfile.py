
import csv
import fileinput as fi
import json

with open('file') as json_file:
    jsondata = json.load(json_file)
data_file = open('file.csv', 'w', newline='')
csv_writer = csv.writer(data_file)
count = 0
for data in jsondata:
    if count == 0:
        header = data.keys()
        csv_writer.writerow(header)
        count += 1
    csv_writer.writerow(data.values())
data_file.close()
