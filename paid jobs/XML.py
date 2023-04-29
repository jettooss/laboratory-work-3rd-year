import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

class Student:
    def __init__(self):

        self.data = [["Frank", "Nelson ", "PMI " ],
                     [ "Gary  ", "Morris ", "PMI "],
                     [ "Ernest  ", "Stanley ", "PMI " ],
                     [ "Sergio  ", "Banks ", "PMI "],
                     [ "Alvin  ", "Daniels ", "PMI "],
                     ["Steven  ", "Ramsey ", "PMI "],
                     ["Mitchell  ", "Jackson ", "PMI "]]
    def serialize_to_xml(self):
        # создаем корневой элемент
     student = ET.Element('students')
     for i in self.data:

        # создаем дочерние элементы

        appt = ET.Element("student")
        first_name = ET.SubElement(appt, 'first_name')
        first_name.text = i[0]
        last_name = ET.SubElement(appt, 'last_name')
        last_name.text =i[1]
        group = ET.SubElement(appt, 'group')
        group.text = i[2]
        student.append(appt)
        # создаем XML-документ
     xmlstr = ET.tostring(student, encoding="unicode")

        # сохраняем XML в файл
     with open("person3.xml", "w") as f:
            f.write(xmlstr)
     return ET.tostring(student)
    def deserialize_from_xml(self,tree):
        root = tree.getroot()
        dom = minidom.parse("person3.xml")
        elements = dom.getElementsByTagName('student')

        for i in range(0, len(elements)):
            print(root[i][0].text, root[i][1].text, root[i][2].text)

# Это функция, которая принимает объект "tree" в формате XML и десериализует его содержимое в объект класса.
# Сначала она получает корневой элемент XML дерева с помощью метода "getroot()" объекта "tree". Затем она находит с
# писок всех элементов "student" в XML файле "person3.xml" с помощью метода "getElementsByTagName()" объекта "dom".
# Затем происходит итерация по этому списку, и для каждого элемента выводятся его три дочерних элемента "text" по индексу с помощью метода "print".
# Объект minidom используется для разбора (парсинга) XML-файла.

            
if __name__ == "__main__":
    serialized_student = Student().serialize_to_xml()
    print(serialized_student)
    tree = ET.parse("person3.xml")
    serialized_student = Student().deserialize_from_xml(tree)

