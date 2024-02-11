# Решил выполнить задание с помощью классов
# Реализация справочника с помощью паттерна Builder
class Phonebook:
    def __init__(self, contacts):
        self.contacts = contacts

    # 1.Просмотр контактов в справочнике
    def get_contacts(self):
        with open(self.contacts, 'r', encoding='utf-8') as f:
            file = f.read()
        return file

    # 2.Добавить контакт в справочник
    def add_contact(self, contact: str):
        #Открыть файл и записать в него информацию
        with open(self.contacts, 'a', encoding="utf-8") as f:
            f.writelines(str(contact))

    # 3.Редактирование записи в справочнике
    def refactor_contact(self):
        with open(self.contacts, 'r', encoding='utf-8') as f:
            filedata = f.read()
        filedata = filedata.replace(input('Какой параметр вы хотите изменить: '), input('Введите новые данные: '), 1)
        with open(self.contacts, 'w', encoding='utf-8') as f:
            f.write(filedata)

    # 4.Поиск контакта
    def search_contact(self, first_name: str, last_name: str) -> bool | str:
        with open(self.contacts, 'r', encoding='utf-8') as f:
            file = f.readlines()
        for i in file:
            if (first_name in i) and (last_name in i):
                return i
        return False


# Создаем класс контакт
class Contact:
    def __init__(self, last_name: str, first_name: str, patronymic: str,
                 name_organization: str, work_phone: str, personal_phone: str):
        self.last_name = last_name
        self.first_name = first_name
        self.patronymic = patronymic
        self.name_organization = name_organization
        self.work_phone = work_phone
        self.personal_phone = personal_phone

    def __str__(self):
        return f'Last name: {self.last_name} ; ' \
               f'First name: {self.first_name} ; ' \
               f'Patronymic: {self.patronymic} ; ' \
               f'Name organization: {self.name_organization} ; ' \
               f'Work phone: {self.work_phone} ; ' \
               f'Personal phone: {self.personal_phone} .\n'


def input_data(txt: str) -> str:
    x = input(txt)
    return x

def main_input() -> str:
    return input('Телефонный справочник: \n'
                 'Нажмите 1 если хотите просмотреть все контакты;\n'
                 'Нажмите 2 если хотите добавить контакт\n'
                 'Нажмите 3 если хотите изменить контакт\n'
                 'Нажмите 4 если хотите найти контакт\n'
                 'Нажмите 0 если хотите выйти. \n')


def main():
    inp = main_input()
    phonebook = Phonebook('test_file.txt')
    while inp != '0':
        if inp == '0':
            break
        elif inp == '1':
            print(phonebook.get_contacts())
            print()
        elif inp == '2':
            contact = Contact(input_data('Введите фамилию: '), input_data('Введите имя: '), input_data('Введите отчество: '),
                              input_data('Введите название компании: '), input_data('Введите рабочий телефон: '),
                              input_data('Введите сотовый телефон: '))
            phonebook.add_contact(contact)
            print(phonebook.get_contacts())
        elif inp == '3':
            phonebook.refactor_contact()
            print(phonebook.get_contacts())
        elif inp == '4':
            print('Чтобы найти человека впишите имя и фамилию.')
            print(phonebook.get_contacts())
            print(phonebook.search_contact(input_data('Имя: '), input_data('Фамилия: ')))
        else:
            print('Введите толькл цифры указанные в меню')
        inp = main_input()
main()
