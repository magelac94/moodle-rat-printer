import tkinter.filedialog as fd
from tkinter import filedialog
from tkinter import *
from lxml import etree
import html
import re
def strip_tags(value):
	return re.sub(r'<[^>]*?>','',value)

def abrirXML():
	 
	gridQuiz = [[0,1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]]	# Estructura donde se guardaran las preguntas
	# gridQuiz[x][] # numero pregunta
	# gridQuiz[][0]	# Titulo
	# gridQuiz[][1]	# Pregunta
	# gridQuiz[][2]	# Tipo de Pregunta
	# gridQuiz[][3]	# Imagen
	# gridQuiz[][4]	# Respuesta 1
	# gridQuiz[][5]	# Respuesta 2
	# gridQuiz[][6]	# Respuesta 3 ...



	archivo=fd.askopenfilename()	# Abre ventana para seleccionar archivo, devuelve la ruta del archivo	

	doc = etree.parse(archivo)	# Se guarda contenido de archivo xml en un arbol de la lib lxml	

	raiz=doc.getroot() 	#Obtener elemento raiz

	print ("Cantidad de Preguntas del test ", len(raiz))	# Elementos hijos de la raiz = cantidad de preguntas

	quiz=raiz[0]	#Primer elemento

	# Titulo opcional
	gridQuiz[0][0]= 2	# agregar titulo pregunta

	# Texto de la Pregunta
	preguntas = doc.findall("question")
	p1 = strip_tags(preguntas[0].find("questiontext/text").text)
	gridQuiz[0][1]= p1
	print ("PREGUNTA EN LISTA")
	print(gridQuiz[0][1])

	# Tipo de pregunta	
	print ("Tipo de Pregunta")
	gridQuiz[0][2] = "Soy el tipo de Pregunta"   # agregar tipo de pregunta


	# Imagen
	print ("Imagen")
	gridQuiz[0][3] = "Soy el tipo de Pregunta"   # agrgar imagen si hay


	# Texto 1era Respuesta
	print ("Respuesta 1")
	r1=strip_tags(preguntas[0].find("answer/text").text)
	gridQuiz[0][4]=r1
	print (gridQuiz[0][4])


	

ventana=Tk()
ventana.title("TBL Printer")
ventana.config(bg="#0B0B61")
ventana.geometry("300x400")
botonAbrir=Button(ventana,text="Seleccionar archivo", command=abrirXML)
botonAbrir.grid(padx=100,pady=100)
ventana.mainloop()