import xml.dom.minidom
import urllib.request
import xml.etree.cElementTree as ET


import xml.dom.minidom as minidom

import xml.etree.ElementTree as xml
import json


data = [["1", "Moscow ", "Khabarovsk ", "8 ", '9 ',"CY-23"], ["2", "Moscow ", "Khabarovsk ", "8 ", '9 ',"CY-23"],
                     ["3", "Moscow ", "Khabarovsk ", "8 ", '9 ',"TY_106"], ["4", "Moscow ", "Khabarovsk ", "8 ", '9 ',"TY_1206"],
                     ["6", "Moscow ", "Khabarovsk ", "8 ", '9 ',"TY_1206"], ["4", "Moscow ", "Khabarovsk ", "8 ", '9 ',"BB2689"],
                     ["6", "Moscow ", "Khabarovsk ", "8 ", '3 ',"BB689"]]



class XML:
 def __init__(self):
        self.data = [["1", "Moscow ", "Khabarovsk ", "8 ", '9 ',"CY-23"], ["2", "Moscow ", "Khabarovsk ", "8 ", '9 ',"CY-23"],
                     ["3", "Moscow ", "Khabarovsk ", "8 ", '9 ',"TY_106"], ["4", "Moscow ", "Khabarovsk ", "8 ", '9 ',"TY_1206"],
                     ["6", "Moscow ", "Khabarovsk ", "8 ", '9 ',"TY_1206"], ["4", "Moscow ", "Khabarovsk ", "8 ", '9 ',"BB2689"],
                     ["6", "Moscow ", "Khabarovsk ", "8 ", '3 ',"BB689"]]
        self.url="appct9.xml"
 def dsd(self):
     return self.data
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





import json
from collections import namedtuple
from json import JSONEncoder

class flights:
    def __init__(self, rollNumber, name, froms,where,landing,arrival):
        self.rollNumber, self.name, self.froms,self.where ,self.landing ,self.arrival= rollNumber, name, froms,where,landing,arrival


class StudentEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__

def customStudentDecoder(studentDict):
    return namedtuple('X', studentDict.keys())(*studentDict.values())

s1=[]
for i in data:
    print(i)
    a=flights(i[0], i[1], i[2], i[3],i[4],i[5])
    s1.append(a)



studentJson = json.dumps(s1, indent=4, cls=StudentEncoder)
print("Student JSON")
print(studentJson)

studObj = json.loads(studentJson, object_hook=customStudentDecoder)

for i in studObj:
    print(i[0],i[1],i[2],i[2],i[3],i[4],i[5])
