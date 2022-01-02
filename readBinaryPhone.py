import pickle

def main() :
    contacts = readContactFile()
    menuoption = 'D'
    while menuoption != 'Q' :
        if menuoption == 'D':
            display(contacts)
            void = input('press enter to show menu')
        elif menuoption == 'A':
            add(contacts)
        elif menuoption == 'R':
            remove(contacts)
        else:
            edit(contacts)
        print()
        menuoption = menu()
        
        
    writeContactFile(contacts)


def readContactFile() :
    infile = open(r'C:\Users\Dmitry\Downloads\phonebook.dat','rb')
    contents = {}
    contents = pickle.load(infile)
    infile.close()
    return contents

def writeContactFile(contacts) :
    outfile = open(r'C:\Users\Dmitry\Downloads\edited_phonebook.dat','wb')
    pickle.dump(contacts, outfile)
    outfile.close()

def menu() :
    print('Use A to add a contact')
    print('Use E to edit a file' + '\n' + 'Use R to remove a contact')
    print('Use D to display curent list' + '\n' + 'Use Q to quit')
    value = input('Please make a choice ')
    I = set('AERDQaerqd')
    while not value in I:
        print('Incorrect variable. Try again')
        value = input()
    print()
    return value.upper()


def add(contacts) :
    name = input('Please enter name: ')
    numail = input('Please enter number or email: ')
    contacts[name] = numail
    print('contant', name, 'was added')

def remove(contacts) :
    to_del = input('Which contact would you like to delete: ')
    try:
        del contacts[to_del]
    except KeyError:
        print('this is not valid contact')
        remove(contacts)
    print('contact', to_del, 'was deleted')
        

def edit(contacts) :
    display(contacts)
    to_edit = input('Which contact whould you like to edit? ')
    while to_edit not in contacts :
        to_edit = input('Enter existing name ')
    change = input('what is the correct number? ')
    contacts[to_edit] = change
    print('contact', to_edit, 'was edited')

def display(contacts) :
    for key in contacts:
        print(key + ":\t" + contacts[key])

main()