from bs4 import BeautifulSoup
import requests, time
process = 1
while process == 1:
    source = requests.get('https://www.robloxforum.com').text
    soup = BeautifulSoup(source, 'lxml')
    text = soup.find('span', class_='block-footer-counter').text