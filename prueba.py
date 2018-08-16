from xhtml2pdf import pisa             # import python module

# Define your data
sourceHtml1 = "<html><body><p>To PDF or not to <b>PDF</b></p></body></html>"
sourceHtml2 = "<html><body><p>To PDF or not to <b>PDF</b></p></body></html>"

outputFilename = "test.pdf"

# Utility function
def convertHtmlToPdf(sourceHtml1,sourceHtml2, outputFilename):
    # open output file for writing (truncated binary)
  
    resultFile = open(outputFilename, "a")

    # convert HTML to PDF
    pisaStatus = pisa.CreatePDF(
            sourceHtml1,                # the HTML to convert
            dest=resultFile)           # file handle to recieve result

    resultFile.close()                 # close output file

    resultFile = open(outputFilename, "w+b")

    pisaStatus3 = pisa.CreatePDF(
            sourceHtml2,                # the HTML to convert
            dest=resultFile) 



    # close output file
    resultFile.close()                 # close output file

    # return True on success and False on errors
    return pisaStatus.err

# Main program
if __name__ == "__main__":
    pisa.showLogging()
    convertHtmlToPdf(sourceHtml1,sourceHtml2, outputFilename)