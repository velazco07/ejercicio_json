# Dime el nombre de todos los equipos junto a su localización.
import json
from pprint import pprint 
with open("nba.json") as data_file:
	data = json.load(data_file)
for equipo in data:
	print(equipo["teamName"],"pertenece a", equipo["location"])
