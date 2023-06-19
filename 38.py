def print_menu():
    print("""
    -------------------------------
    1 - вывести все контакты  
    2 - поиск контакта
    3 - добавить контакт 
    4 - изменить данные контакта 
    5 - удалить контакт 
    6 - выход  
    ------------------------------- 
    """)
print_menu()
def addition():
    with open(file, 'a', encoding='utf8') as open_book:
        add_surname = (input('Введите фамилию: ' ).title())
        add_name = (input('Введите имя: ' ).title())
        add_phone = (input('Введите телефон: ' ).title())
        add_note = (input('Введите заметку: ' ).title())
        new_line = add_surname +' '+add_name +' '+ add_phone +' '+ add_note 
        open_book.writelines(f'\n{new_line}')
        print(new_line)

def search():
    with open(file, 'r', encoding='utf8') as open_book:
        seach_param = (input('Введите параметр для поиска: ' ).title())
        for line in open_book:
            if seach_param in line:
                print(line)

def remove_contact():
    with open(file, 'r', encoding="utf-8") as open_book:
        X = input('Введите Имя или Фамилию для удаления: ')
        lines = open_book.readlines()
        with open(file, 'w', encoding="utf-8") as open_book:
            for line in lines:
                if X in line:
                    print("Строка удалена")
                else:
                    print(line)    
                    open_book.write(line)


def edit():
    with open(file, 'r', encoding="utf-8") as open_book:
        seach_param = (input('Введите параметр для поиска: ' ).title())
        for line in open_book:
            if seach_param in line:
                with open (file, 'w', encoding='utf8') as open_book:
                    print(line)
                    add_surname = (input('Введите фамилию: ' ).title())
                    add_name = (input('Введите Имя: ' ).title())
                    add_phone = (input('Введите телефон: ' ).title())
                    add_note = (input('Введите заметку: ' ).title())
                    new_line = add_surname +' '+add_name +' '+ add_phone + ' '+ add_note + '\n'
                    line = line.replace(line, new_line)
                    open_book.writelines(line)

def read_all():
    with open(file, 'r', encoding='utf8') as open_book:
        print()
        for line in open_book:
            print(line)  



def tasks(choice):
        if choice == 1:
            read_all()
            print_menu()
            tasks(int(input('Выберите пункт меню: ')))   
        elif choice == 2: 
            search()
            print_menu()
            tasks(int(input('Выберите пункт меню: ')))
        elif choice == 3:
            addition()
            print_menu()
            tasks(int(input('Выберите пункт меню: ')))
        elif choice == 4:
            edit()
            print_menu()
            tasks(int(input('Выберите пункт меню: ')))
        elif choice == 5:
            remove_contact()
            print_menu()
            tasks(int(input('Выберите пункт меню: ')))
        elif choice == 6:
            exit            
            
file = 'phonebook.txt'
tasks(int(input('Выберите пункт меню: ')))