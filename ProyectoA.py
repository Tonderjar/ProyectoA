import sys

def menup() -> 'void'
	print("1.- Composición")
	print("2.- Escuchar Composición")
	print("3.- Salir del programa")
	omp = int(input("Seleccione una opcion: "))
	return omp

def Componer(omp: int) -> int:
	print("1.- Parte 1")
	print("2.- Parte 2")
	print("3.- Parte 3")
	print("4.- Parte 4")
	omc = int(input("Seleccione una opcion: "))
	return omc

def submenu(omc: int) -> int:
	print("1.- Cargar archivo")
	print("2.- Generar arpegio")
	print("3.- Transportar")
	print("4.- Escuchar parte")
	print("5.- Borrar parte")
	print("6.- Volver al menu anterior")
	osm = int(input("Seleccione una opcion"))
	return osm

#main
menup()
