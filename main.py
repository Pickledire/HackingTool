import os
from pyfiglet import Figlet
from colorama import Fore, Style
import time


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_intro():
    clear_screen()
    intro_time = 0.05
    clear_time = 3
    banner = Figlet(font='standard', width = 100, justify='center')
    for line in banner.renderText('System\nHacker\nTool').split('\n'):
        print(Fore.GREEN + line + Style.RESET_ALL)
        time.sleep(intro_time)
    time.sleep(clear_time)
    clear_screen()


    for line in 'Welcome to the Hacker Tool'.split('\n'):
        print(Fore.LIGHTGREEN_EX + line + Style.RESET_ALL)
        time.sleep(intro_time)
        print('\n')
        print(Fore.LIGHTGREEN_EX + 'This tool is designed to help you hack into systems' + Style.RESET_ALL)
        time.sleep(intro_time)
        print('\n')
        print(Fore.LIGHTGREEN_EX + 'Type /help to see the list of commands' + Style.RESET_ALL)
        time.sleep(intro_time)
        if input(Fore.LIGHTWHITE_EX + 'Type here: ' + Style.RESET_ALL) == '/help':
            print_help()

def print_help():
    clear_screen()
    print(Fore.LIGHTGREEN_EX + 'Help' + Style.RESET_ALL)
    print(Fore.LIGHTGREEN_EX + 'Type /help to see the list of commands' + Style.RESET_ALL)
    print(Fore.LIGHTGREEN_EX + 'Type /quit to exit the tool' + Style.RESET_ALL)
    print(Fore.LIGHTGREEN_EX + 'Type /create to create a new hacking tool' + Style.RESET_ALL)
    print(Fore.LIGHTGREEN_EX + 'Type /list to list all the hacking tools' + Style.RESET_ALL)
    if input(Fore.LIGHTWHITE_EX + 'Type here: ' + Style.RESET_ALL) == '/create':
        print_create()

def print_create():
    clear_screen()
    print(Fore.LIGHTGREEN_EX + 'Create' + Style.RESET_ALL)
    print(Fore.LIGHTGREEN_EX + '\n' + 'Enter the name of the hacking tool' + Style.RESET_ALL)
    name = input(Fore.LIGHTWHITE_EX + 'Type here: ' + Style.RESET_ALL)
    if input == True:
        with open('hacking_tools.txt', 'w') as file:
            file.write(name)
        print(Fore.LIGHTGREEN_EX + 'Hacking tool created successfully' + Style.RESET_ALL)
    else:
        

def main():
    print_intro()
main()