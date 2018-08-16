from xhtml2pdf import pisa             # import python module

# Define your data
sourceHtml1 = "<html><body><p>To PDF or not to <b>PDF</b></p></body></html>"
sourceHtml2 = "<html><body><p>To PDF or not to <b>PDF</b></p></body></html>"
html = "<p><meta http-equiv="Content-Type" content="text/html; charset=utf-8">En el lenguaje Haskell, ¿a qué se le llama una <i>definición</i>?<br></p><p>A una asociación de un nombre (identificador) con un valor de un tipo particular.<br></p><p>A la asociación de un nombre (identificador) con su tipo.<br></p><p>A la declaración de una función.<br></p><p>A la firma de una función.<br></p>"

outputFilename = "test.pdf"

# Utility function
def convertHtmlToPdf(html, outputFilename):
    # open output file for writing (truncated binary)
  
    resultFile = open(outputFilename, "w+b")

    # convert HTML to PDF
    pisaStatus = pisa.CreatePDF(
            html,                # the HTML to convert
            dest=resultFile)           # file handle to recieve result

    resultFile.close()                 # close output file
    
    # return True on success and False on errors
    return pisaStatus.err

# Main program
if __name__ == "__main__":
    pisa.showLogging()
    convertHtmlToPdf(html, outputFilename)