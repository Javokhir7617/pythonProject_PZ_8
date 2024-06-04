def input_name():
    return input('Введите имя: ')


def input_surname():
    return input('Введите фамилию: ')


def input_patronymic():
    return input('Введите отчество: ')


def input_phone():
    return input('Введите номер телефона: ')


def input_address():
    return input('Введите адрес: ')


def create_contact():
    surname = input_surname()
    name = input_name()
    patronymic = input_patronymic()
    phone = input_phone()
    address = input_address()
    return f'{surname} {name} {patronymic} {phone}\n{address}\n\n'


def add_contact():
    contact = create_contact()
    with open('phonebook.txt', 'a', encoding='utf-8') as file_a:
        file_a.write(contact)


def print_contacts():
    try:
        with open('phonebook.txt', 'r', encoding='utf-8') as file_r:
            print(file_r.read())
            print()
            print('-' * 50)
            print('Вывод контактов завершен!')
    except FileNotFoundError:
        print('Телефонная книга пуста или файл не найден!')


def search_contacts():
    print('Варианты поиска: \n'
          '1 - По фамилии\n'
          '2 - По имени\n'
          '3 - По отчеству\n'
          '4 - По телефону\n'
          '5 - По адресу\n')
    var = input('Введите вариант поиска: ')
    while var not in ('1', '2', '3', '4', '5'):
        print('Неверный вариант, попробуйте снова.')
        var = input('Введите вариант поиска: ')

    search = input('Введите данные для поиска: ')
    try:
        with open('phonebook.txt', 'r', encoding='utf-8') as file_r:
            contacts_lst = file_r.read().split('\n\n')
        found_contacts = [contact for contact in contacts_lst if search in contact]
        if found_contacts:
            for contact in found_contacts:
                print(contact)
        else:
            print('Контакты не найдены.')
    except FileNotFoundError:
        print('Телефонная книга пуста или файл не найден!')


def copy_contact():
    try:
        with open('phonebook.txt', 'r', encoding='utf-8') as file_r:
            contacts_lst = file_r.read().split('\n\n')
        print("Контакты в исходном файле:")
        for idx, contact in enumerate(contacts_lst, start=1):
            print(f"{idx}. {contact}")

        contact_number = int(input("Введите номер строки для копирования: "))
        while contact_number < 1 or contact_number > len(contacts_lst):
            print("Неверный номер строки, попробуйте снова.")
            contact_number = int(input("Введите номер строки для копирования: "))

        contact_to_copy = contacts_lst[contact_number - 1]

        with open('phonebook_copy.txt', 'a', encoding='utf-8') as file_w:
            file_w.write(contact_to_copy + '\n\n')
        print("Контакт успешно скопирован!")
    except FileNotFoundError:
        print('Телефонная книга пуста или файл не найден!')


def interface():
    with open('phonebook.txt', 'a', encoding='utf-8'):
        pass
    command = ''
    while command != '5':
        print('Варианты действий: \n'
              '1 - Ввод контакта\n'
              '2 - Вывод контактов\n'
              '3 - Поиск контакта\n'
              '4 - Копирование контакта\n'
              '5 - Выход\n')
        command = input('Введите вариант действий: ')
        while command not in ('1', '2', '3', '4', '5'):
            print('Неверный вариант, попробуйте снова.')
            command = input('Введите вариант действий: ')
        match command:
            case '1':
                add_contact()
            case '2':
                print_contacts()
            case '3':
                search_contacts()
            case '4':
                copy_contact()
            case '5':
                print('Всего доброго!')


interface()
