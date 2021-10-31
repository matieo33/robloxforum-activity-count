from bs4 import BeautifulSoup
import requests, time, re, keyboard
from colorama import Fore, Style
from datetime import datetime
from termcolor import colored
from colorama import init
init()
print(Style.RESET_ALL)


# black, red, green, yellow, blue, magenta, cyan, white
colors = ['black', 'red', 'green', 'yellow',
          'blue', 'magenta', 'cyan', 'white']

print("RF trackbot - credits to MATIEO33")
print("RF: https://robloxforum.com/members/matieo33.8832/")
print("Github: https://github.com/matieo33")
print("Available options: TRACK INFO")
in_menu = 1
while in_menu == 1:
    decision = str(input(Fore.GREEN))
    print(Fore.RESET, end='')
    if decision == "INFO":
        print("I made this bot purely for the purpose of entertainment, and if ever happens - maybe also will come in handy for somebody.")
        print("Wanna help this bot grow? Ping me on caci's/RF server, or DM me!")
        print("CONTROLS: CTRL + C will entirely stop the program, requiring you to restart.")
    elif decision == "TRACK":
        in_menu = 0
    else:
        print("You typed something that was never intended, retry.")

a = int(input("Every how much seconds do you wish to recieve updates on the site activity? "))
b = str(input("Do you wish the data to be saved to a TXT file? (Y/N) "))
if b == "Y":
    c = str(input('Do you wish to include the list of all online users? (Y/N) '))


print('')

process = 1
while process == 1:
    obj = time.localtime()
    currentime = time.asctime(obj)
    time.sleep(a)
    source = requests.get('https://www.robloxforum.com').text
    soup = BeautifulSoup(source, 'lxml')
    stringy = soup.find('span', class_='block-footer-counter').text
    usernames = soup.find_all('span', class_=['username--style1', 'username--style2', 'username--style3', 'username--style4',
                                              'username--style5', 'username--style6', 'username--style7', 'username--style8', 'username--style9', 'username--style10'
                                              'username--style11'])
    print(currentime)
    print(stringy)
    for span in usernames:
        attr = span.attrs['class']
        numbas = re.findall(r'\d+', str(attr))
        if numbas[0] == "2":
            print(span.text)
        elif numbas[0] == "3":
            print(colored(span.text, 'red', attrs=['bold']))
        elif numbas[0] == "4":
            print(colored(span.text, 'blue', attrs=['bold']))
        elif numbas[0] == "6":
            print(colored(span.text, 'green', attrs=['bold']))
        elif numbas[0] == "7":
            print(colored(span.text, 'green'))
        elif numbas[0] == "8":
            print(colored(span.text, 'blue'))
        elif numbas[0] == "9":
            print(colored(span.text, 'yellow'))
        elif numbas[0] == "10":
            def strike(text):
                return ''.join([u'\u0336{}'.format(c) for c in text])
            black = (colored(span.text, 'yellow'))
            print(strike(black))
        elif numbas[0] == "11":
            print(colored(span.text, 'blue', attrs=['bold']))
    print('\n')
    if b == "Y":
        with open("log.txt", "a") as o:
            encoded_string = stringy.encode("ascii", "ignore")
            decode_string = encoded_string.decode()
            o.write(decode_string)
            for span in usernames:
                attr = span.attrs['class']
                numbas = re.findall(r'\d+', str(attr))
                sp = span.text
                obj = time.localtime()
                currentime = time.asctime(obj)
                if c == "Y":
                    o.write(currentime)
                    if numbas[0] == "2":
                        o.write(sp + " | normal user")
                        o.write('\n')
                    elif numbas[0] == "3":
                        o.write(sp + " | administrator")
                        o.write('\n')
                    elif numbas[0] == "4":
                        o.write(sp + " | moderator")
                        o.write('\n')
                    elif numbas[0] == "6":
                        o.write(sp + " | verified")
                        o.write('\n')
                    elif numbas[0] == "7":
                        o.write(sp + " | vip")
                        o.write('\n')
                    elif numbas[0] == "8":
                        o.write(sp + " | pro")
                        o.write('\n')
                    elif numbas[0] == "9":
                        o.write(sp + " | ultra")
                        o.write('\n')
                    elif numbas[0] == "10":
                        o.write(sp + " | banned")
                        o.write('\n')
                    o.write('\n')
                else:
                    pass
    else:
        pass