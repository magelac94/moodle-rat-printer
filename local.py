from lxml import etree

doc = etree.parse("lo.xml")
raiz=doc.getroot()

for provincia in raiz:
    nombre, localidades = provincia.getchildren()
    print('\nProvincia: {} {}\n  Localidades:'.format(nombre.text, provincia.attrib['id']))
    for localidad in localidades:
        print('    {} {}'.format(localidad.text, provincia.attrib['id']))



        print("Nuevas Pruebas")
	tree = ET.parse(archivo)
	roott = tree.getroot()

	print("Root tag")
	print(roott.tag)
	print("Root attrib")
	print(roott.attrib)

	print("HIJOS")
	for child in roott:
		print (child.tag, child.attrib)

	print (roott[0][1].text)
	
	for neighbor in roott.iter('name'):
		print (neighbor.tag, neighbor.attrib, neighbor.text)