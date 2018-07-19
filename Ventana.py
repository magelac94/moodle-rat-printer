import tkinter.filedialog as fd
from tkinter import filedialog
from tkinter import *
from lxml import etree
def abrir():
	
# Abre ventana para seleccionar archivo, devuelve la ruta del archivo 
	archivo=fd.askopenfilename()	
	print("soy el archivo" + str(archivo))   # imprimo ruta del archivo

# Guardo contenido de archivo xml en un arbol de la lib lxml	
	doc = etree.parse(archivo)

 #Obtener elemento raiz
	print ("RAIZ")
	raiz=doc.getroot()
	print (raiz.tag)

# Elementos hijos de la raiz
	print (" CANTIDAD DE HIJOS")
	print (len(raiz))

 #Primer elemento
	quiz=raiz[0]

	# Texto de la Pregunta
	preguntas = doc.findall("question")
	print ("Pregunta ")
	print (preguntas[0].find("questiontext/text").text)

	# tipo de pregunta
	print ("Tipo de Pregunta")
	
	# Texto 1era Respuesta
	print ("Respuesta 1")
	print (preguntas[0].find("answer/text").text)

ventana=Tk()
ventana.title("TBL Printer")
ventana.config(bg="#0B0B61")
ventana.geometry("300x400")
botonAbrir=Button(ventana,text="Seleccionar archivo", command=abrir)
botonAbrir.grid(padx=100,pady=100)
ventana.mainloop()