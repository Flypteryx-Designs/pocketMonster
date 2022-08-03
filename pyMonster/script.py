import re

poke_dict = {}

with open('E:\Documents\FlypteryxDesigns\pyMonster\pokedex.txt') as file:
  lines = file.readlines()
  for line in lines:
    broken = re.split(r'\s{2,}', line.strip())
    poke_id = str(hex(int(broken[0])))[2:]
    base_stats = poke_id if len(poke_id) == 2 else '0' + poke_id 
    for stat in broken[3:8]:
      hex_stat = str(hex(int(stat)))[2:]
      base_stats += hex_stat if len(hex_stat) == 2 else '0' + hex_stat
    poke_dict[broken[1]] = base_stats
    print(base_stats, broken[1])
