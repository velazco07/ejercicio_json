#Haz un programa que pida dos números (premios), e imprima el nombre, la ciudad y el nombre común.
import json
from pprint import pprint
with open("nba.json") as data_file:
	data = json.load(data_file)
numeromn = int(input("Introduzca el valor por el que quiere empezar a buscar: "))
numeromy = int(input("Introduzca el valor por el que quiere que deje de buscar: "))
for equipo in data:
	if equipo["premios"] >= numeromn and equipo["premios"] <= numeromy:
		print("Nombre: ", equipo["teamName"])
		print("Ciudad: ", equipo["location"])
		print("Nombre Común: ", equipo["simpleName"])
		