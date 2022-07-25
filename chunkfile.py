<<<<<<< HEAD
import fileinput as fi

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
=======
with open('C:\Spindles\data.json') as json_file:
    jsondata = json.load(json_file)
data_file = open('C:\Spindles\jsonoutput.csv', 'w', newline='')
csv_writer = csv.writer(data_file)
count = 0
for data in jsondata:
    if count == 0:
        header = data.keys()
        csv_writer.writerow(header)
        count += 1
    csv_writer.writerow(data.values())
data_file.close()
>>>>>>> fd5cd24e128b620c5cae6f0b2d83069d32e2d539
