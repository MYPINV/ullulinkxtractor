from typing import cast
import requests
from requests.sessions import merge_setting
import telebot

headers = {'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}

bot = telebot.TeleBot("1764551909:AAH7JJ2gK-K1LKwRvho5fibeW10QO3ScuGI")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    print(message.chat.id)
    if message.chat.id == -1001475242453 or message.chat.id == 941874401:
	    bot.reply_to(message, """welcome User ,i can give you access to ullu direct links,
Format of usage:
/ullu https://ullulink

Enjoy & Stay Safe  """)
    else:
        bot.reply_to(message,"Note:Bot will not respond to any of your messages as bot can only be used by bot-owner")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    url = (message.text).split(" ")[1]
    print(url)
    geturl = url
    #print(url)
    new_url = geturl.replace("https://ullu.app/#/media/","")
    print(new_url)
    req_url = "https://ullu.app/ulluCore/api/v2/media/fetchMediaBySlug?titleYearSlug="+new_url
    print(req_url)
    try:
        
        response = requests.get(req_url,headers).json()
        #print(response)
        #print(response['mediaFileUrl'])
        title = response["title"]
        descp = response["description"]
        cast_here = response["cast"]
        director_here = response["director"]
        release_date =response["releaseDate"]
        poster_url = "https://d3qpi926vijvfo.cloudfront.net/"+response["landscapePosterId"]

        mediafileurl = response['mediaFileUrl']
    except:
        bot.reply_to(message,"Something went wrong")
    #replacing the mediurl to get working m3u8 link
    
    if mediafileurl != None:
        mediafileurl = mediafileurl.replace("playlist.m3u8","chunklist_b1323870_sleng.m3u8")

        bot.reply_to(message,f""" {title}-{release_date}
Desc:{descp}
Cast:{cast_here}
Director:{director_here}
posterURL:{poster_url}

Episode link:{mediafileurl}

Stay Safe """)

    else:
        videos = response["seasons"][0]["episodeList"]
        epno = 1
        output = []
        button =""" """
        for video in videos:
            mediafileurl = video["video"]["mediaFileUrl"]
            mediafileurl = mediafileurl.replace("playlist.m3u8","chunklist_b1323870_sleng.m3u8")
        
            #result = {"Episode":epno,"Url":mediafileurl}
            button = button + f"""Episode {epno}:{mediafileurl}
            
"""
            #output.append(mediafileurl)
            epno +=1
        bot.reply_to(message,f""" {title}-{release_date}
Desc:{descp}
Cast:{cast_here}
Director:{director_here}
posterURL:{poster_url}

{button}

Stay Safe """)


bot.polling()

    

