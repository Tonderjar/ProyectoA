import sys
from pygame import *
from music21 import *

def menup() -> int:
	print("MENÚ PRINCIPAL")
	print("1.- Parte 1")
	print("2.- Parte 2")
	print("3.- Parte 3")
	print("4.- Parte 4")
	print("5.- Escuchar toda la composición")
	print("6.- Salir del programa")
	omp = int(input("Seleccione una opción: "))
	print("") # Salto de línea
	return omp

def submenu() -> int:
	print("SUBMENÚ")
	print("1.- Cargar archivo")
	print("2.- Generar arpegio")
	print("3.- Transportar")
	print("4.- Escuchar parte")
	print("5.- Borrar parte")
	print("6.- Volver al menú anterior")
	osm = int(input("Seleccione una opción: "))
	print("") # Salto de línea
	return osm

#main
comp = ['', '', '', '']
while True:
	omp = menup() # Menú principal
	if (1 <= omp <= 4):
		while True:
			osm = submenu() # Submenú de las partes
			if (osm==1): # Cargar archivo
				comp[omp - 1] = converter.parse(input("Introduzca la ruta de su archivo: "))
				sp = midi.realtime.StreamPlayer(comp[omp - 1])
				sp.play()
			elif (osm==2): # Generar arpegio
				print("En desarrollo")
			elif (osm==3): # Transportar
				print("En desarrollo")
			elif (osm==4): # Escuchar parte
				print("En desarrollo")
			elif (osm==5): # Borrar parte
				print("En desarrollo")
			elif (osm==6): # Volver al menú anterior
				print("Esta opción regresa al menú anterior")
				break
	elif (omp == 5):
		print("En desarrollo")
		break
	elif (omp == 6):
		#posible confirmación
		sys.exit()
