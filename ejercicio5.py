#Haz un menu que tenga como opciones los datos del json, es decir 1- Nombre. Y te diga los datos en contreto. 
#Una opción sera un submenú con opciones parecidas, pero si le pulsa esa opción te pregunatara cual quieres buscar 
#y te dará todos los datos de el.
import json
from pprint import pprint
with open("nba.json") as data_file:
	data = json.load(data_file)
opcion = ""
while opcion != 8:
	print("----------------------")
	print("Menú")
	print("----------------------")
	print("1. Id")
	print("2. Abreviación")
	print("3. Nombre")
	print("4. Nombre común")
	print("5. Localizacion")
	print("6. Premios")
	print("7. Otras Opciones")
	print("8. Salir")
	print("----------------------")
	opcion = int(input("Introduzca su opción: "))
	if opcion == 1:
		for equipo in data:
			print(equipo["teamId"])
	elif opcion == 2:
		for equipo in data:
			print(equipo["abbreviation"])
	elif opcion == 3:
		for equipo in data:
			print(equipo["teamName"])
	elif opcion == 4:
		for equipo in data:
			print(equipo["simpleName"])
	elif opcion == 5:
		for equipo in data:
			print(equipo["location"])
	elif opcion == 6:
		for equipo in data:
			print(equipo["premios"])
	elif opcion == 7:
		opcion2 = ""
		while opcion2 != 7:
			print("******************")
			print("Submenú")
			print("******************")
			print("1. Buscar por Id")
			print("2. Buscar por Abreviación")
			print("3. Buscar por Nombre")
			print("4. Buscar por Nombre común")
			print("5. Buscar por Localizacion")
			print("6. Buscar por Premios")
			print("7. Salir")
			print("******************")
			opcion2 = int(input("Introduzca su opción: "))
			if opcion2 == 1:
				ID = int(input("Introduzca la ID de un equipo: "))
				for equipo in data:
					if ID == equipo["teamId"]:
						print("Abreviación:", equipo["abbreviation"])
						print("Nombre: ", equipo["teamName"])
						print("Nombre comun:", equipo["simpleName"])
						print("Localizacion:", equipo["location"])
						print("Premios:", equipo["premios"])
			elif opcion2 == 2:
				abreviacion = input("Introduzca la abreviación de un equipo: ")
				for equipo in data:
					if abreviacion == equipo["abbreviation"]:
						print("Id: ", equipo["teamId"])
						print("Nombre: ", equipo["teamName"])
						print("Nombre comun:", equipo["simpleName"])
						print("Localizacion:", equipo["location"])
						print("Premios:", equipo["premios"])
			elif opcion2 == 3:
				nombre = input("Introduce el nombre del equipo: ")
				for equipo in data:
					if nombre == equipo["teamName"]:
						print("Id: ", equipo["teamId"])
						print("Abreviación:", equipo["abbreviation"])
						print("Nombre comun:", equipo["simpleName"])
						print("Localizacion:", equipo["location"])
						print("Premios:", equipo["premios"])
			elif opcion2 == 4:
				nombre_simple = input("Introduce el nombre común del equipo: ")
				for equipo in data:
					if nombre_simple == equipo["simpleName"]:
						print("Id: ", equipo["teamId"])
						print("Abreviación:", equipo["abbreviation"])
						print("Nombre: ", equipo["teamName"])
						print("Localizacion:", equipo["location"])
						print("Premios:", equipo["premios"])
			elif opcion2 == 5:
				localizacion = input("Introduce la ciudad del equipo: ")
				for equipo in data:
					if localizacion == equipo["location"]:
						print("Id: ", equipo["teamId"])
						print("Abreviación:", equipo["abbreviation"])
						print("Nombre: ", equipo["teamName"])
						print("Nombre comun:", equipo["simpleName"])
						print("Premios:", equipo["premios"])	
			elif opcion2 == 6:
				premio = int(input("Introduce los premios de los equipos: "))
				for equipo in data:
					if premio == equipo["premios"]:
						print("Id: ", equipo["teamId"])
						print("Abreviación:", equipo["abbreviation"])
						print("Nombre: ", equipo["teamName"])
						print("Nombre comun:", equipo["simpleName"])
						print("Localizacion:", equipo["location"])