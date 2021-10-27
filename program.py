from bs4 import BeautifulSoup
import requests, time
process = 1
while process == 1:
    source = requests.get('https://www.robloxforum.com').text
    soup = BeautifulSoup(source, 'lxml')
    gay = soup.find('span', class_='block-footer-counter').text
    with open("logs.txt", "a") as o:
        time.sleep(1)
        encoded_string = gay.encode("ascii", "ignore")
        decode_string = encoded_string.decode()
        o.write(decode_string)
