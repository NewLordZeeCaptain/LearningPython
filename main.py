documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
]
directories = {"1": ["2207 876234", "11-2", "5455 028765"], "2": ["10006"], "3": []}


def people():
    number = input("Введите номер документа: ")
    for document in documents:
        if number in document["number"]:
            print(document["name"])
            return
    print("Данного человека нет")


def search():
    number = input("Введите номер документа: ")
    for key, value in directories.items():
        if number in value:
            print(key)
            return

    print("Такого документа нет")


def add():
    number, type_of, name, place = (
        input("Укажите номер: "),
        input("Тип документа: "),
        input("Имя: "),
        input("Полку: "),
    )
    if place not in directories:
        print("Такой полки нет")
        return

    directories[place].append(number)
    documents.append({"type": type_of, "number": number, "name": name})


def document_list():
    pass


def main():
    while True:
        command = input()
        if command == "p":
            people()

        elif command == "s":
            search()

        elif command == "l":
            document_list()

        elif command == "a":
            add()

        elif command == "q":
            print("Goodbye")
            break


main()
