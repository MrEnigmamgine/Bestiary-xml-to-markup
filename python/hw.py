from xml.dom import minidom

file= open('./test/test.txt','w+')
for i in range(10):
     file.write("This is line %d\r\n" % (i+1))

file.close()

import xml.etree.ElementTree as ET  
xmlp = ET.XMLParser(encoding='ISO-8859-1')

tree= ET.parse('test.xml',parser=xmlp)
root = tree.getroot()
print(root.tag)
if(root.find('items')):{
    print('Found items') #Works
}
if('items' in root):{
    print('Items in root') #doesn't work
}
for e in root:
    if(e.find('item')):{
        print('Found item') #Never prints
    }
    if(e.find('findme')):{
        print('Found findme') #Never prints
    }
    t = e.find('findme').text 
    print(t) #does print
    print(list(e))
