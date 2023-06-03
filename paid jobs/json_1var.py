import json

class Book:
    def __init__(self):
        # Инициализация списка данных о книгах
        self.data = [
            ["The Master and Margarita", "Mikhail Bulgakov ", "Soviet Writer"],
            ["Fahrenheit 451", "Ray Bradbury", "AST"],
            ["Crime and Punishment", "Fyodor Dostoevsky", "Eksmo"],
            ["Pride and Prejudice", "Jane Austen", "Azbooka-Atticus"],
            ["War and Peace", "Leo Tolstoy", "AST"],
            ["1984", "George Orwell", "Eksmo"],
            ["Shantaram", "Gregory David Roberts", "AST"]
        ]

    def serialize_to_json(self):
        # Создаем словарь с данными о книгах
        books_dict = {"book_catalog": []}
        for i in self.data:
            book_dict = {
                "name_book": i[0],
                "author": i[1],
                "publisher": i[2]
            }
            # Добавляем книгу в список книг
            books_dict["book_catalog"].append(book_dict)
        # Сериализуем данные в формате JSON
        serialized_data = json.dumps(books_dict, indent=4)
        # Записываем данные в файл
        with open("books.json", "w") as f:
            f.write(serialized_data)
        return serialized_data

    def deserialize_from_json(self):
        # Читаем данные из файла
        with open("books.json", "r") as f:
            data = json.load(f)
        # Выводим информацию о каждой книге из данных
        for book in data["book_catalog"]:
            print(book["name_book"], book["author"], book["publisher"])

if __name__ == "__main__":
    # Создаем экземпляр класса и сериализуем данные о книгах в файл
    serialized_book = Book().serialize_to_json()
    # Выводим созданный JSON-документ на экран
    print(serialized_book)
    # Считываем данные из файла и десериализуем их
    deserialized_book = Book().deserialize_from_json()