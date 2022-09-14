import math
import re
# import json

attack = 14
defense = 5
speed = 8
special = 6
hitpoints = 4

mewtwo_statexp = (((((234 - 80) * 100) / 70) - (106 * 2)) * 4) ** 2

print(mewtwo_statexp) 

def parsePokemonList():
  genIPoke = {}
  with open('Flypteryx-Designs\pocketMonster\python_files\genIPoke.txt', 'r') as f:
    for line in f.readlines():
      newLine = re.split(r'\W+', line)
      newLine.pop(1)
      if newLine[-1] == '':
        newLine.pop()
      pokeObj = {
        'id': newLine[0],
        'name': newLine[1],
        'HP': newLine[2],
        'Attack': newLine[3],
        'Defense': newLine[4],
        'Speed': newLine[5],
        'Special': newLine[6],
        'Total': newLine[7],
      }
      genIPoke[pokeObj['id']] = pokeObj
  return genIPoke

def parseMoveList():
  genIMoves = {}
  with open ('Flypteryx-Designs\pocketMonster\python_files\genIMoves.txt', 'r') as f:
    for line in f.readlines():
      newLine = line.split(',')
      fullSplit = list(map(lambda x: x.strip(), [*newLine[0].split(' ', 1), *newLine[1].split('\t')]))
      if fullSplit[2] == '':
        fullSplit.pop(2)
      moveObj = {
        'id': fullSplit[0],
        'name': fullSplit[1],
        'type': fullSplit[2],
        'category': fullSplit[3],
        'power': fullSplit[4] if fullSplit[4] != 'â€”' else '-',
        'accuracy': fullSplit[5] if fullSplit[5] != 'â€”' else '-',
        'pp': fullSplit[6] if fullSplit[6] != 'â€”' else '-',
        'effect': fullSplit[7],
      }
      genIMoves[moveObj['id']] = moveObj
  return genIMoves

# with open('Flypteryx-Designs\pocketMonster\python_files\genIMoves.json', 'w') as outFile:
#  json.dump(parseMoveList(), outFile)

# with open('Flypteryx-Designs\pocketMonster\python_files\genIPoke.json', 'w') as outFile:
#  json.dump(parsePokemonList(), outFile)

