
import os as oc
import xml.dom.minidom as minidom
import xml.etree.ElementTree as ET


class Computer:
    def __init__(self, ip, name, os):
        self.ip = ip
        self.name = name
        self.os = os

    def to_dict(self):
        return {"ip": self.ip, "name": self.name, "os": self.os}

    def from_dict(self, data):
        self.ip = data["ip"]
        self.name = data["name"]
        self.os = data["os"]


class Network_XML:
    def __init__(self):
        self.computers = []

    def add_computer(self, computer):
        self.computers.append(computer)

    def serialize_to_xml(self):
        network = ET.Element('network')
        for computer in self.computers:
            element = ET.Element('computer')
            ip = ET.SubElement(element, 'ip')
            ip.text = computer.ip
            name = ET.SubElement(element, 'name')
            name.text = computer.name
            os = ET.SubElement(element, 'os')
            os.text = computer.os
            network.append(element)
        xmlstr = minidom.parseString(ET.tostring(network)).toprettyxml()
        if not oc.path.isfile('network.xml'):
            with open('network.xml', 'x') as f:
                f.write(xmlstr)
            print("Файл создан:", oc.path.abspath('network.xml'))
        else:
            print("Файл уже существует, запись произведена не будет.")
        return xmlstr

    def deserialize_from_xml(self):
        tree = ET.parse('network.xml')
        root = tree.getroot()
        for element in root.findall('computer'):
            ip = element.find('ip').text
            name = element.find('name').text
            os = element.find('os').text
            computer = Computer(ip, name, os)
            self.computers.append(computer)
        return self.computers

    def add_computer_to_xml(self, computer):
        # Добавляем новый компьютер в файл network.xml
        tree = ET.parse('network.xml')
        root = tree.getroot()
        computer_elem = ET.SubElement(root, 'computer')
        ET.SubElement(computer_elem, 'name').text = computer.name
        ET.SubElement(computer_elem, 'ip').text = computer.ip
        ET.SubElement(computer_elem, 'os').text = computer.os
        tree.write('network.xml', encoding='utf-8', xml_declaration=True)


def add_computer(self, computer):
    self.computers.append(computer)
    self.add_computer_to_xml(computer)


def main():
    net = Network_XML()

    while True:
        command = input(
            "Введите команду 1 - добавить компьютер, 2 - сериализовать данные в XML, 3 - десериализовать данные из XML, 4 - выход,5 добавить данные в XML-файл): ")

        if command == '1':
            # Получаем данные для нового компьютера
            ip = input("Введите IP-адрес нового компьютера: ")
            name = input("Введите имя нового компьютера: ")
            os = input("Введите ОС нового компьютера: ")

            # Создаем объект компьютера и добавляем его в сеть
            computer = Computer(ip, name, os)
            net.add_computer(computer)

        elif command == '2':
            # Сохраняем изменения в файл network.xml
            net.serialize_to_xml()

        elif command == '3':
            # Десериализуем данные из файла network.xml
            net.computers = net.deserialize_from_xml()
            # Выводим список компьютеров
            for computer in net.computers:
                print(computer.name, computer.ip, computer.os)

        elif command == '4':
            print("Выход из программы.")
            break
        elif command == '5':  # Получаем данные для нового компьютера и добавляем его в сеть и XML-файл
            ip = input("Введите IP-адрес нового компьютера: ")
            name = input("Введите имя нового компьютера: ")
            os = input("Введите ОС нового компьютера: ")
            computer = Computer(ip, name, os)
            net.add_computer(computer)
            net.add_computer_to_xml(computer)
        else:
            print("Неверная команда.")


if __name__ == '__main__':
    main()
