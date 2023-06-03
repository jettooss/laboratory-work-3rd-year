class Van:
    def __init__(self, weight, id):
        self.weight = weight
        self.id = id


class PassengerVan(Van):
    def __init__(self, weight, id, capacity, num_passengers, avg_bag_weight):
        super().__init__(weight, id)
        self.capacity = capacity
        self.num_passengers = num_passengers
        self.avg_bag_weight = avg_bag_weight

    def get_total_weight(self):
        return self.weight + self.num_passengers * self.avg_bag_weight


class CargoVan(Van):
    def __init__(self, weight, id):
        super().__init__(weight, id)


class Locomotive():
    def __init__(self, max_weight, id):
        self.max_weight = max_weight
        self.id = id


class Train:
    def __init__(self):
        self.vans = []
        self.vansLocomotive = []
        self.total_weight_luggage = 0
        self.van_id = 0

    def find_luggage(self, num_passengers, avg_bag_weight):
        self.total_weight_luggage += num_passengers * avg_bag_weight

    def add_passenger_van(self, capacity, num_passengers, avg_bag_weight):
        total_weight = num_passengers * avg_bag_weight
        if total_weight <= self.max_weight():
            self.van_id += 1
            self.vans.append(PassengerVan(total_weight, self.van_id, capacity, num_passengers, avg_bag_weight, ))
        else:
            print("Общий вес пассажиров и их багажа превышает грузоподъемность поезда")

    def add_cargo_van(self, weight):
        if weight + sum([van.weight for van in self.vans if isinstance(van, CargoVan)]) <= self.max_weight():
            self.van_id += 1
            self.vans.append(CargoVan(weight, self.van_id))
        else:
            print("Вагон не может быть добавлен, так как его вес превышает грузоподъемность поезда.")

    def add_locomotive(self, max_weight):
        self.van_id += 1
        self.vansLocomotive.extend([Locomotive(max_weight, self.van_id)])

    def max_weight(self):
        weight_sum = 0
        for van in self.vansLocomotive:
            if isinstance(van, Locomotive):
                weight_sum += van.max_weight
            elif isinstance(van, CargoVan):
                pass
            else:
                weight_sum += van.weight
        return weight_sum

    def total_passengers(self):
        total = 0

        for van in self.vans:
            if isinstance(van, PassengerVan):
                total += van.num_passengers

        return total

    def find_vans_by_weight(self, weight_min, weight_max):
        result = []

        # Перебираем все вагоны в поезде
        for van in self.vans:
            # Проверяем вес вагона
            if isinstance(van,
                          Van) and weight_min is not None and weight_max is not None and weight_min <= van.weight <= weight_max:
                result.append(van)

        return result

    def sort_vans(self, attr_name):
        # Создаем временный экземпляр класса Van с минимальным весом
        temp_van = Van(weight=0, id=0)

        # Проверяем, существует ли атрибут в классе Van
        if not hasattr(temp_van, attr_name):
            raise ValueError(f"Атрибут {attr_name} не существует в классе Van")

        self.vans.sort(key=lambda x: getattr(x, attr_name) if hasattr(x, attr_name) else float('inf'))

    def print_vans(self):
        for van in self.vans:
            if isinstance(van, PassengerVan):
                print(
                    f"Пассажирский вагон (id: {van.id}), вместимостью {van.capacity} пассажиров и их багажа {van.avg_bag_weight}, вес {van.get_total_weight()}")
            elif isinstance(van, CargoVan):
                print(f"Грузовой вагон (id: {van.id}), вес {van.weight} ")
            # elif isinstance(van, Locomotive):
            #     print(f"Локомотив (id: {van.id}), грузоподъемность {van.max_weight}")
            else:
                print("Неизвестный тип вагона")

        print("____________________________________Локомотивы________________________________")
        for van in self.vansLocomotive:
            if isinstance(van, Locomotive):
                print(f"Локомотив (id: {van.id}), грузоподъемность {van.max_weight}")


def main():
    train = Train()
    while True:
        print("Введите номер действия:\n"
              "1. Вывести состав поезда\n"
              "2. Отсортировать вагоны по грузоподъемности и вывести\n"
              "3. Добавить пассажирский вагон\n"
              "4. Добавить грузовой вагон\n"
              "5. Добавить локомотив\n"
              "6. Общая численность пассажиров и багажа\n"
              "7. Найти вагоны по весу\n"
              " 8. Выход\n"
              )
        choice = input("Введите номер: ")
        if choice == "1":

            train.print_vans()

        elif choice == "2":
            train.sort_vans("weight")
            train.print_vans()
        elif choice == "3":
            capacity = int(input("Введите вместимость вагона: "))
            num_passengers = int(input("Введите количество пассажиров: "))
            avg_bag_weight = int(input("Введите средний вес багажа на пассажира: "))
            train.add_passenger_van(capacity, num_passengers, avg_bag_weight)
            train.find_luggage(num_passengers, avg_bag_weight)

        elif choice == "4":
            weight = int(input("Введите  вес груза: "))
            train.add_cargo_van(weight)
        elif choice == "5":
            max_weight = int(input("Введите грузоподъемность  локомотива: "))
            train.add_locomotive(max_weight)
        elif choice == "6":
            total_passengers = train.total_passengers()
            print(f"Общая численность пассажиров: {total_passengers}")

            print(f"Общая численность багажа: {train.total_weight_luggage}")
        elif choice == "7":
            weight_min = input("Введите минимальный вес вагона или нажмите ENTER: ")
            weight_max = input("Введите максимальный вес вагона или нажмите ENTER: ")
            vans = train.find_vans_by_weight(int(weight_min), int(weight_max))
            if vans:
                print(f"Найдено вагонов: {len(vans)}")
                for van in vans:
                    if isinstance(van, PassengerVan):
                        print(
                            f"Пассажирский вагон (id: {van.id}), вместимостью {van.capacity} пассажиров и их багажа {van.avg_bag_weight}, вес {van.get_total_weight()}")
                    elif isinstance(van, CargoVan):
                        print(f"Грузовой вагон (id: {van.id}), вес {van.weight} ")
                    elif isinstance(van, Locomotive):
                        print(f"Локомотив (id: {van.id}), грузоподъемность {van.max_weight}")
                    else:
                        print("Неизвестный тип вагона")
            else:
                print("Вагонов не найдено")
        elif choice == "8":
            print("Завершение работы")
            break
        else:
            print("Неверный номер, попробуйте еще раз")


if __name__ == '__main__':
    main()
# Данный код описывает классы и методы для создания поездов. Классы "Van", "PassengerVan", "CargoVan" и
# "Locomotive" описывают вагоны разных типов (грузовые, пассажирские, локомотивы).
# Класс "Train" описывает методы, позволяющие добавить вагон разного типа (грузовой, пассажирский),
# а также оценить грузоподъемность поезда, посчитать количество пассажиров,
# найти вагоны по весу и отсортировать вагоны по разным параметрам (например, весу).
# Данные методы могут быть использованы для создания и управления поездом.
