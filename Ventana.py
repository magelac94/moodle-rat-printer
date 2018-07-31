import tkinter.filedialog as fd
from tkinter import filedialog
from tkinter import *
from lxml import etree
import html
import re
import xml.etree.ElementTree as ET
#import time
from ToPDF import convertir
#import ToPDF.py



def strip_tags(value):
	return re.sub(r'<[^>]*?>','',value)

def manejoDatos(archivo):
	
	gridQuiz = []
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
	#quiz=raiz[0]	#Primer elemento

	tree = ET.parse(archivo)
	root = tree.getroot()

	# Cantidad de Preguntas
	cantidadPreguntas = len(root)
	print ("Cantidad de Preguntas del test ", cantidadPreguntas)

	cantidadRespuestasMax = 20
	
	
	for j in range(cantidadPreguntas):
		gridQuiz.append([])
		for h in range(cantidadRespuestasMax):
			gridQuiz[j].append(None)

	i = 0
	for cuestion in root.findall('question'):

		tipopregunta = cuestion.get('type')

		if tipopregunta == "category":
			cantidadPreguntas = cantidadPreguntas - 1
			i = i - 1
		else:
			titulo = cuestion.find("name/text").text
			pregunta = strip_tags(cuestion.find("questiontext/text").text)
			tipopregunta = cuestion.get('type')
			#imagen = resolvertipopregunta = cuestion.get('type')
			respuesta1 = strip_tags(cuestion.find("answer/text").text)

			# Respuestas de la Pregunta
			k = 5 
			for elt in cuestion.getiterator("answer"):
				respuesta = strip_tags(elt.find("text").text)
				gridQuiz[i][k]=respuesta
			#	print (gridQuiz[i][k])
				k = k + 1
			cantidadRespuestas = k-5

			gridQuiz[i][0]= titulo
			gridQuiz[i][1]= pregunta
			gridQuiz[i][2] = tipopregunta
		#	gridQuiz[i][3] = imagen
			gridQuiz[i][4] = cantidadRespuestas

			print ("Titulo Pregunta: ",gridQuiz[i][0])
			print( "Texto Pregunta: ",gridQuiz[i][1])
			print ("Tipo de Pregunta: ", gridQuiz[i][2])
			print ("Cantidad de Respuestas",gridQuiz[i][4])
			
			for p in range (5,5+cantidadRespuestas):
				print ("Respuesta :",gridQuiz[i][p])
			i = i + 1
			print("------------------------------------------------")

	return gridQuiz

def imprimirPDF(lista):
	convertir(lista)


def abrirXML():
 	archivo=fd.askopenfilename()	# Abre ventana para seleccionar archivo, devuelve la ruta del archivo	
 	datos = manejoDatos(archivo)
 	imprimirPDF(datos)

	

	
ventana=Tk()
ventana.title("TBL Printer")
ventana.config(bg="#0B0B61")
ventana.geometry("300x400")
botonAbrir=Button(ventana,text="Seleccionar archivo", command=abrirXML)
botonAbrir.grid(padx=100,pady=100)
ventana.mainloop()