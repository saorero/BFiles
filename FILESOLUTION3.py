import sys
import os
import json
import math
from zipfile import ZipFile


if sys.version_info[0] < 3:
    print('This script requires Python 3 or higher')
    exit()

print('Welcome to the JSON Splitter')
print('First, enter the name of the file you want to split')

    # request file name
file_name = input('filename: ')
with open(f"{file_name}", "r") as f:
    f = open(file_name)
file_size = os.path.getsize(file_name)
data = json.load(f)
data_len = len(data)
print(f'The file {file_name} has {data_len} entries')
print('Valid JSON file found')
    # request chunk size
chunk_size = int(input('chunk size: '))





# get numeric input

mb_per_file = abs(float(input('Enter maximum file size (MB): ')))

if chunk_size > data_len:
    chunk_size = data_len
if chunk_size < 1:
    chunk_size = 1
if mb_per_file < 1:
    mb_per_file = 1


# check that file is larger than max size
    if file_size > mb_per_file * 1024 * 1024:
        print('File is too large to split')
        exit()


# calculate number of chunks
num_chunks = math.ceil(data_len / chunk_size)
print(f'Splitting {file_name} into {num_chunks} chunks')
print(f'Each chunk will be {mb_per_file}MB')

# create directory for chunks
if not os.path.exists('chunks'):
        os.makedirs('chunks')
else:
    print('chunks directory already exists')


# split file
for i in range(num_chunks):
    with open(f'chunks/{file_name}_{i+1}.json', 'w') as outfile:
        json.dump(data[i:(i+1)*chunk_size], outfile)
        print(f'{file_name}_{i+1}.json created')



# fix unshable type :slice error


# zip chunks
with ZipFile('chunks.zip', 'w') as zip:
    for file in os.listdir('chunks'):
        zip.write('chunks/' + file)
print('Chunks zipped into chunks.zip')
print('Done')
exit()

# if file is not large enough to split
if file_size < mb_per_file * 1024 * 1024:
    print('File is too small to split')
    exit()

# if file is not a valid JSON file
if not data:
    print('Invalid JSON file')
    exit()





