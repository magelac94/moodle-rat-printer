from xhtml2pdf import pisa             # import python module

#import ho.pisa as pisa
import io
from io import StringIO
import sys

def main():
	data = """
	<html>
    	<head>
        	<title>Testing</title>
        	<meta http-equiv="content-type" content="text/html; charset=utf-8">
    	</head>
    	<body>
        	<p>%s</p>
    	</body>	
	</html>
	"""

	text = ""
	for line in sys.stdin:
    	text = text + line

	pisa.pisaDocument(StringIO.StringIO(data % text), file('final.pdf', 'w'), encoding='UTF-8') 

main()