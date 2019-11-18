import xml.etree.ElementTree as myxml

root = myxml.Element("catalogue")
child = myxml.SubElement(root,"book",{"id":"419"})
subchild1 = myxml.SubElement(child,"author")
subchild2 = myxml.SubElement(child, "title")
subchild1.text = "Amolegbe Kola"
subchild2.text = "Python 3 Evolution"

child = myxml.SubElement(root, "book", {"id":"197"})
subchild1 = myxml.SubElement(child,"author")
subchild2 = myxml.SubElement(child, "title")
subchild1.text = "Mike Daniels"
subchild2.text = "HTML5 in programming"

child = myxml.SubElement(root, "book", {"id":"108"})
subchild1 = myxml.SubElement(child,"author")
subchild2 = myxml.SubElement(child, "title")
subchild1.text = "Pelumi Adebogun"
subchild2.text = "Javascript Storm"

catalogTree =myxml.ElementTree(root)
catalogTree.write("programmingbooks.xml")