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

<<<<<<< HEAD
def menup() -> int:
=======
def Componer() -> int:
	print("COMPOSICIÓN")
>>>>>>> e2cc93d296690b8eec37367757e765c3b83e3071
	print("1.- Parte 1")
	print("2.- Parte 2")
	print("3.- Parte 3")
	print("4.- Parte 4")
<<<<<<< HEAD
	print("5.- Escuchar toda la composicion")
	print("6.- Salir del programa")
	omp = int(input("Seleccione una opción: "))
	return omp
=======
	print("5.- Volver al menú principal")
	omc = int(input("Seleccione una opción: "))
	print("") # Salto de linea
	return omc
>>>>>>> e2cc93d296690b8eec37367757e765c3b83e3071

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
	if (1 <= omc <= 4):
		while True:
<<<<<<< HEAD
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
=======
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
>>>>>>> e2cc93d296690b8eec37367757e765c3b83e3071
			#sp = midi.realtime.StreamPlayer(cancion) #Aqui en "cancion" va el nombre que le pongamos a la composicion
			#sp.play()
			print("En desarrollo")

	if (omp == 3):
		#posible confirmacion
		sys.exit()
