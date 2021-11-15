try:
    import logo as logo_print
except ModuleNotFoundError:
    missingfile = str(input("The program is missing a file. Continue anyways? "))
    if missingfile == "yes" or "y" or "Y" or "Yes" or "YES":
        pass
    else:
        os.exit(0)

try:
    from bs4 import BeautifulSoup
    import requests
    import time
    import re
    from termcolor import colored
    from colorama import init
    import os
except ModuleNotFoundError:
    print(colored("The program is missing essential libraries. Read the Github's tutorial how to install all the libraries.", 'red'))
    os.exit(0)

os.system("mode con cols=150 lines=75")
decision = ''
init()

# DEFS BELOW


def print_status():
    obj = time.localtime()
    currentime = time.asctime(obj)
    if decision == 'SAMPLE' or decision.lower == 'sample':
        pass
    else:
        time.sleep(a)
    source = requests.get('https://www.robloxforum.com').text
    soup = BeautifulSoup(source, 'lxml')
    stringy = soup.find('span', class_='block-footer-counter').text
    usernames = soup.find_all('span', class_=['username--style1', 'username--style2', 'username--style3', 'username--style4',
                                              'username--style5', 'username--style6', 'username--style7', 'username--style8', 'username--style9', 'username--style10'
                                              'username--style11'])
    whitespace_remove = stringy.replace('				Robots', "Robots")
    print(currentime)
    print(whitespace_remove)
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
    if decision == 'SAMPLE':
        print()
    else:
        if b == "Y":
            with open("log.txt", "a") as o:
                encoded_string = stringy.encode("ascii", "ignore")
                decode_string = encoded_string.decode()
                whitespace_remove = decode_string.replace('				Robots', "Robots")
                o.write(whitespace_remove)
                if c == "Y": o.write(currentime + '\n')
                for span in usernames:
                    attr = span.attrs['class']
                    numbas = re.findall(r'\d+', str(attr))
                    sp = span.text
                    obj = time.localtime()
                    currentime = time.asctime(obj)
                    if c == "Y":
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


def run():
    process = 1
    while process == 1:
        print_status()
# DEFS ABOVE

try:
    print(logo_print.final_str)
except ModuleNotFoundError:
    pass
print(colored("RF trackbot - credits to MATIEO33", 'blue'))
print(colored("RF: https://robloxforum.com/members/matieo33.8832/", 'red'))
print(colored("Github: https://github.com/matieo33", 'green'))
print("Available options: TRACK SAMPLE HELP \n")

if __name__ == '__main__':
    in_menu = 1
    while in_menu == 1:
        decision = str(input())
        if decision == "HELP" or decision.lower() == 'help':
            print("I made this bot purely for the purpose of entertainment, and if ever happens - maybe also will come in handy for somebody.")
            print("Wanna help this bot grow? DM me.")
            print('Important: CTRL + C will stop the program entirely! Make sure to answer with "Y" if you wish to save the data to a TXT file.')
            print(
                "TRACK: Prints the activity of the site per amount of seconds you select.")
            print(
                "SAMPLE: Prints the activity of the site one time as an example of the program's work.")
        elif decision == "SAMPLE" or decision.lower() == 'sample':
            print('')
            print_status()
        elif decision == "TRACK" or decision.lower() == 'track':
            print('')
            in_menu = 0
        else:
            print("ERROR: unknown command " + "'" + decision + "'")

    a = int(input(
        "Every how much seconds do you wish to recieve updates on the site activity? "))
    b = str(input("Do you wish the data to be saved to a TXT file? (Y/N) "))
    if b == "Y":
        c = str(input('Do you wish to include the list of all online users? (Y/N) '))
        while 1:
            print_status()
    else:
        while 1:
            print_status()
