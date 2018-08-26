# TBLPrint desarrollado por Magela Carballo - Agosto 2018

# Documentacion sobre el formato de los test Moodle donde se basa este programa
# https://docs.moodle.org/all/es/Formato_Moodle_XML

# TBLPrint recibe un archivo de test moodle exportado en formato XML 
# y devuelve un Archivo PDF con el test para completar.
# Tambien se imprime un PDF con las respuetas correctas a modo de 
# facilitar la correccion de la prueba. - no terminado 

import tkinter.filedialog as fd
from tkinter import filedialog
from tkinter import *
from lxml import etree
import html
import re
import xml.etree.ElementTree as ET
import random
#from ToPDF import *
import os
from htmlAPDF import *

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
			# Se obtiene el titulo de la pregunta - no se utiliza
			titulo = cuestion.find("name/text").text

			# Se obtiene la pregunta
			#pregunta = strip_tags(cuestion.find("questiontext/text").text)
			pregunta = cuestion.find("questiontext/text").text
			try:
				imagen = cuestion.find("questiontext/file").text
			except:
				imagen = ""
	
			# Respuestas de la Pregunta
			if tipopregunta != "essay":
				listaAuxiliarDeRespuestas = [] 		# Lista auxiliar que guarda solo las respuestas
				for t in cuestion.getiterator("answer"):
					#respuesta = strip_tags(t.find("text").text)
					respuesta = t.find("text").text
					listaAuxiliarDeRespuestas.append(respuesta)
					respuestaCorrecta = listaAuxiliarDeRespuestas[0] # guardo la respuesta correcta ( la primera en este caso)
					random.shuffle(listaAuxiliarDeRespuestas)		#entrevera las respuestas
				cantidadRespuestas = len(listaAuxiliarDeRespuestas)

				cont = 5
				for x in listaAuxiliarDeRespuestas:
					gridQuiz[i][cont]=x
					cont = cont + 1

			else:
				cantidadRespuestas = 0

			gridQuiz[i][0]= titulo
			gridQuiz[i][1]= pregunta
			gridQuiz[i][2] = tipopregunta
			gridQuiz[i][3] = imagen
			gridQuiz[i][4] = cantidadRespuestas
			#gridAnswers.append((i,respuestaCorrecta))	# se guarda numero pregunta con la respuesta correcta en una tupla

			# Imprime en pantalla todos los datos
			print ("Titulo Pregunta: ",gridQuiz[i][0])
			print( "Texto Pregunta: ",gridQuiz[i][1])
			print ("Tipo de Pregunta: ", gridQuiz[i][2])
			print ("Cantidad de Respuestas",gridQuiz[i][4])
			
			#if (cantidadRespuestas != 0 ):
			#	for p in range (5,5+cantidadRespuestas):
			#		print ("Respuesta :",gridQuiz[i][p])
			i = i + 1
			#	print("------------------------------------------------")
	return [gridQuiz, gridAnswers]

def abrirXML():
	ventana=Tk()
	ventana.title("TBL Printer by Magela Carballo")
	ventana.config(bg="#0B0B61")
	ventana.geometry("400x400")
	botonAbrir=Button(ventana,text="Select File", command=comando)
	botonAbrir.grid(padx=100,pady=100)
	abrirXML()

def comando():
 	archivo=fd.askopenfilename()	# Abre ventana para seleccionar archivo, devuelve la ruta del archivo	
 	datos = manejoDatos(archivo)	# recibe la matriz de datos generada desde el archivo xml
 	destino = filedialog.askdirectory()	# Caperta donde se guardara los pdf generados
 	print (" DESTINO ", destino)
 	convertir(datos[0],destino,nombrePrueba,descripcion )			# imprime los datos en un pdf
 	#imprimirRespuestas(datos[1],destino)			# imprime los datos en un pdf

def configuracionDeParametros():
	opcion = "a"
	descripcion = ""
	cantidadRespuestasMax = ""
	imprimirNumeroPregunta = False
	imprimirDescripcion = False
	while opcion != 0:
		parametros = []
		print ("Parameter Configuration")
		print ("1 - Escribir una Descripcion Personalizada ")
		print ("2 - Configurar Cantidad de Respuestas Maximas")
		print ("3 - Imprimir Numero de Pregunta")
		print ("4 - Imprimir Descripcion")
		print ("5 - Ver OPCIONES configuradas")
		print ("0 - Salir")
		opcion = input("Ingrese una opcion para configurar (Q para volver atras)")
	
		if (opcion == '1'):
			descripcion = input("Ingrese Descripcion Opcional de la Prueba: ")
		elif (opcion == '2'):
			cantidadRespuestasMax = input("Ingrese cantidad de respuestas maxima [0-100]: ")
		elif (opcion == '3'):
			if (imprimirNumeroPregunta == False):
				imprimirNumeroPregunta = True
			else:
				imprimirNumeroPregunta = False
			print ("Se cambio el valor de impresion")
		elif (opcion == '4'):
			if (imprimirDescripcion ==  False):
				imprimirDescripcion = True
			else:
				imprimirDescripcion = False
			print ("Se cambio el valor de impresion")
		elif (opcion == '5'):
			print("Descripcion de la Prueba: ", descripcion)
			print("Cantidad de Preguntas Maximas por Pregunta: ",cantidadRespuestasMax)
			print("Imprimir Numero de Pregunta: ", imprimirNumeroPregunta)
			print("Imprimir Descripcion de Prueba: ",imprimirDescripcion)
			print("")
		elif(opcion == '0'):
			parametros.append(descripcion)
			parametros.append(cantidadRespuestasMax)
			parametros.append(imprimirNumeroPregunta)
			parametros.append(imprimirDescripcion)
			return parametros
		else:
			print("Opcion incorrecta, seleccione nuevamente")
		#return parametros

def main():
	#Parametros
	directorioOrigen = ''
	directorioDestino = ""
	descripcion = ""
	cantidadDeRespuestas = 10
	inumeroPregunta = False
	idescripcion = False

	while (directorioOrigen == ''):
		directorioOrigen = input("\nSelect xml file (C for cancel): ")
		if (directorioOrigen == ''):
			print("You must enter the source directory")
		elif(directorioOrigen == 'P'):
			parametros = configuracionDeParametros();
			descripcion = parametros[0]
			cantidadRespuestasMax = parametros[1]
			inumeroPregunta = parametros[2]
			idescripcion = parametros[3]
			directorioOrigen = ''
		elif (directorioOrigen == 'C'):
			print ("Bye!")
		elif (os.path.basename(directorioOrigen).split('.')[-1] != 'xml'):
			print ("You must enter in a .xml file")
		elif (directorioOrigen == 'W'):
			abrirXML()   # abrir ventana grafica
			directorioOrigen = ""
		else:
			directorioDestino = ''
			while (directorioDestino == ''):
				directorioDestino = input("Select destination directory (C for cancel) ")
				if (directorioDestino == ''):
					print("You must enter the destination directory")
				elif(directorioDestino == 'C'):
					print ("Bye!")
					directorioOrigen = ''
				else:

					nombrePrueba = input("\nInput a title for the quiz: ")
					datos = manejoDatos(directorioOrigen, cantidadDeRespuestas)
					pasarPDF( datos[0], directorioDestino,nombrePrueba,
							descripcion,inumeroPregunta,idescripcion)
					directorioOrigen = ''

main()
