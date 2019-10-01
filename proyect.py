import sys
from pygame import *
from music21 import *

# print de Menu Principal
def menup() -> int:
	print("")
	print("MENÚ PRINCIPAL")
	print("1.- Parte 1")
	print("2.- Parte 2")
	print("3.- Parte 3")
	print("4.- Parte 4")
	print("5.- Escuchar toda la composición")
	print("6.- Salir del programa")
	opcmenprin = int(input("Seleccione una opción: "))
	print("") # Salto de línea
	return opcmenprin

# print del Submenu, hace print cuando selecciona alguna de las 4 partes
def submenu() -> int:
	print("")
	print("SUBMENÚ")
	print("1.- Cargar archivo")
	print("2.- Generar arpegio")
	print("3.- Transportar")
	print("4.- Escuchar parte")
	print("5.- Borrar parte")
	print("6.- Volver al menú anterior")
	opcsubmen = int(input("Seleccione una opción: "))
	print("") # Salto de línea
	return opcsubmen

# Menu de Transportar 
def transp(comp: [note.Note]) -> [note.Note]:
	print ("")
	print ("Unísono:       P1")
	print ("Segunda menor: m2")
	print ("Segunda mayor: M2")
	print ("Tercera menor: m3")
	print ("Tercera mayor: M3")
	print ("Cuarta justa:  P4")
	print ("Quinta justa:  P5")
	print ("Sexta menor:   m6")
	print ("Sexta mayor:   M6")
	print ("Séptima menor: m7")
	print ("Séptima mayor: M7")
	print ("Octava justa:  P8")
	print ("")
	while True:
		try:
			a = input("Introduzca el intervalo: ")
			assert(a == "P1" or a == "m2" or a == "M2" or a == "m3" or a == "M3" or a == "P4" or a == "P5" or a =="m6" or a == "M6" or a == "m7" or a == "M7" or a == "P8")
			break
		except:
			print("Intervalo incorrecto")
	aux = stream.Part(comp[opcmenprin-1])
	comp[opcmenprin-1] = aux.transpose(a)
	return comp[opcmenprin-1]

# Main
comp = ['', '', '', '']
while True:
	opcmenprin = menup() # Menú principal
	if (1 <= opcmenprin <= 4):
		while True:
			opcsubmen = submenu() # Submenú de las partes
			if (opcsubmen==1): # Cargar archivo
				comp[opcmenprin - 1] = converter.parse(input("Introduzca la ruta de su archivo: "))
				sp = midi.realtime.StreamPlayer(comp[opcmenprin - 1])
				sp.play()
			elif (opcsubmen==2): # Generar arpegio
				print("En desarrollo")
			elif (opcsubmen==3): # Transportar
				comp[opcmenprin-1] = transp(comp[opcmenprin-1])
			elif (opcsubmen==4): # Escuchar parte
				while True:
					try:
						assert(comp[opcmenprin-1] != '')
						sp = midi.realtime.StreamPlayer(comp[opcmenprin-1])
						sp.play()
						break
					except:
						print("Debe cargar un archivo en esta parte")
						break
			elif (opcsubmen==5): # Borrar parte
				comp[opcmenprin-1] = ''
			elif (opcsubmen==6): # Volver al menú anterior
				print("Esta opción regresa al menú anterior")
				break
	elif (opcmenprin == 5):
		sp = midi.realtime.StreamPlayer(comp)
		sp.play()
	elif (opcmenprin == 6):
		#posible confirmación
		sys.exit()
