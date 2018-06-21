import sys
from pygame import *
from music21 import *

def menup() -> 'void':
	print("1.- Componer")
	print("2.- Escuchar Composición")
	print("3.- Salir del programa")
	omp = int(input("Seleccione una opción: "))
	return omp

def menup() -> int:
	print("1.- Parte 1")
	print("2.- Parte 2")
	print("3.- Parte 3")
	print("4.- Parte 4")
	print("5.- Escuchar toda la composicion")
	print("6.- Salir del programa")
	omp = int(input("Seleccione una opción: "))
	return omp

def submenu() -> int:
	print("1.- Cargar archivo")
	print("2.- Generar arpegio")
	print("3.- Transportar")
	print("4.- Escuchar parte")
	print("5.- Borrar parte")
	print("6.- Volver al menú anterior")
	osm = int(input("Seleccione una opción: "))
	return osm

#main
comp = ['', '', '', '']
while True:
	omp = menup() # Menu principal
	if (1 <= omc <= 4):
		while True:
			osm = submenu() # Submenu de las partes
			if (osm==1): # Cargar archivo
				comp[omc - 1] = converter.parse(input("Introduzca la ruta de su archivo entre '': "))
				sp = midi.realtime.StreamPlayer(comp[omc - 1])
				sp.play()
			#elif (osm==2): # Generar arpegio
			#	d
			#elif (osm==3): # Transportar
			#	d
			#elif (osm==4): # Escuchar parte
			#	s
			#elif (osm==5): # Borrar parte
			#	s
			elif (osm==6): # Volver al menu anterior
				break
	elif (omc == 5):
		break
		#if (omp == 2): #Escuchar composicion
			#sp = midi.realtime.StreamPlayer(cancion) #Aqui en "cancion" va el nombre que le pongamos a la composicion
			#sp.play()

	if (omp == 3):
		#posible confirmacion
		sys.exit()
