# ToPDF funcion auxiliar para TBLPrinter
# Desarrollado por Magela Carballo - Agosto 2018

import time
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_RIGHT, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfgen import *

# LISTA DE PREGUNTAS
# Estructura donde se guardaran las preguntas /
    # gridQuiz[x][] # numero pregunta
    # gridQuiz[][0] # Titulo
    # gridQuiz[][1] # Pregunta
    # gridQuiz[][2] # Tipo de Pregunta
    # gridQuiz[][3] # Imagen
    # gridQuiz[][4] # Cantidad de Respuestas
    # gridQuiz[][5] # Respuesta 1
    # gridQuiz[][6] # Respuesta 2
    # gridQuiz[][7] # Respuesta 3 ...
 
 # Funcion que recibe matriz con las preguntas y respuestas y
 # genera un archivo PDF con las preguntas formateadas
def convertir(listaPreguntas,destino):
    Prueba=[]                                               # Lista con lineas del archivo
    diaHora = time.ctime()                                  # Hora actual
    nombrePrueba = "PROGFUN-RAT1 Lenguaje funcional básico" # Nombre de la prueba
    descripcion = ""                                        # Descripcion - Opcional
    nombreArchivo = destino+"/"+nombrePrueba +".pdf"         # nombre archivo

    documento = SimpleDocTemplate(nombreArchivo,pagesize=letter,
                        rightMargin=72,leftMargin=72,
                        topMargin=50,bottomMargin=18)
 
    # DIA Y HORA
    estiloFecha=getSampleStyleSheet()
    estiloFecha.add(ParagraphStyle(name='Right', alignment=TA_RIGHT))
    lineaFecha = '<font size=9>%s</font>' % diaHora
    Prueba.append(Paragraph(lineaFecha, estiloFecha["Normal"]))
    Prueba.append(Spacer(1, 12))

    #Nombre y CI
    estiloCI=getSampleStyleSheet()
    estiloCI.add(ParagraphStyle(name='Center', alignment=TA_CENTER))
    lineaCI = '<font size=9>Nombre y Apellido _____________________________________       CI ________________________  </font>'
    Prueba.append(Paragraph(lineaCI, estiloCI["Normal"]))
    Prueba.append(Spacer(1, 12))
 
    # NOMBRE DE LA PRUEBA
    estiloTitulo=getSampleStyleSheet()
    estiloTitulo.add(ParagraphStyle(name='Center', alignment=TA_CENTER))
    lineaTitulo = '<font size=13>%s</font>' % nombrePrueba
    Prueba.append(Paragraph(lineaTitulo, estiloTitulo["Normal"]))  
    Prueba.append(Spacer(1, 12))

    # Descripcion de la Prueba (Opcional)
    estiloDescripcion=getSampleStyleSheet()
    estiloDescripcion.add(ParagraphStyle(name='Center', alignment=TA_CENTER, fontName='Arial'))
    lineaDescripcion = '<font size=11>%s</font>' % descripcion
    Prueba.append(Paragraph(lineaDescripcion, estiloDescripcion["Normal"]))  
    Prueba.append(Spacer(1, 12))


    # Preguntas y Respuestas
    estiloTituloPregunta=getSampleStyleSheet()
    estiloTituloPregunta.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))

    estiloPregunta=getSampleStyleSheet()
    estiloPregunta.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))

    estiloRespuesta=getSampleStyleSheet()
    estiloRespuesta.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))

    estiloNumPregunta=getSampleStyleSheet()
    estiloNumPregunta.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))

    numPreg = 1

    for pregunta in listaPreguntas:
        if pregunta[4] != None:

            # Numero Pregunta
            lineaNumeroPregunta = '<font size=9>Pregunta %s</font>' % numPreg
            Prueba.append(Paragraph(lineaNumeroPregunta, estiloNumPregunta["Normal"])) 

            #Titulo de la Pregunta - Opcional
            lineaTituloPregunta = '<font size=11>%s</font>' % pregunta[0]
            Prueba.append(Paragraph(lineaTituloPregunta, estiloTituloPregunta["Normal"])) 
            Prueba.append(Spacer(1, 6))

            #Texto de la Pregunta
            lineaPregunta = '<font size=12>%s</font>' % pregunta[1]
            Prueba.append(Paragraph(lineaPregunta, estiloPregunta["Normal"])) 
            Prueba.append(Spacer(1, 12))

            # Respuestas
            tipopregunta = pregunta[2]
            if tipopregunta == "enssay":
                Prueba.append(Spacer(1, 100))
                line = '<font size=11>__ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __  </font>'
                Prueba.append(Paragraph(line, estiloRespuesta["Normal"]))
                Prueba.append(Spacer(1, 12))
            elif tipopregunta == "matching":
                line = '<font size=11>--Error al mostrar tipo de pregunta matching>--Consulte al docente</font>'
                Prueba.append(Paragraph(line, estiloRespuesta["Normal"]))
                Prueba.append(Spacer(1, 12))

            else:
                p = 5+pregunta[4]

                for i in range(5,p):
                    lineaRespuesta = '<font size=11>O %s</font>' % pregunta[i]
                    Prueba.append(Paragraph(lineaRespuesta, estiloRespuesta["Normal"]))
                    Prueba.append(Spacer(1, 6))
                Prueba.append(Spacer(1, 12))

            numPreg = numPreg + 1         

    documento.build(Prueba)     # Generacion del documento

# Funcion que recibe lista de tuplas con el numero de pregunta y
# La respueta correcta de esa pregunta
def imprimirRespuestas(listaRespuestas, destino):
    Prueba=[]                                                        # Lista lineas archivo
    diaHora = time.ctime()                                           # Hora actual

    nombrePrueba = "PROGFUN-RAT1 Lenguaje funcional básico -  RESPUESTAS"   # nombre prueba
    nombreArchivo = destino+"/"+nombrePrueba +".pdf"                                    # nombre archivo

    documento = SimpleDocTemplate(nombreArchivo,pagesize=letter,
                        rightMargin=72,leftMargin=72,
                        topMargin=50,bottomMargin=18)

    # DIA Y HORA
    estiloFecha=getSampleStyleSheet()
    estiloFecha.add(ParagraphStyle(name='Right', alignment=TA_RIGHT))
    lineaFecha = '<font size=9>%s</font>' % diaHora
    Prueba.append(Paragraph(lineaFecha, estiloFecha["Normal"]))
    Prueba.append(Spacer(1, 12))

    # NOMBRE DE LA PRUEBA
    estiloTitulo=getSampleStyleSheet()
    estiloTitulo.add(ParagraphStyle(name='Center', alignment=TA_CENTER))
    lineaTitulo = '<font size=13>%s</font>' % nombrePrueba
    Prueba.append(Paragraph(lineaTitulo, estiloTitulo["Normal"]))  
    Prueba.append(Spacer(1, 12))

    # Preguntas y Respuestas
    estiloLinea=getSampleStyleSheet()
    estiloLinea.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY, fontName="Arial"))

    for pregunta in listaRespuestas:
        lineaRespuesta = '<font size=10>Pregunta %s - R: %s</font>' % (pregunta[0]+1 , pregunta[1])
        Prueba.append(Paragraph(lineaRespuesta, estiloLinea["Normal"])) 
        Prueba.append(Spacer(1, 10))   

    documento.build(Prueba)         # Generacion de Archivo