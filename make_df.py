import os
import json
from os.path import join as pjoin

directory = os.path.join(os.path.dirname(__file__), "names")
savepath = os.path.join(os.path.dirname(__file__), "reference", "data.json")

names = []
targets = []

def process_names(lines):
    for line in lines:
        parts = line.split(',')
        names.append(parts[0].lower())
        targets.append(parts[1] == 'M' and 1 or 0)

files = [f for f in os.listdir(directory) if f.endswith(".txt")]

for entry in files:
    name_file = open(os.path.join(directory,entry))
    process_names(name_file.readlines())
    name_file.close()
    #print(entry)

with open(savepath, "w+") as f:
    json.dump({'name': names, 'target': targets}, f)
