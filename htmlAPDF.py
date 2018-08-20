from xhtml2pdf import pisa             # import python module
import time

def txtToHtml(listaPreguntas,nombrePrueba,descripcion,tipoLetra,itituloPrueba,inumeroPregunta,itituloPregunta,idescripcion):
     # gridQuiz[x][] # numero pregunta
    # gridQuiz[][0] # Titulo
    # gridQuiz[][1] # Pregunta
    # gridQuiz[][2] # Tipo de Pregunta
    # gridQuiz[][3] # Imagen
    # gridQuiz[][4] # Cantidad de Respuestas
    # gridQuiz[][5] # Respuesta 1
    # gridQuiz[][6] # Respuesta 2
    # gridQuiz[][7] # Respuesta 3 ...
    htmlcode = """
    <html>
        <head>
            <title>Testing</title>
            <meta http-equiv="content-type" content="text/html; charset=utf-8">
        </head>
        <body style="font-size:12px"> 
    """

    espacios10 = """
        <p> </p>
        <p> </p>
        <p> </p>
        <p> </p>
        <p> </p>
        <p> </p>
        <p> </p>
        <p> </p>
        <p> </p>
        <p> </p>
    """

    linesolid = """<p style="font-size:15px">_______________________________________________________________________________________</p>"""
    
    #formato = """<p style="font-family: calibri; font-size: 20px">This is some text!</p>"""  style="font-size:15px"
    #htmlcode = htmlcode + formato

    #Nombre y CI
    lineaCI = """<p style="font-size:10px">Nombre y Apellido _____________________________________       CI ________________________ </p>"""
    htmlcode = htmlcode + lineaCI
    #Dia y Hora
    diaHora = time.ctime() 
    htmlcode = htmlcode + """<p style="font-size:10px">""" + diaHora + "</p>"
    #NOmbre de la Prueba - OPCIONAL
    if (itituloPrueba == True):
        htmlcode = htmlcode + """<p style="font-size:13px">""" + nombrePrueba + "</p>"
    # Descripcion de la Prueba - OPCIONAL
    if (idescripcion == True):
        htmlcode = htmlcode + """<p style="font-size:11px">""" + descripcion + "</p>"
    # Preguntas y Respuestas
    numPreg = 1
    for pregunta in listaPreguntas:
        if pregunta[4] != None:

            # Numero Pregunta - Opcional
            if (inumeroPregunta == True):
                htmlcode = htmlcode + """<p style="font-size:10px">""" + numPreg + "</p>"

            #Titulo de la Pregunta - Opcional
            if (itituloPregunta == True):
                htmlcode = htmlcode + """<p style="font-size:12px">""" + pregunta[0] + "</p>"

            #Texto de la Pregunta 
            htmlcode = htmlcode + pregunta[1]

            # Respuestas
            tipopregunta = pregunta[2]
            if tipopregunta == "enssay":
                htmlcode = htmlcode + espacios10
            elif tipopregunta == "matching":
                line = """<p style="font-size:11px">Error al mostrar tipo de pregunta matching -- Consulte al docente </p>"""
                htmlcode = htmlcode + line
            else:
                p = 5+pregunta[4]
                htmlcode = htmlcode + """<ul type="square">"""
                for i in range(5,p):
                    # cuadrado blanco  U+25A1
                    htmlcode = htmlcode + "<li>" +pregunta[i] + "</li>"
                htmlcode = htmlcode + "</ul>"

            htmlcode = htmlcode + linesolid
            
            numPreg = numPreg + 1     

    return htmlcode

# Utility function
def convertHtmlToPdf(html, outputFilename):
    # open output file for writing (truncated binary)
#    textHtml = txtToHtml(datos)
    resultFile = open(outputFilename, "w+b")

    # convert HTML to PDF
    pisaStatus = pisa.CreatePDF(
            html,                # the HTML to convert
            dest=resultFile)           # file handle to recieve result

    #pisa.CreatePDF(cont.encode, pdf_out, encoding='utf-8')


    resultFile.close()                 # close output file
    
    # return True on success and False on errors
    return pisaStatus.err

def pasarPDF(datos, outputFilename,nombrePrueba,descripcion,tipoLetra,itituloPrueba,inumeroPregunta,itituloPregunta,idescripcion):
    htmlcode = txtToHtml(datos,nombrePrueba,descripcion,tipoLetra,itituloPrueba,inumeroPregunta,itituloPregunta,idescripcion)
    convertHtmlToPdf(htmlcode,outputFilename)
    pisa.startViewer(outputFilename)
# Main program
#if __name__ == "__main__":
#    pisa.showLogging()
#    convertHtmlToPdf(html, outputFilename)
 #   pisa.startViewer(outputFilename)

