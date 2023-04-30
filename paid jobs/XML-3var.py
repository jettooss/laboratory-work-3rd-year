import xml.etree.ElementTree as ET
class Firm:
    def __init__(self):

        self.data = [["Nike", "1101", "clothes "],
                     ["Levis  ", "41414", "clothes "],
                     ["Xerox  ", "2457", "clothes "],
                     ["Chlo  ", "7575", "clothes "],
                     ["Cartier  ", "757527", "clothes "],
                     ["Bvlgari   ", "75757", "clothes "],
                     ["Disney  ", "75786", "movie "]]

    def serialize_to_xml(self):
        # создаем корневой элемент
        student = ET.Element('firms')
        for i in self.data:
            # создаем дочерние элементы

            appt = ET.Element("firm")
            first_name = ET.SubElement(appt, 'name_firm')
            first_name.text = i[0]
            last_name = ET.SubElement(appt, 'price')
            last_name.text = i[1]
            group = ET.SubElement(appt, 'product')
            group.text = i[2]
            student.append(appt)
            # создаем XML-документ
        xmlstr = ET.tostring(student, encoding="unicode")

        # сохраняем XML в файл
        with open("firms1.xml", "w") as f:
            f.write(xmlstr)
        return ET.tostring(student)

    def deserialize_from_xml(self, tree):
        root = tree.getroot()

        for elem in root:
            name_firm = elem.find('name_firm').text
            price = elem.find('price').text
            product = elem.find('product').text
            print(name_firm, price, product)


serialized= Firm().serialize_to_xml()
print(serialized)
tree = ET.parse("firms1.xml")
serialized = Firm().deserialize_from_xml(tree)
# import xml.etree.ElementTree as ET - это инструкция импорта модуля xml.etree.ElementTree.
#
# xml.etree.ElementTree - это стандартный модуль Python для работы с XML-документами. Каждый элемент XML-документа представлен в виде объекта класса Element, который может содержать другие элементы в качестве дочерних. Методы класса Element позволяют создавать, изменять и сохранять XML-документы.
#
# Чтобы сократить длинные имена модулей при использовании их в коде, мы можем использовать оператор as, который позволяет назначить альтернативное имя для модуля. В данном случае мы используем имя ET, чтобы обращаться к модулю xml.etree.ElementTree в нашем коде.
#
# Класс Firm имеет два метода: serialize_to_xml и deserialize_from_xml.
#
# Метод serialize_to_xml создает объект Element для корневого элемента firms и создает дочерние элементы firm для каждой записи в self.data. Для каждой записи создаются дочерние элементы name_firm, price и product. Метод serialize_to_xml сохраняет полученный XML-документ в файл firms1.xml и возвращает строку с XML-документом.
#
# Метод deserialize_from_xml использует метод ElementTree.parse для чтения XML-файла firms1.xml и получения корневого элемента firms. Затем он получает элементы firm, используя метод Element.findall, и для каждого элемента извлекает значения элементов name_firm, price и product.