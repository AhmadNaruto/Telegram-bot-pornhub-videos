#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup

##########CONFIG####################
APITOKEN="************************************************"
GROUP="-***********"

base_url = 'https://pornhub.com'
last_url = ''

#RANDOM VIDEO
def get(url, no_cache=False):
    headers = {
        'User-Agent': 'A Telegram bot inspired in cybits/cybot',
    }
    if no_cache:
        headers['Cache-Control'] = 'private,max-age=0'
    return requests.get(base_url + url, headers=headers)

def get_random_title():
    r = get('/random')
    soup = BeautifulSoup(str(r.content, 'UTF-8', errors='replace'))
    last_url = r.url
    return soup.find('title').text.split(' - Pornhub.com')[0],last_url

message="Good morning! ;) \n \n" + get_random_title()[1]

#SEND TO TELEGRAM
requests.post('https://api.telegram.org/bot'+ APITOKEN + '/sendMessage',data={'chat_id': GROUP, 'text': message})

