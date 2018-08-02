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

# Funcion que elimina etiquetas HTML
def strip_tags(value):
	return re.sub(r'<[^>]*?>','',value)

# Funcion que obtiene un archivo XML realiza un arbol xml. 
# Con el arbol se genera una matriz de preguntas, respuestas y algunos datos necesarios.
def manejoDatos(archivo):
	
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
	cantidadRespuestasMax = 100
	
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
			pregunta = strip_tags(cuestion.find("questiontext/text").text)

			# En caso de tener imagen se guarda la misma
			#imagen = resolvertipopregunta = cuestion.get('type')

			# Respuestas de la Pregunta
			listaAuxiliarDeRespuestas = [] 		# Lista auxiliar que guarda solo las respuestas
			for t in cuestion.getiterator("answer"):
				respuesta = strip_tags(t.find("text").text)
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

# Funcion que recibe una lista y con una funcion auxiliar se imprime el test
def imprimirPDF(lista):
	convertir(lista)

# Funcion que recibe una lista y con una funcion auxiliar se imprime las respuestas correctas
def respuestasPDF(lista):
	imprimirRespuestas(lista)

def abrirXML():
 	archivo=fd.askopenfilename()	# Abre ventana para seleccionar archivo, devuelve la ruta del archivo	
 	datos = manejoDatos(archivo)	# recibe la matriz de datos generada desde el archivo xml
 	imprimirPDF(datos[0])			# imprime los datos en un pdf
 	respuestasPDF(datos[1])			# imprime los datos en un pdf

	

	
ventana=Tk()
ventana.title("TBL Printer")
ventana.config(bg="#0B0B61")
ventana.geometry("300x400")
botonAbrir=Button(ventana,text="Seleccionar archivo", command=abrirXML)
botonAbrir.grid(padx=100,pady=100)
ventana.mainloop()