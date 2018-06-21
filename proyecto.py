import sys
from pygame import *
from music21 import *

def menup() -> 'void':
	print("MENÚ PRINCIPAL")
	print("1.- Componer")
	print("2.- Escuchar Composición")
	print("3.- Salir del programa")
	omp = int(input("Seleccione una opción: "))
	print("") # Salto de linea
	return omp

def Componer() -> int:
	print("COMPOSICIÓN")
	print("1.- Parte 1")
	print("2.- Parte 2")
	print("3.- Parte 3")
	print("4.- Parte 4")
	print("5.- Volver al menú principal")
	omc = int(input("Seleccione una opción: "))
	print("") # Salto de linea
	return omc

def submenu() -> int:
	print("SUBMENÚ")
	print("1.- Cargar archivo")
	print("2.- Generar arpegio")
	print("3.- Transportar")
	print("4.- Escuchar parte")
	print("5.- Borrar parte")
	print("6.- Volver al menú anterior")
	osm = int(input("Seleccione una opción: "))
	print("") # Salto de linea
	return osm

#main
comp = ['', '', '', '']
while True:
	omp = menup() # Menu principal
	if (omp == 1): # Componer
		while True:
			omc = Componer() # Menu de las partes
			if (1 <= omc <= 4):
				while True:
					osm = submenu() # Submenu de las partes
					if (osm==1): # Cargar archivo
						comp[omc - 1] = converter.parse(input("Introduzca la ruta de su archivo: "))
						sp = midi.realtime.StreamPlayer(comp[omc - 1])
						sp.play()
					elif (osm==2): # Generar arpegio
						print("En desarrollo")
					elif (osm==3): # Transportar
						print("En desarrollo")
					elif (osm==4): # Escuchar parte
						print("En desarrollo")
					elif (osm==5): # Borrar parte
						print("En desarrollo")
					elif (osm==6): # Volver al menu anterior
						print("Esta opción regresa al menú anterior")
						break
			elif (omc == 5):
				print("Esta opción regresa al menú principal")
				break
		if (omp == 2): #Escuchar composicion
			#sp = midi.realtime.StreamPlayer(cancion) #Aqui en "cancion" va el nombre que le pongamos a la composicion
			#sp.play()
			print("En desarrollo")

	if (omp == 3):
		#posible confirmacion
		sys.exit()
