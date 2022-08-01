# converts Json file to csv file and writes it to a new file
import os
import csv

import json
from urllib import request
from zipfile import ZipFile


# gets file name from user
def get_file_name():
    file_name = input('filename: ')
    return file_name


""""
@apps.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # 'file-name' is the file name here
        if 'file-name' not in request.files:
            flash('No file part')
            return 'no file found'
        file = request.files['file-name']
    return file
"""

filename = get_file_name()


with open(f'{filename}') as json_file:
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
