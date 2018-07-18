import tkinter.filedialog as fd
from tkinter import filedialog
from tkinter import *
from lxml import etree
def abrir():
	
# Abre ventana para seleccionar archivo, devuelve la ruta del archivo 
	archivo=fd.askopenfilename()	
	print("soy el archivo" + str(archivo))   # imprimo ruta del archivo

# Abro archivo y guardo su contenido en una lista que contiene las lineas del archivo
   #contenido = open(archivo,'r')
   #lista = contenido.readlines()

 	# Imprimo las lineas del archivo
	#  cont = 0
	 #  for linea in lista:
	 #  	cont +=1
	 #  	print(cont,linea)

# Cierro archivo
	#contenido.close


# Guardo contenido de archivo xml en un arbol de la lib lxml	
	doc = etree.parse(archivo)
   #print etree.tostring(doc,pretty_print=True ,xml_declaration=True, encoding="utf-8")

 #Obtener elemento raiz
	print ("RAIZ")
	raiz=doc.getroot()
	print (raiz.tag)

# Elementos hijos de la raiz
	print (" CANTIDAD DE HIJOS")
	print (len(raiz))

 #Primer elemento
	quiz=raiz[0]
	#print (quiz.tag)
	#print (quiz[0].tag)
 
	#print ("QUESTIONTEXT " )
	#print (quiz.get("questiontext"))
	# Devuelve UN precio
	#precio = quiz.find("questiontext")

	# Texto de la Pregunta
	preguntas = doc.findall("question")
	print (preguntas[0].find("questiontext/text").text)

	# Texto 1era Respuesta
	print (preguntas[0].find("answer/text"))

# Devuelve text del primer elemento
	#print (quiz.findtext("questiontext"))

	# iterar ascendentemente para obtener padre o abuelo
	#for padre in quiz.iterancestors():
	#	print (padre.tag)

	#o=etree.fromstring(archivo)
	# get childrens
	#for hijo in quiz.getchildren():
	#	print (hijo.tag)

  


ventana=Tk()
ventana.title("TBL Printer")
ventana.config(bg="#0B0B61")
ventana.geometry("300x400")
botonAbrir=Button(ventana,text="Seleccionar archivo", command=abrir)
botonAbrir.grid(padx=100,pady=100)
ventana.mainloop()