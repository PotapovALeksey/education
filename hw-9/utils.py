import commands
from db import DATABASE
from functools import reduce

def help(*_):
    documentation = f'''
        Read the instructions
    
        "{commands.HELLO}" - Greeting"
        "{commands.HELP}" - Watch the documentation"
        "{commands.ADD} [name] [phone]" - Create a new contact
        "{commands.CHANGE} [name] [phone]" - Update an existing contact by the name 
        "{commands.PHONE} [name]" - Watch a phone by a name
        "{commands.SHOW_ALL}" - Watch all existing contacts
        "{commands.GOOD_BYE}", "{commands.CLOSE}", "{commands.EXIT}" - Leave the program with saying "Good buy"
        "{commands.SILENT_EXIT}" - Leave the program
        
        !!!Pay attention - spaces are required between each word!!!
    '''

    return documentation


def input_error(func):
    def inner(*args):
        try:
            return func(*args)

        except (ValueError, AttributeError):
            return f'Something went wrong. Please read documentation and try again \n {help()}'

    return inner


def hello(*_):
    return "How can I help you?"


@input_error
def add(*args):
    name, phone = args

    DATABASE[name] = phone

    return 'User has been added'


@input_error
def change(*args):
    name, phone = args

    if name in DATABASE:
        DATABASE[name] = phone
        return 'The phone has been changed'
    else:
        return f'There is no user - {name}'

@input_error
def phone(*args):
    name = args

    if name in DATABASE:
        return f'{name.title()}: {DATABASE[name]}'
    else:
        return f'There is no user - {name}'


@input_error
def show_all(*_):
    return reduce(lambda acc, user: acc + f'{user[0].title()}: {user[1]} \n', DATABASE.items(), '')

def close(has_goodbuy=True):
    return lambda *_: 'Good buy' if has_goodbuy else ''

