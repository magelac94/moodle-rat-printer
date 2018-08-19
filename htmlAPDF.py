from xhtml2pdf import pisa             # import python module
import time


# Define your data
#html = ""<html><p><meta charset=utf-8"><body><p>To PDF or not to <b>PDF</b></p></body></html>""
html = """
    <html>
        <head>
            <title>Testing</title>
            <meta http-equiv="content-type" content="text/html; charset=utf-8">
        </head>
        <body>
        <p>En el lenguaje Haskell, ¿a qué se le llama una <i>definición</i>?<br></p>
        <p>A una asociación de un nombre (identificador) con un valor de un tipo particular.</p>
        <p>A la asociación de un nombre (identificador) con su tipo.</p>
        <p>A la declaración de una función.</p>
        <p>A la firma de una función.</p>
        </body>
    </html>
    """
outputFilename = "test.pdf"

def txtToHtml(datos):
     # gridQuiz[x][] # numero pregunta
    # gridQuiz[][0] # Titulo
    # gridQuiz[][1] # Pregunta
    # gridQuiz[][2] # Tipo de Pregunta
    # gridQuiz[][3] # Imagen
    # gridQuiz[][4] # Cantidad de Respuestas
    # gridQuiz[][5] # Respuesta 1
    # gridQuiz[][6] # Respuesta 2
    # gridQuiz[][7] # Respuesta 3 ...
    htmlcode = """ """

    #Dia y Hora
    diaHora = time.ctime() 
    htmlcode = htmlcode ++ "<p>" ++ diaHora ++ "</p>"

# Utility function
def convertHtmlToPdf(html, outputFilename):
    # open output file for writing (truncated binary)
    textHtml = txtToHtml(datos)
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
    htmlcode = txtToHtml(datos, outputFilename,nombrePrueba,descripcion,tipoLetra,itituloPrueba,inumeroPregunta,itituloPregunta,idescripcion)
    convertHtmlToPdf(htmlcode,outputFilename)
# Main program
if __name__ == "__main__":
    pisa.showLogging()
    convertHtmlToPdf(html, outputFilename)
    pisa.startViewer(outputFilename)

