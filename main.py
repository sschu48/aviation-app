# Aviation App
# Created by Sean Schumacher
# 2021

user = 'sean'       # Temporary username
password = '1234'   # Temporary password

# Login Page
def Login():
    print('Welcome to the Aviation App')
    print('Enter usename and password below:')
    user_input = input('Username: ')
    pass_input = input('Password: ')

    if user_input == user and pass_input == password:
        Dashboard()
    else:
        print('Unkown, Try Again:')
        Login()

# Dashboard View
def Dashboard():
    print('What would you like to do today?')
    print('- weather')
    print('- logbook')
    print('- exit')
    user_input = input('Enter Here: ')

    if user_input == 'weather':
        print('weather')
        Weather()
    elif user_input == 'logbook':
        print('logbook')
        Logbook()
    elif user_input == 'exit':
        Login()
    else:
        user_input = input('Unkown, Try Again: ')

# Weather View
def Weather():
    print('What weather do you want to see?')
    print('- METARs (METAR)')
    print('- TAFs (TAF)')
    user_input = input('Enter Here: ')

    if user_input == 'METAR' or user_input == 'METARs':
        print('METAR')
    elif user_input == 'TAF' or user_input == 'TAFs':
        print('TAF')
    else:
        user_input = input('Unkown, Try Again: ')

# Logbook View
def Logbook():
    print('What do you want to do?')
    print('- Add Entry (add)')
    print('- Remove Entry (remove)')
    print('- View Entries (view)')
    print('- Exit (exit)')
    user_input = input('Enter here: ')

    def addEntry(name):
        print(name)

    def removeEntry(name):
        print('removed' + name)

    def viewEntry():
        print('list')

    if user_input == 'add':
        entry_name = input('Add Entry Name: ')
        addEntry(entry_name)
    elif user_input == 'remove':
        entry_name = input('Remove Entry Name: ')
        removeEntry(entry_name)
    elif user_input == 'view':
        entry_name = input('Viewing List')
        viewEntry()


    

Login()