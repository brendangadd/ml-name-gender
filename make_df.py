import os
import pandas
from os.path import join as pjoin

directory = pjoin('/', 'home', 'brendan', 'Downloads', 'names')

names = []
targets = []

def process_names(lines):
  for line in lines:
    parts = line.split(',')
    names.append(parts[0].lower())
    targets.append(parts[1] == 'M' and 1 or 0)

for entry in [
  f for f in os.scandir(directory)
  if f.is_file() and f.name.endswith('.txt')
]:
  name_file = open(entry.path)
  process_names(name_file.readlines())
  name_file.close()
  print(entry.name)

frame = pandas.DataFrame({'name': names, 'target': targets})
frame.to_csv('names.csv')
