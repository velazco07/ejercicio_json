#Haz un programa que pida una ciudad y la abreviación del nombre y diga todos lo datos del equipo de esa ciudad.
import json
from pprint import pprint
with open("nba.json") as data_file:
	data = json.load(data_file)
ciudad = input("Introduce la ciudad natal del equipo (La primera letra en mayuscula): ")
abreviacion = input ("Introduce la abreviación del equipo (En mayusculas): ")
if ciudad == "" or abreviacion == "":
	print("Tiene que reyenar los dos parametros")
else:
	for equipo in data:
		if ciudad == equipo["location"] and abreviacion == equipo["abbreviation"]:
			print("Id:", equipo["teamId"])
			print("Abreviación:", equipo["abbreviation"])
			print("Nombre: ", equipo["teamName"])
			print("Nombre comun:", equipo["simpleName"])
			print("Localizacion:", equipo["location"])
			print("Premios:", equipo["premios"])
		