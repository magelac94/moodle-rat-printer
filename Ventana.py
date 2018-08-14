# TBLPrint desarrollado por Magela Carballo - Agosto 2018

# Documentacion sobre el formato de los test Moodle donde se basa este programa
# https://docs.moodle.org/all/es/Formato_Moodle_XML

# TBLPrint recibe un archivo de test moodle exportado en formato XML 
# y devuelve un Archivo PDF con el test para completar.
# Tambien se imprime un PDF con las respuetas correctas a modo de 
# facilitar la correccion de la prueba.

import tkinter.filedialog as fd
from tkinter import filedialog
from tkinter import *
from lxml import etree
import html
import re
import xml.etree.ElementTree as ET
import random
from ToPDF import *
import os

# Funcion que elimina etiquetas HTML
def strip_tags(value):
	return re.sub(r'<[^>]*?>','',value)

# Funcion que obtiene un archivo XML realiza un arbol xml. 
# Con el arbol se genera una matriz de preguntas, respuestas y algunos datos necesarios.
def manejoDatos(archivo,cantidadRespuestasMax):
	
	gridQuiz = []
	gridAnswers = []

	# Estructura donde se guardaran las preguntas
	# gridQuiz[x][] # numero pregunta
	# gridQuiz[][0]	# Titulo
	# gridQuiz[][1]	# Pregunta
	# gridQuiz[][2]	# Tipo de Pregunta
	# gridQuiz[][3]	# Imagen
	# gridQuiz[][4]	# Cantidad de Respuestas
	# gridQuiz[][5]	# Respuesta 1
	# gridQuiz[][6]	# Respuesta 2
	# gridQuiz[][7]	# Respuesta 3 ...

	# Estructura donde se guardaran las respuestas correctas 
	# gridAnswer[(numero pregunta, descripcion de la respuesta correcta)]


	#Arbol XML
	tree = ET.parse(archivo)
	root = tree.getroot()

	# Cantidad de Preguntas
	cantidadPreguntas = len(root)
	print ("Cantidad de Preguntas del test ", cantidadPreguntas)

	# Cantidad de Respuestas maximas por pregunta
#	cantidadRespuestasMax = 100
	
	# Generacion de Matriz
	for j in range(cantidadPreguntas):
		gridQuiz.append([])
		for h in range(cantidadRespuestasMax):
			gridQuiz[j].append(None)

	# Se buscan las etiquetas en el arbol y se guardan los elementos en la matriz
	i = 0
	for cuestion in root.findall('question'):

		# Guardo el tipo de pregunta
		# Puede ser multichoice|truefalse|shortanswer|matching|cloze|essay|numerical|description
		tipopregunta = cuestion.get('type')

		# Existe una pregunta de tipo category que no es pregunta y debe descartarse
		if tipopregunta == "category":
			cantidadPreguntas = cantidadPreguntas - 1
			#i = i - 1
		else:
			# Se obtiene el titulo de la pregunta
			titulo = cuestion.find("name/text").text

			# Se obtiene la pregunta

			#pregunta = strip_tags(cuestion.find("questiontext/text").text)
			pregunta = cuestion.find("questiontext/text").text

			# En caso de tener imagen se guarda la misma
			#imagen = resolvertipopregunta = cuestion.get('type')

			# Respuestas de la Pregunta
			listaAuxiliarDeRespuestas = [] 		# Lista auxiliar que guarda solo las respuestas
			for t in cuestion.getiterator("answer"):
				#respuesta = strip_tags(t.find("text").text)
				respuesta = t.find("text").text
				listaAuxiliarDeRespuestas.append(respuesta)
				respuestaCorrecta = listaAuxiliarDeRespuestas[0] # guardo la respuesta correcta ( la primera en este caso)
				random.shuffle(listaAuxiliarDeRespuestas)		#entrevera las respuestas
			cantidadRespuestas = len(listaAuxiliarDeRespuestas)

			gridQuiz[i][0]= titulo
			gridQuiz[i][1]= pregunta
			gridQuiz[i][2] = tipopregunta
		#	gridQuiz[i][3] = imagen
			gridQuiz[i][4] = cantidadRespuestas

			gridAnswers.append((i,respuestaCorrecta))	# se guarda numero pregunta con la respuesta correcta en una tupla

			cont = 5
			for x in listaAuxiliarDeRespuestas:
				gridQuiz[i][cont]=x
				cont = cont + 1
			
			# Imprime en pantalla todos los datos
			print ("Titulo Pregunta: ",gridQuiz[i][0])
			print( "Texto Pregunta: ",gridQuiz[i][1])
			print ("Tipo de Pregunta: ", gridQuiz[i][2])
			print ("Cantidad de Respuestas",gridQuiz[i][4])
			
			for p in range (5,5+cantidadRespuestas):
				print ("Respuesta :",gridQuiz[i][p])
			i = i + 1
			print("------------------------------------------------")

	return [gridQuiz, gridAnswers]

#def abrirXML(archivo):
# 	archivo=fd.askopenfilename()	# Abre ventana para seleccionar archivo, devuelve la ruta del archivo	
# 	datos = manejoDatos(archivo)	# recibe la matriz de datos generada desde el archivo xml
# 	destino = filedialog.askdirectory()	# Caperta donde se guardara los pdf generados
# 	print (" DESTINO ", destino)
# 	convertir(datos[0],destino,nombrePrueba,descripcion,tipoLetra )			# imprime los datos en un pdf
# 	imprimirRespuestas(datos[1],destino)			# imprime los datos en un pdf

def configuracionDeParametros():
	parametros = []
	print ("Parameter Configuration")
	print ("1 - Escribir un Titulo Personalizado")
	print ("2 - Escribir una Descripcion Personalizada ")
	print ("3 - Configurar Cantidad de Respuestas Maximas")
	print ("4 - Configurar Tipo de Letra")
	print ("5 - Imprimir Titulo Prueba")
	print ("6 - Imprimir Numero de Pregunta")
	print ("7 - Imprimir Titulo de Pregunta")
	print ("8 - Imprimir Descripcion")
	print ("9 - Ver OPCIONES configuradas")
	print ("0 - Salir")
	opcion = input("Ingrese una opcion para configurar (Q para volver atras)")
	
	if (opcion == '1'):
		nombrePrueba = input(" Ingrese Titulo para la Prueba: ")
	elif (opcion == '2'):
		descripcion = input("Ingrese Descripcion Opcional de la Prueba: ")
	elif (opcion == '3'):
		cantidadRespuestasMax = input("Ingrese cantidad de respuestas maxima [0-100]: ")
	elif (opcion == '4'):
		tipoLetra = input("Tipo Letra: A (Arial) / Time Roman (T): ")
	elif (opcion == '5'):
		if (imprimirTituloPrueba == true):
			imprimirTituloPrueba = false
		else:
			imprimirTituloPrueba = true
		print ("Se cambio el valor de impresion")
	elif (opcion == '6'):
		if (imprimirNumeroPregunta == false):
			imprimirNumeroPregunta = true
		else:
			imprimirNumeroPregunta = false
		print ("Se cambio el valor de impresion")
	elif (opcion == '7'):
		if (imprimirTituloPregunta ==  false):
			imprimirTituloPregunta = true
		else:
			imprimirTituloPregunta = false
		print ("Se cambio el valor de impresion")
	elif (opcion == '8'):
		if (imprimirDescripcion ==  false):
			imprimirDescripcion = true
		else:
			imprimirDescripcion = false
		print ("Se cambio el valor de impresion")
	elif (opcion == '9'):
		print("Nombre de Prueba: ", nombrePrueba)
		print("Descripcion de la Prueba: ", descripcion)
		print("Cantidad de Preguntas Maximas por Pregunta: ",cantidadRespuestasMax)
		print("Tipo de Letra: ", tipoLetra)
		print("Imprimir Titulo de Prueba:", imprimirTituloPrueba)
		print("Imprimir Numero de Pregunta: ", imprimirNumeroPregunta)
		print("Imprimir Titulo de la Pregunta: ",imprimirTituloPregunta)
		print("Imprimir Descripcion de Prueba: ",imprimirDescripcion)
		print("")
	elif(opcion == '0'):
		parametros.append(nombrePrueba)
		parametros.append(descripcion)
		parametros.append(cantidadRespuestasMax)
		parametros.append(tipoLetra)
		parametros.append(imprimirTituloPrueba)
		parametros.append(imprimirNumeroPregunta)
		parametros.append(imprimirTituloPregunta)
		parametros.append(imprimirDescripcion)
		return parametros
	else:
		print("Opcion incorrecta, seleccione nuevamente")


#Parametros
directorioOrigen = ''
directorioDestino = ''
nombrePrueba = ''
descripcion = ''
cantidadDeRespuestas = 10
tipoLetra = ''
imprimirNumeroPregunta = False
imprimirTituloPregunta = False

while (directorioOrigen == ''):
	directorioOrigen = input("Select xml file or press P for more options(C for cancel): ")
	if (directorioOrigen == ''):
		print("You must enter the source directory")
	elif(directorioOrigen == 'P'):
		parametros = configuracionDeParametros();
		nombrePrueba = parametros[0]
		descripcion = parametros[1]
		cantidadRespuestasMax = parametros[2]
		tipoLetra = parametros[3]
		itituloPrueba = parametros[4]
		inumeroPregunta = parametros[5]
		itituloPregunta = parametros[6]
		idescripcion = parametros[7]
		directorioOrigen = ''
	elif (directorioOrigen == 'C'):
		print ("Bye!")
	elif (os.path.basename(directorioOrigen).split('.')[-1] != 'xml'):
		print ("You must enter in a .xml file")
	elif (directorioOrigen == 'W'):
		abrirXML()   # abrir ventana grafica
	else:
		directorioDestino = ''
		nombrePrueba = os.path.basename(directorioOrigen).split('.')[0]
		while (directorioDestino == ''):
			directorioDestino = input("Select destination directory (C for cancel) ")
			if (directorioDestino == ''):
				print("You must enter the destination directory")
			elif(directorioDestino == 'C'):
				print ("Bye!")
				directorioOrigen = ''
			else:
				try:
					datos = manejoDatos(directorioOrigen,cantidadDeRespuestas)
					try:
						convertir( datos[0], directorioDestino, nombrePrueba,descripcion,tipoLetra,imprimirNumeroPregunta,imprimirTituloPregunta)
						imprimirRespuestas(datos[1],directorioDestino, nombrePrueba,tipoLetra)
						print("PDF file created successfully in : ", directorioDestino)
						directorioOrigen = ''
					except:
						print ("Error in selected directory")
						directorioOrigen = ''
				except:
					print ("Error opening the source file")
					directorioDestino = ''



#ventana=Tk()
#ventana.title("TBL Printer by Magela Carballo")
#ventana.config(bg="#0B0B61")
#ventana.geometry("600x500")
#botonAbrir=Button(ventana,text="Select File", command=abrirXML)
#botonAbrir.grid(padx=100,pady=100)
#ventana.mainloop()