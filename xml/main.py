import xml.dom.minidom
import urllib.request
import xml.etree.cElementTree as ET


import xml.dom.minidom as minidom

import xml.etree.ElementTree as xml

class XML:
 def __init__(self):
        self.data = [["1", "Moscow ", "Khabarovsk ", "8 ", '9 ',"CY-23"], ["2", "Moscow ", "Khabarovsk ", "8 ", '9 ',"CY-23"],
                     ["3", "Moscow ", "Khabarovsk ", "8 ", '9 ',"TY_106"], ["4", "Moscow ", "Khabarovsk ", "8 ", '9 ',"TY_1206"],
                     ["6", "Moscow ", "Khabarovsk ", "8 ", '9 ',"TY_1206"], ["4", "Moscow ", "Khabarovsk ", "8 ", '9 ',"BB2689"],
                     ["6", "Moscow ", "Khabarovsk ", "8 ", '3 ',"BB689"]]
        self.url="appct1.xml"
 def createXML(self):
    root = xml.Element("scoreboard")


    for i in  self.data:
        print(i)

        appt = xml.Element("flight")
        id = xml.SubElement(appt, "id ")
        id.text = i[0]
        froms = xml.SubElement(appt, "from")
        froms.text = i[1]
        where = xml.SubElement(appt, "where")
        where.text = i[2]
        landing = xml.SubElement(appt, "landing")
        landing.text = i[3]
        arrival = xml.SubElement(appt, "arrival")
        arrival.text = i[4]
        arrival = xml.SubElement(appt, "type")
        arrival.text = i[5]
        root.append(appt)
        tree = xml.ElementTree(root)

        with open(self.url, "wb") as fh:
                tree.write(fh)


 def deserialization(self):

    tree = ET.parse(self.url)
    root = tree.getroot()
    print(root[0][2].text)


    dom = minidom.parse(self.url)
    elements = dom.getElementsByTagName('flight')


    for i in range(0 ,len(elements)):

        print(root[i][0].text,root[i][1].text,root[i][2].text,root[i][3].text,root[i][4].text,root[i][5].text)





if __name__ == "__main__":
  

    x = XML().createXML()
    x = XML().deserialization()
