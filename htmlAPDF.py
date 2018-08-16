from xhtml2pdf import pisa             # import python module

# Utility function
def conv(sourceHtml1, outputFilename):
    # open output file for writing (truncated binary)

    resultFile = open(outputFilename, "w+b")

    pisaStatus3 = pisa.CreatePDF(
            sourceHtml1,                # the HTML to convert
            dest=resultFile) 



    # close output file
    resultFile.close()                 # close output file

    # return True on success and False on errors
#    return pisaStatus.err

# Main program
#convertirHTMLtoPDF( datos[0], directorioDestino, nombrePrueba,descripcion,tipoLetra,itituloPrueba,inumeroPregunta,itituloPregunta,idescripcion)
def convertirHTMLtoPDF(datos, directorioDestino, 
    nombrePrueba,descripcion,tipoLetra,itituloPrueba,
    inumeroPregunta,itituloPregunta,idescripcion):
    print (" que hay en datos [2]: ", datos[2])
    sourceHtml1 = str(datos[2][1]) # datos[2]
    outputFilename = "test.pdf"

    pisa.showLogging()
    conv(sourceHtml1, outputFilename)