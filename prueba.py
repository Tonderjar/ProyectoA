#import sys
from pygame import *
from music21 import *
from tkinter import *

# La función menup imprime las opciones que posee el usuario para utilizar el programa en el menú principal,
# una vez que el usuario elige una opción, el valor será guardado en una variable (opcmenprin) especificada en el programa
# al momento de hacer la llamada a la función.
#
# Entrada: No posee argumentos de entrada.
#
# Salida: el  valor obtenido al momento de finalizar los procesos de la función se llama opcmenprin, el cual refleja la opción
# elegida  por el usuario
#
# Precondición: True
#
# Postcondición: opcmenprin = menup()

def menup() -> int:
	while True:
		try:
			opcmenprin = int(input("Seleccione una opción: ")) 
			assert(opcmenprin == 1 or opcmenprin == 2 or opcmenprin == 3 or opcmenprin == 4 or opcmenprin == 5 or opcmenprin == 6)
			break
		except:
			print("Inserte una opción válida")
			print("")
	print("") # Salto de línea
	return opcmenprin

def click(boton) -> int:
	if (boton == botón1):
		opcmenprin = 1
	elif (boton == botón2):
		opcmenprin = 2
	elif (boton == botón3):
		opcmenprin = 3	
	elif (boton == botón4):
		opcmenprin = 4	
	elif (boton == botón5):
		opcmenprin = 5
	elif (boton == botón6):
		opcmenprin = 6
	print(opcmenprin)
	return opcmenprin
# La función submenu imprime las opciones que posee el usuario para utilizar el programa en el submenú,
# una vez que el usuario elige una opción, el valor será guardado en una variable (opcsubmen) especificada en el programa
# al momento de hacer la llamada a la función.
#
# Entrada: No posee argumentos de entrada.
#
# Salida: el  valor obtenido al momento de finalizar los procesos de la función se llama opcsubmen, el cual refleja la opción
# elegida  por el usuario
#
# Precondición: True
#
# Postcondición: opcsubmen = submenu()

def submenu() -> int:
	print("")
	print("SUBMENÚ")
	print("1.- Cargar archivo")
	print("2.- Generar arpegio")
	print("3.- Transportar")
	print("4.- Escuchar parte")
	print("5.- Borrar parte")
	print("6.- Volver al menú anterior")
	while True:
		try:
			opcsubmen = int(input("Seleccione una opción: "))
			assert(opcsubmen == 1 or opcsubmen == 2 or opcsubmen == 3 or opcsubmen == 4 or opcsubmen == 5 or opcsubmen == 6)
			break
		except:
			print("Inserte una opción válida")
			print("")
	print("") # Salto de línea
	return opcsubmen

# La función transp imprime las opciones que posee el usuario para transportar el elemento deseado, una vez que el usuario
# elige una opción, se procederá a transportar el elemento deseado el intervalo especificado por el usuario mediante la librería
# music21 
#
# Entrada: La función no posee elementos de entrada.
#
# Salida: La función tiene como salida un archivo del mismo tipo pero ya transportado el intervalo deseado.
#
# Precondición: comp[opcmenprin-1]!=''
#
# Postcondición: comp[opcmenprin-1] != transp(comp[opcmenprin-1]) or comp[opcmenprin-1] == transp(comp[opcmenprin-1])

def transp() -> [note.Note]:
	while True:
		try:	
			assert(comp[opcmenprin-1]!='')
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
					intervalo = input("Introduzca el intervalo: ")
					assert(intervalo == 'P1' or intervalo == 'm2' or intervalo == 'M2' or intervalo == 'm3' or intervalo == 'M3' or intervalo == 'P4' or intervalo == 'P5' or intervalo =='m6' or intervalo == 'M6' or intervalo == 'm7' or intervalo == 'M7' or intervalo == 'P8')
					break
				except:
					print("Intervalo incorrecto")
			auxiliar = comp[opcmenprin-1]
			comp[opcmenprin-1] = auxiliar.transpose(intervalo)
			return comp[opcmenprin-1]
			break
		except:
			print("La parte está vacía")
			break

# La función arp permite generar el arpegiode 8 elementos de una nota tomada como base,en este caso llamada basearp,la cual será tomada
# como parámetro de entrada y será proporcionada por el usuario luego de hacer la llamada a la función.
#
# Entrada: La función no posee argumentos de entrada.
#
# Salida: La función tiene como salida un archivo una lista de elementos de tipo note.Note los cules conforman el arpegio
# de la nota base (basearp), dicho arreglo se guarda en la variable arp, la cual constituye la salida de la función.
#
# Precondición: True
#
# Postcondición: comp[opcmenprin-1] == arp

def arpegio()-> [note.Note]:
	print("")
	basearp=input("Introduzca la nota base del arpegio: ")
	nota = note.Note(basearp)
	arp = stream.Part()
	for i in range(0, 8):
		arp.append(nota)
		nota = nota.transpose("m3")
	comp[opcmenprin - 1] = arp
	return  comp[opcmenprin - 1]

def reproducir() -> [note.Note]:
	composición = stream.Score()
	parte1 = stream.Part(comp[0])
	parte2 = stream.Part(comp[1])
	parte3 = stream.Part(comp[2])
	parte4 = stream.Part(comp[3])
	composición.insert(0, parte1)
	composición.insert(0, parte2)
	composición.insert(0, parte3)
	composición.insert(0, parte4)
	canción = midi.realtime.StreamPlayer(composición)
	canción.play()

# INICIO
comp = ['', '', '', '']
while True:
	root = Tk()

	etiqueta0 = Label(root, text="MENÚ PRINCIPAL", fg="light green", bg="black")
	etiqueta0.pack(fill=X)
	etiqueta1 = Label(root, text="Elija una opción:", fg="light green", bg="black")
	etiqueta1.pack(fill=X)
	botón1 = Button(text="Parte 1", fg="light green", bg="black" )
	botón1.pack(fill=X)
	botón2 = Button(text="Parte 2", fg="light green", bg="black")
	botón2.pack(fill=X)
	botón3 = Button(text="Parte 3", fg="light green", bg="black")
	botón3.pack(fill=X)
	botón4 = Button(text="Parte 4", fg="light green", bg="black")
	botón4.pack(fill=X)
	botón5 = Button(text="Escuchar composición", fg="light green", bg="black")
	botón5.pack(fill=X)
	botón6 = Button(text="Salir del programa", fg="light green", bg="black")
	botón6.pack(fill=X)
	botón1.bind("<Button-1>", click)
	botón2.bind("<Button-1>", click)
	botón3.bind("<Button-1>", click)
	botón4.bind("<Button-1>", click)
	botón5.bind("<Button-1>", click)
	botón6.bind("<Button-1>", click)
	print (opcmenprin)
	opcmenprin = menup() # Menú principal#########################################
	if (1 <= opcmenprin <= 4): # Opciones de las partes ##########################
		while True:
			opcsubmen = submenu() # Submenú de las partes#########################
			if (opcsubmen==1): # Cargar archivo###################################
				if comp[opcmenprin-1] == '':	
					comp[opcmenprin - 1] = converter.parse(input("Introduzca la ruta de su archivo: "))
				else:
					while True:
						try:
							opcion = 0
							opcion = int(input("Escriba 1 si desea sobrescribir la parte, 0 si no: "))
							assert( opcion == 1 or opcion == 0)
							break
						except:
							print("Introduzca una opción válida")
							break
					if opcion == 1:
						comp[opcmenprin - 1] = converter.parse(input("Introduzca la ruta de su archivo: "))
					else:
						pass
			elif (opcsubmen==2): # Generar arpegio#################################
				if (comp[opcmenprin-1] == ''):
					comp[opcmenprin-1] = arpegio()
				else:
					while True:
						try:
							opcion = 0
							opcion = int(input("Escriba 1 si desea sobrescribir la parte, 0 si no: "))
							assert( opcion == 1 or opcion == 0)
							break
						except:
							print("Introduzca una opción válida")
							break
					if opcion == 1:
						comp[opcmenprin-1] = arpegio()
					else:
						pass
			elif (opcsubmen==3): # Transportar######################################
				comp[opcmenprin-1] = transp()
			elif (opcsubmen==4): # Escuchar parte###################################
				while True:
					try:
						assert(comp[opcmenprin-1] != '')
						sp = midi.realtime.StreamPlayer(comp[opcmenprin-1])
						sp.play()
						break
					except:
						print("Debe cargar un archivo en esta parte")
						break
			elif (opcsubmen==5): # Borrar parte######################################
				comp[opcmenprin-1] = ''
				print("Se ha borrado la parte")
			elif (opcsubmen==6): # Volver al menú anterior###########################
				break
	elif (opcmenprin == 5): # Reproducir toda la composición#########################
		reproducir()
	elif (opcmenprin == 6): # Salir del programa#####################################
		while True:
			try:
				opcion = 0
				opcion = int(input("Escriba 1 si desea salir, 0 si no: "))
				assert( opcion == 1 or opcion == 0)
				break
			except:
				print("Introduzca una opcion válida")
				break
		if opcion == 1:
			sys.exit()
		else:
			pass
	root.mainloop()