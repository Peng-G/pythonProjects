"""This is a simple database built with shelve."""

import shelve


def store_person(data_base):
    'input data and store to a shelf object'

    pid = input('Enter unique ID number: ')
    person = {'name': input('Enter name: '), 'age': input('Enter age: '), 'phone': input('Enter phone number: ')}
    data_base[pid] = person


def lookup_person(data_base):
    'lookup an object with id or other information'

    pid = input('Enter ID number: ')
    field = input('What would you like to know? (name, age, phone) ')
    field = field.strip().lower()
    print(field.capitalize() + ':', data_base[pid][field])


def print_help():
    'show help information'
    print('The available commands are:')
    print('store : Stores information about a person')
    print('lookup : Looks up a person from ID number')
    print('quit : Save changes and exit')
    print('? : Prints this message')


def enter_command():
    'show basic input instructions to user'
    cmd = input('Enter command (? for help): ')
    cmd = cmd.strip().lower()
    return cmd


def main():
    """basic workflow"""
    database = shelve.open('D:\\database.dat')  # filepath could be modified.
    try:
        while True:
            cmd = enter_command()
            if cmd == 'store':
                store_person(database)
            elif cmd == 'lookup':
                lookup_person(database)
            elif cmd == '?':
                print_help()
            elif cmd == 'quit':
                return
    finally:
        database.close()


if __name__ == '__main__':
    main()
