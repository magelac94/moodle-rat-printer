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

# Obtener elemento raiz
   raiz=doc.getroot()
   print (raiz.tag)

# Elementos hijos de la raiz
	#len (raiz)

 
  

 





 #  open(archivo,"r")
 #  archivo = open("r")
 #  lines = archivo.read()
 # print (str(lines))


ventana=Tk()
ventana.title("TBL Printer")
ventana.config(bg="#0B0B61")
ventana.geometry("300x400")
botonAbrir=Button(ventana,text="Seleccionar archivo", command=abrir)
botonAbrir.grid(padx=100,pady=100)
ventana.mainloop()