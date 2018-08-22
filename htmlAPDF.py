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
        <body style="font-size:12px"> 
        <div><img src="data:image/jpg;base64,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" /></div>
  
        """
#<img src="C://Users//Magela//Documents//GitHub//moodle-rat-printer//Archivos//gar.jpg"></div> 
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

    htmlcode = htmlcode + """   </body> </html>"""
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

