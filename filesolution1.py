import json
import sys


with open(sys.argv[1], 'r') as infile:  # instead of f = open('data.json',)
    # returns JSON object as a dictionary
    jsonFile = json.load(infile)
    # Set Chunk size per file
    chunkSize = 1400
    # Iterating through the json list
    for i in range(0, len(jsonFile), chunkSize):  # xrange is obsolete
        with open(sys.argv[1] + '_' + str(i//chunkSize) + '.json', 'w') as outfile:
            json.dump(jsonFile[i:i+chunkSize], outfile)(edited)
