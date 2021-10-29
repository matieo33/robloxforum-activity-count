from bs4 import BeautifulSoup
import requests
import time
from colorama import Fore, Back, Style
from colorama import init
init()
print(Fore.RED + 'in order')
print(Style.RESET_ALL)


# black, red, green, yellow, blue, magenta, cyan, white
colors = ['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']


print("RF trackbot")
a = int(input("Every how much seconds do you wish to recieve updates on the site activity? "))
b = str(input("Do you wish the data to be saved to a TXT file? (Y/N) "))

process = 1
while process == 1:
    time.sleep(a)
    source = requests.get('https://www.robloxforum.com').text
    soup = BeautifulSoup(source, 'lxml')
    stringy = soup.find('span', class_='block-footer-counter').text
    usernames = soup.find_all('span', class_=['username--style1', 'username--style2', 'username--style3', 'username--style4',
    'username--style5', 'username--style6', 'username--style7', 'username--style8', 'username--style9', 'username--style10'
    'username--style11', 'username--style12'])
    print(stringy)
    for span in usernames:
        print(span.text)
    print('\n')
    if b == "Y":
        with open("log.txt", "a") as o:
            encoded_string = stringy.encode("ascii", "ignore")
            decode_string = encoded_string.decode()
            o.write(decode_string)
    else:
        pass