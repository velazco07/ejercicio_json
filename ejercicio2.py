# Cuenta los equipos cuya abreviacion empieze por la letra N
import json
from pprint import pprint
with open("nba.json") as data_file:
	data=json.load(data_file)
contador = 0
for equipo in data:
	if equipo["abbreviation"].startswith("M") == True:
		contador = contador + 1
print(contador)