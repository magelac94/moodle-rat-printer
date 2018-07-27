import tkinter.filedialog as fd
from tkinter import filedialog
from tkinter import *
from lxml import etree
import html
import re
import xml.etree.ElementTree as ET
def strip_tags(value):
	return re.sub(r'<[^>]*?>','',value)

def manejoDatos(archivo):
	gridQuiz = [[0,1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]]	# Estructura donde se guardaran las preguntas
	# gridQuiz[x][] # numero pregunta
	# gridQuiz[][0]	# Titulo
	# gridQuiz[][1]	# Pregunta
	# gridQuiz[][2]	# Tipo de Pregunta
	# gridQuiz[][3]	# Imagen
	# gridQuiz[][4]	# Respuesta 1
	# gridQuiz[][5]	# Respuesta 2
	# gridQuiz[][6]	# Respuesta 3 ...


	tree = ET.parse(archivo)
	root = tree.getroot()
	
	print ("Cantidad de Preguntas del test ", len(root))	# Elementos hijos de la raiz = cantidad de preguntas

	#quiz=raiz[0]	#Primer elemento

	for cuestion in root.findall('question'):
		titulo = cuestion.find('name/text').text
		pregunta = strip_tags(cuestion.find('questiontext/text').text)
		tipopregunta = cuestion.get('type')
		#imagen = resolver
		respuesta1 = strip_tags(cuestion.find("answer/text").text)

		gridQuiz[0][0]= titulo
		gridQuiz[0][1]= pregunta
		gridQuiz[0][2] = tipopregunta
	#	gridQuiz[0][3] = imagen
		gridQuiz[0][4] = respuesta1


		print ("Titulo Pregunta: ",gridQuiz[0][0])
		print( "Texto Pregunta: ",gridQuiz[0][1])
		print ("Tipo de Pregunta: ", gridQuiz[0][2])
		print ("Respuesta1: ", gridQuiz[0][4])

def abrirXML():
 	archivo=fd.askopenfilename()	# Abre ventana para seleccionar archivo, devuelve la ruta del archivo	
 	manejoDatos(archivo)
	

	
ventana=Tk()
ventana.title("TBL Printer")
ventana.config(bg="#0B0B61")
ventana.geometry("300x400")
botonAbrir=Button(ventana,text="Seleccionar archivo", command=abrirXML)
botonAbrir.grid(padx=100,pady=100)
ventana.mainloop()