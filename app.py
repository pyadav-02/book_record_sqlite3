from utils import database

MAIN_MENU = """
press 'a' to add book
press 'd' to delete book
press 'l' to list all books
press 'r' to mark a book as read
press 'q' to quit"""


def menu():
    print(MAIN_MENU)

    choice_list = ['a', 'd', 'l', 'r', 'q']
    while True:
        print('='*20)
        choice = input('Enter input: ')
        while choice not in choice_list:
            print('invalid input is given')
            choice = input('Enter input: ')

        if choice == 'l':
            database.list_book()
            continue
        elif choice == 'q':
            break

        name = input('Enter book name: ')
        author = input("Enter author's name: ")
        if choice == 'a':
            database.add_book(name, author)
        elif choice == 'd':
            database.delete_book(name, author)
        else:
            database.read_book(name, author)

    print('='*20)
    print('program ended')

database.create_table()
menu()
