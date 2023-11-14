import re
from utils import add, change, phone, show_all, close, hello, help
import commands

hendlers = {
    commands.HELLO: hello,
    commands.ADD: add,
    commands.CHANGE: change,
    commands.PHONE: phone,
    commands.SHOW_ALL: show_all,
    commands.CLOSE: close(),
    commands.GOOD_BYE: close(),
    commands.EXIT: close(),
    commands.SILENT_EXIT:  close(False),
    commands.HELP: help,
}

def get_command(user_input):

    for command in hendlers.keys():

        if user_input.startswith(command):
            args = user_input.replace(command, '').strip().split(' ')

            return command, args


    return commands.HELP, ()

EXIT_COMMANDS = (commands.EXIT, commands.CLOSE, commands.GOOD_BYE, commands.SILENT_EXIT)

def main():
    user_input = input('').casefold()

    while True:
        command, args = get_command(user_input)
        handler = hendlers.get(command, None)

        result = handler(*args)

        if result != None:
            print(result)

        if command in EXIT_COMMANDS:
            break

        user_input = input().casefold()


if __name__ == '__main__':
    main()