#!/usr/bin/python3
import requests
import json
import time

from telegram.ext import Updater
#import logging
from telegram.ext import CommandHandler

#We obtained 5 more recent videos according to the chosen cateogry.
#It's a very early version. It works well, but there's a lot of code repeated.


#EDIT TOKEN!!!!!!!!!!!!!!
updater = Updater(token='*********************************************************************', use_context=True)
dispatcher = updater.dispatcher

#logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                     level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hi!.............. ==> /help")

#EDIT <CATEGORY OF PRONHUB> !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def <CATEGORY OF PRONHUB1>(update, context):
    CATEGORYWEB="<CATEGORY OF PRONHUB1>"
    #GET VIDEOS BY CATEGORY ORDER BY NEWEST
    r = requests.get('https://es.pornhub.com/webmasters/search?search=' + CATEGORYWEB + '&ordering=newest')
    rjson=r.json()
    count=0
    listurls=[]
    for urls in rjson["videos"]:
        if count<5:
            count=count+1
            context.bot.send_message(chat_id=update.effective_chat.id, text=urls["url"])
            time.sleep(1)


def <CATEGORY OF PRONHUB2>(update, context):
    CATEGORYWEB="<CATEGORY OF PRONHUB2>"
    #GET VIDEOS BY CATEGORY ORDER BY NEWEST
    r = requests.get('https://es.pornhub.com/webmasters/search?search=' + CATEGORYWEB + '&ordering=newest')
    rjson=r.json()
    count=0
    listurls=[]
    for urls in rjson["videos"]:
        if count<5:
            count=count+1 
            context.bot.send_message(chat_id=update.effective_chat.id, text=urls["url"])
            time.sleep(1)

def <CATEGORY OF PRONHUB3>(update, context):
    CATEGORYWEB="<CATEGORY OF PRONHUB3>"
    #GET VIDEOS BY CATEGORY ORDER BY NEWEST
    r = requests.get('https://es.pornhub.com/webmasters/search?search=' + CATEGORYWEB + '&ordering=newest')
    rjson=r.json()
    count=0
    listurls=[]
    for urls in rjson["videos"]:
        if count<5:
            count=count+1 
            context.bot.send_message(chat_id=update.effective_chat.id, text=urls["url"])
            time.sleep(1)

def <CATEGORY OF PRONHUB4>(update, context):
    CATEGORYWEB="<CATEGORY OF PRONHUB4>"
    #GET VIDEOS BY CATEGORY ORDER BY NEWEST
    r = requests.get('https://es.pornhub.com/webmasters/search?search=' + CATEGORYWEB + '&ordering=newest')
    rjson=r.json()
    count=0
    listurls=[]
    for urls in rjson["videos"]:
        if count<5:
            count=count+1 
            context.bot.send_message(chat_id=update.effective_chat.id, text=urls["url"])
            time.sleep(1)

def <CATEGORY OF PRONHUB5>(update, context):
    CATEGORYWEB="<CATEGORY OF PRONHUB5>"
    #GET VIDEOS BY CATEGORY ORDER BY NEWEST
    r = requests.get('https://es.pornhub.com/webmasters/search?search=' + CATEGORYWEB + '&ordering=newest')
    rjson=r.json()
    count=0
    listurls=[]
    for urls in rjson["videos"]:
        if count<5:
            count=count+1 
            context.bot.send_message(chat_id=update.effective_chat.id, text=urls["url"])
            time.sleep(1)

def <CATEGORY OF PRONHUB6>(update, context):
    CATEGORYWEB="<CATEGORY OF PRONHUB6>"
    #GET VIDEOS BY CATEGORY ORDER BY NEWEST
    r = requests.get('https://es.pornhub.com/webmasters/search?search=' + CATEGORYWEB + '&ordering=newest')
    rjson=r.json()
    count=0
    listurls=[]
    for urls in rjson["videos"]:
        if count<5:
            count=count+1 
            context.bot.send_message(chat_id=update.effective_chat.id, text=urls["url"])
            time.sleep(1)

def <CATEGORY OF PRONHUB7>(update, context):
    CATEGORYWEB="<CATEGORY OF PRONHUB7>"
    #GET VIDEOS BY CATEGORY ORDER BY NEWEST
    r = requests.get('https://es.pornhub.com/webmasters/search?search=' + CATEGORYWEB + '&ordering=newest')
    rjson=r.json()
    count=0
    listurls=[]
    for urls in rjson["videos"]:
        if count<5:
            count=count+1 
            context.bot.send_message(chat_id=update.effective_chat.id, text=urls["url"])
            time.sleep(1)

def <CATEGORY OF PRONHUB8>(update, context):
    CATEGORYWEB="<CATEGORY OF PRONHUB8>"
    #GET VIDEOS BY CATEGORY ORDER BY NEWEST
    r = requests.get('https://es.pornhub.com/webmasters/search?search=' + CATEGORYWEB + '&ordering=newest')
    rjson=r.json()
    count=0
    listurls=[]
    for urls in rjson["videos"]:
        if count<5:
            count=count+1 
            context.bot.send_message(chat_id=update.effective_chat.id, text=urls["url"])
            time.sleep(1)

def <CATEGORY OF PRONHUB9>(update, context):
    CATEGORYWEB="<CATEGORY OF PRONHUB9>"
    #GET VIDEOS BY CATEGORY ORDER BY NEWEST
    r = requests.get('https://es.pornhub.com/webmasters/search?search=' + CATEGORYWEB + '&ordering=newest')
    rjson=r.json()
    count=0
    listurls=[]
    for urls in rjson["videos"]:
        if count<5:
            count=count+1 
            context.bot.send_message(chat_id=update.effective_chat.id, text=urls["url"])
            time.sleep(1)

def <CATEGORY OF PRONHUB10>(update, context):
    CATEGORYWEB="<CATEGORY OF PRONHUB10>"
    #GET VIDEOS BY CATEGORY ORDER BY NEWEST
    r = requests.get('https://es.pornhub.com/webmasters/search?search=' + CATEGORYWEB + '&ordering=newest')
    rjson=r.json()
    count=0
    listurls=[]
    for urls in rjson["videos"]:
        if count<5:
            count=count+1 
            context.bot.send_message(chat_id=update.effective_chat.id, text=urls["url"])
            time.sleep(1)

def <CATEGORY OF PRONHUB11>(update, context):
    CATEGORYWEB="<CATEGORY OF PRONHUB11>"
    #GET VIDEOS BY CATEGORY ORDER BY NEWEST
    r = requests.get('https://es.pornhub.com/webmasters/search?search=' + CATEGORYWEB + '&ordering=newest')
    rjson=r.json()
    count=0
    listurls=[]
    for urls in rjson["videos"]:
        if count<5:
            count=count+1 
            context.bot.send_message(chat_id=update.effective_chat.id, text=urls["url"])
            time.sleep(1)

def <CATEGORY OF PRONHUB12>(update, context):
    CATEGORYWEB="<CATEGORY OF PRONHUB12>"
    #GET VIDEOS BY CATEGORY ORDER BY NEWEST
    r = requests.get('https://es.pornhub.com/webmasters/search?search=' + CATEGORYWEB + '&ordering=newest')
    rjson=r.json()
    count=0
    listurls=[]
    for urls in rjson["videos"]:
        if count<5:
            count=count+1 
            context.bot.send_message(chat_id=update.effective_chat.id, text=urls["url"])
            time.sleep(1)

def <CATEGORY OF PRONHUB13>(update, context):
    CATEGORYWEB="<CATEGORY OF PRONHUB13>"
    #GET VIDEOS BY CATEGORY ORDER BY NEWEST
    r = requests.get('https://es.pornhub.com/webmasters/search?search=' + CATEGORYWEB + '&ordering=newest')
    rjson=r.json()
    count=0
    listurls=[]
    for urls in rjson["videos"]:
        if count<5:
            count=count+1 
            context.bot.send_message(chat_id=update.effective_chat.id, text=urls["url"])
            time.sleep(1)

def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="help text...............\n")

#EDIT <CATEGORY OF PRONHUB> !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

start_handler = CommandHandler('<CATEGORY OF PRONHUB1>', <CATEGORY OF PRONHUB1>)
dispatcher.add_handler(start_handler)

start_handler = CommandHandler('<CATEGORY OF PRONHUB2>', <CATEGORY OF PRONHUB2>)
dispatcher.add_handler(start_handler)

start_handler = CommandHandler('<CATEGORY OF PRONHUB3>', <CATEGORY OF PRONHUB3>)
dispatcher.add_handler(start_handler)

start_handler = CommandHandler('<CATEGORY OF PRONHUB4>', <CATEGORY OF PRONHUB4>)
dispatcher.add_handler(start_handler)

start_handler = CommandHandler('<CATEGORY OF PRONHUB5>', <CATEGORY OF PRONHUB5>)
dispatcher.add_handler(start_handler)

start_handler = CommandHandler('<CATEGORY OF PRONHUB6>', <CATEGORY OF PRONHUB6>)
dispatcher.add_handler(start_handler)

start_handler = CommandHandler('<CATEGORY OF PRONHUB7>', <CATEGORY OF PRONHUB7>)
dispatcher.add_handler(start_handler)

start_handler = CommandHandler('<CATEGORY OF PRONHUB8>', <CATEGORY OF PRONHUB8>)
dispatcher.add_handler(start_handler)

start_handler = CommandHandler('<CATEGORY OF PRONHUB9>', <CATEGORY OF PRONHUB9>)
dispatcher.add_handler(start_handler)

start_handler = CommandHandler('<CATEGORY OF PRONHUB10>', <CATEGORY OF PRONHUB10>)
dispatcher.add_handler(start_handler)

start_handler = CommandHandler('<CATEGORY OF PRONHUB11>', <CATEGORY OF PRONHUB11>)
dispatcher.add_handler(start_handler)

start_handler = CommandHandler('<CATEGORY OF PRONHUB12>', <CATEGORY OF PRONHUB12>)
dispatcher.add_handler(start_handler)

start_handler = CommandHandler('<CATEGORY OF PRONHUB13>', <CATEGORY OF PRONHUB13>)
dispatcher.add_handler(start_handler)

start_handler = CommandHandler('help', help)
dispatcher.add_handler(start_handler)

updater.start_polling()
#FOR TEST IN IPYTHON:
#updater.idle()






#To improve...
#def getpornbycategory(search):
#    CATEGORY=search
#    CATEGORYWEB=CATEGORY.replace(' ','_')
#
#    #GET VIDEOS BY CATEGORY ORDER BY NEWEST
#    r = requests.get('https://es.pornhub.com/webmasters/search?search=' + CATEGORYWEB + '&ordering=newest')
#    rjson=r.json()
#    count=0
#    listurls=[]
#    for urls in rjson["videos"]:
#        if count<3:
#            count=count+1
#            listurls.append(urls["url"])
#    return listurls
    