import tkinter.filedialog as fd
from tkinter import filedialog
from tkinter import *
def abrir():
  # ruta=fd.askdirectory()
   archivo=fd.askopenfilename()
   print("soy el archivo" + str(archivo))
   contenido = open(archivo,'r')
   lista = contenido.readlines()

   cont = 0
   for linea in lista:
   	cont +=1
   	print(cont,linea)

   #print(linea)

   contenido.close



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