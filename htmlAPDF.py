from xhtml2pdf import pisa             # import python module
import time

def txtToHtml(listaPreguntas,nombrePrueba,descripcion,inumeroPregunta,idescripcion):
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
            <title>Quiz</title>
            <meta http-equiv="content-type" content="text/html; charset=utf-8">
        <body style="font-size: 12px">              
         """
    espacios10 = """
        <br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>

    """

    boxp = """<img src="data:image/png;base64,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" />"""
    linesolid = """<span style="font-size:15px">_______________________________________________________________________________________</span><br><br>"""
    
    # Fecha
    diaHora = time.strftime("%d/%m/%y")
    
    #Nombre y CI
    lineaCI = """<span style="font-size:12px">Nombre y Apellido __________________________________________________       CI _____________________________        """ + diaHora + "</span>"
    
    htmlcode = htmlcode + lineaCI
    
    #NOmbre de la Prueba - OPCIONAL por defecto es el nombre del archivo origen
    htmlcode = htmlcode + """<H1 align="center">""" + nombrePrueba + "</h1>"

    # Descripcion de la Prueba - OPCIONAL
    if (idescripcion == True):
        htmlcode = htmlcode + """<span style="font-size:11px">""" + descripcion + "</span><br>"
    
    # Preguntas y Respuestas
    numPreg = 1
    for pregunta in listaPreguntas:
        if pregunta[4] != None:

            # Numero Pregunta - Opcional
            if (inumeroPregunta == True):
                pregnumero = "Pregunta " + str(numPreg)
                htmlcode = htmlcode + """<strong style="font-size:12px">""" + pregnumero + "</strong><br>"

            #Texto de la Pregunta 
            preguntaTexto = pregunta[1].replace("<p>", """<p style="display: inline">""")
            preguntaTexto = preguntaTexto.replace("<pre>", """<pre style="display: inline">""")
            preguntaTexto = preguntaTexto.replace("<br>", "") # elimino etiquetas br
            preguntaTexto = preguntaTexto.replace("<p>&nbsp;</p>", "")
            preguntaTexto = preguntaTexto.replace("</p>", "</p><br>")
            preguntaTexto = preguntaTexto.replace("</pre>", "</pre><br>")
            htmlcode = htmlcode + preguntaTexto

            # Imagen de la Pregunta
            if pregunta[3] != "" :
                lineaimagen =  """<div align="center"><img src="data:image/png;base64,""" + pregunta[3] + """ "/></div><br>"""
                htmlcode = htmlcode + lineaimagen

            # Respuestas
            tipopregunta = pregunta[2]
            if tipopregunta == "essay":
                htmlcode = htmlcode + espacios10
            elif tipopregunta == "matching":
                line = """<span style="font-size:11px">Error al mostrar tipo de pregunta matching -- Consulte al docente </span></br>"""
                htmlcode = htmlcode + line
            else:
                p = 5+pregunta[4]
                for i in range(5,p):
                    preguntaM = pregunta[i].replace("<br>", "") # elimino etiquetas br
                    preguntaM = preguntaM.replace("<br />", "") # elimino etiquetas br
                    preguntaM = preguntaM.replace("</p>", "") # elimino etiquetas p
                    preguntaM = preguntaM.replace("<pre>", """<pre style="display: inline">""")

                    if preguntaM.find("<p>") == -1:
                        preguntaModificada = boxp + "<span>" + preguntaM + "</span>"
                    else:
                        parte1=preguntaM[:15].replace("<p>", boxp)  # agrego imagen al inicio
                        parte2=preguntaM[15:]       
                        preguntaModificada = parte1+parte2
                    htmlcode = htmlcode + """<span style="line-height: 1.2">""" + preguntaModificada + "</span><br>"  #agrego etiqueta span

            htmlcode = htmlcode + linesolid
            
            numPreg = numPreg + 1     
    htmlcode = htmlcode + """   </body> </html>"""
    return htmlcode

def convertHtmlToPdf(html, outputFilename):
    resultFile = open(outputFilename, "w+b")

    # convert HTML to PDF
    pisaStatus = pisa.CreatePDF(
            html,                # the HTML to convert
            dest=resultFile)           # file handle to recieve result

    resultFile.close()                 # close output file
    
    # return True on success and False on errors
    return pisaStatus.err

def pasarPDF(datos, outputFilename,nombrePrueba,descripcion,inumeroPregunta,idescripcion):
    htmlcode = txtToHtml(datos,nombrePrueba,descripcion,inumeroPregunta,idescripcion)
    convertHtmlToPdf(htmlcode,outputFilename)
    pisa.startViewer(outputFilename)