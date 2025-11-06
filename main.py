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
    print(Fore.LIGHTGREEN_EX + 'Type /create to create a new hacking tool' + Style.RESET_ALL)
    if input(Fore.LIGHTWHITE_EX + 'Type here: ' + Style.RESET_ALL) == '/create':
        print_create()

PRANK_TEXT = """
'll have you know I graduated top of my class in the Navy Seals, and I've been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. \n
I am trained in gorilla warfare and I'm the top sniper in the entire US armed forces. \n
You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. \n
You think you can get away with saying that shit to me over the Internet? Think again, fucker. \n
As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. \n
The storm that wipes out the pathetic little thing you call your life. You're fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that's just with my bare hands. \n
Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. \n
If only you could have known what unholy retribution your little "clever" comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn't, you didn't, and now you're paying the price, you goddamn idiot. \n
I will shit fury all over you and you will drown in it. You're fucking dead, kiddo. \n
"""


def print_create():
    clear_screen()
    name = input(Fore.LIGHTWHITE_EX + 'Filename (no path, e.g. funny.txt): ' + Style.RESET_ALL).strip()
    if not name:
        print(Fore.LIGHTRED_EX + 'Name required' + Style.RESET_ALL); return
    if not os.path.splitext(name)[1]:
        name += '.txt'

    desktop = os.path.expanduser('~/Desktop')
    folder = os.path.join(desktop, 'Don\'t open this file')

    os.makedirs(folder, exist_ok=True)
    out = os.path.join(folder, name)
    with open(out, 'w', encoding='utf-8') as f:
        f.write(PRANK_TEXT)
    
    hacked = Figlet(font='standard').renderText('Congrats you have been hacked')
    for line in hacked.split('\n'):
        print(Fore.LIGHTGREEN_EX + line + Style.RESET_ALL)
        time.sleep(0.05)
        
def main():
    print_intro()
main()