import shutil

user = "a"

while user != "Stop":
    print("команды: ")
    print("1.Запись файла по новому")
    print("2.Добавить Запись к файлу")
    print("3.Чтение файла")
    print("4.Копирование определенной строки файла в ваш файл")
    print("5.Копирование всего файла в ваш файл")

    def write():
        with open("справочник.txt", "w") as data:
            data.write(input("Введите номера телефонов и фамилию через пробел: "))
        return data

    def append():
        with open("справочник.txt", "a") as data:
            data.write(input("Введите номер телефона и фамилию через пробел: \n"))
        return data

    def read():
        with open("справочник.txt", "r") as data:
            for line in data:
                print(line)
        return line

    def copyfileline():
        source_file = "справочник.txt"
        destination_file = input("Введите название вашего файла: ")

        line_number = int(input("Введите номер строки для копирования: "))
        with open(source_file, "r") as source:
            lines = source.readlines()
            if 0 < line_number <= len(lines):
                with open(destination_file, "a") as dest:
                    dest.write(lines[line_number - 1])
                print(f"Строка {line_number} скопирована в файл {destination_file}")
            else:
                print("Такой строки нет")
    
    def copyfile():
        return shutil.copy("справочник.txt",input("Введите название вашего файла: "))

    user_f = int(input("Выберите номер команды: "))
    if user_f == 1:
        write()
    elif user_f == 2:
        append()
    elif user_f == 3:
        read()
    elif user_f == 4:
        copyfileline()
    elif user_f == 5:
        copyfile()
    else:
        print("такой операции нет")
    user = input("введите Stop чтобы остановить программу: ")