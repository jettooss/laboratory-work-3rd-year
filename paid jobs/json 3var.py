import json

class Firm:
    def __init__(self, firm, price, product):
        self.firm = firm
        self.price = price
        self.product = product

    def to_dict(self):
        return {
            'firm': self.firm,
            'price': self.price,
            'product': self.product,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            firm=data['firm'],
            price=data['price'],
            product=data['product']
        )

Price_list = [

    Firm("Nike", 1101, "clothes "),
    Firm("Levis  ", 41414, "clothes "),
    Firm("Xerox  ", 2457, "clothes "),
    Firm("Chlo  ", 7575, "clothes "),
    Firm("Cartier  ", 757527, "clothes "),
    Firm("Bvlgari   ", 75757, "clothes "),
    Firm("Disney  ", 75786, "movie "),
]


serialized_firm = json.dumps([s.to_dict() for s in Price_list])
with open('firm.json', 'w') as f:
 f.write(serialized_firm)


with open('firm.json', 'r') as f:
 deserialized_firm = [Firm.from_dict(s) for s in json.loads(f.read())]
# Print list of students
for firm in deserialized_firm:
    print("{}, {}, {}".format(firm.firm, firm.price, firm.product))


# В данном примере определен класс Firm, имеющий атрибуты firm, price и product. Есть методы to_dict() и from_dict(), которые преобразуют объект класса в словарь и наоборот соответственно.
#
# Далее создается список объектов класса Firm, который называется Price_list.
#
# Затем объекты из Price_list сериализуются в JSON формат и записываются в файл firm.json.
#
# Далее эти данные считываются из файла firm.json и десериализуются обратно в список объектов класса Student, который называется deserialized_firm.
#
# В конце происходит итерация по объектам класса Student, считанным из файла firm.json, выводится на экран в форматированном виде информация о каждом объекте.
#
# В последней строке кода, однако, отсутствуют кавычки, закрывающие строку. Необходимо заменить print("{}, {}, {}".format(firm.firm, firm.price, fir, на print("{}, {}, {}".format(firm.firm, firm.price, firm.product)).
#
#
#
