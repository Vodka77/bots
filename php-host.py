import telebot
import requests
import random
from telebot import types
from time import sleep
import time
Z = '\x1b[1;31m'#احمر
X = '\x1b[1;32m'#اخضر
C = '\x1b[1;33m'#yellow
V = '\x1b[1;34m'#blue	
B = '\x1b[1;35m'#pink
N = '\x1b[1;36m'#لبني
M = '\x1b[1;37m'#ابيض
token = ('5609332892:AAFAbSMpaHDPEQZNYEA5nBj7DIpB9-89WTE')
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start','help'])
def start(message):
    if message.chat.type == 'private':
        ch = 'Vodka_Tools'
        idu = message.chat.id
        join = requests.get(f"https://api.telegram.org/bot{token}/getChatMember?chat_id=@{ch}&user_id={idu}").text
        if '"status":"left"' in join:
            bot.send_message(message.chat.id, '\n🚸| عذرا عزيزي\n🧿| عليك الاشتراك بقناة البوت لتتمكن من استخدامه\n\n- https://t.me/Vodka_Tools\n\n‼️| اشترك ثم ارسل /start\n                    ',disable_web_page_preview=True)
        ch = 'TBGBT'
        idu = message.chat.id
        join = requests.get(f"https://api.telegram.org/bot{token}/getChatMember?chat_id=@{ch}&user_id={idu}").text
        if '"status":"left"' in join:
            bot.send_message(message.chat.id, '\n🚸| عذرا عزيزي\n🧿| عليك الاشتراك بقناة البوت لتتمكن من استخدامه\n\n- https://t.me/TBGBT\n\n‼️| اشترك ثم ارسل /start\n                    ',disable_web_page_preview=True)
        else:
            print(message.from_user.id)
            print('@',message.from_user.username)
            maac = types.InlineKeyboardMarkup()
            ca = types.InlineKeyboardButton(text ="- PHP Host",callback_data = 'acc')
            py = types.InlineKeyboardButton(text ="- Python Host",callback_data = 'make')
            ch = types.InlineKeyboardButton(text ="- Channel",url='https://t.me/Vodka_Tools')    
            maac.row_width = 2
            maac.add(ca,py,ch)    
            bro = f"<a href='https://t.me/{message.from_user.username}'>{message.from_user.first_name}</a>"            
            bot.send_message(message.chat.id , f'<b>Hi {bro}\n- - - - - - - - - - - - - -\nWelcome To Make python & php Host Maker\nClick python host to create python one\nclick php host to create php one\n- - - - - - - - - - - - - -\nBy  : @l_dll</b>', parse_mode="html",disable_web_page_preview=True,reply_to_message_id=message.message_id, reply_markup=maac)
            @bot.message_handler(commands=['about'])
            def start(message):
                bot.send_message(message.chat.id,f'<b>Hello Dear\nI Make This To Be Easy To php & python Host For Bots Api ...\nThe Bot Make a 100% Host It Works Correct\n Without Any Problems\nIf You Have Any Problem \nContact Here : @l_dll</b> ',parse_mode='html')
            @bot.callback_query_handler(func=(lambda call:True))
            def callback_inline(call):
                if call.data == 'make':
                    host = requests.get('https://vodka-toolsx.herokuapp.com/Host-Maker/?type=2').json()
                    user = host['user']
                    email = host['Email']
                    passw = host['Password']
                    login = host['login']
                    web_url = host['Website-Url']
                    log = f"<a href='{login}'>Login-Url</a>"  
                    name = f"<a href='{call.from_user.first_name}'>{call.from_user.first_name}</a>" 
                    bot.send_message(call.message.chat.id,f'<b>Done Create python Host Account 🧑‍💻\n- - - - - - - - - - - -\nEmail : <code>{email}</code>\nUserName : <code>{user}</code>\nPassword : <code>{passw}</code>\nLogin : {log}\nWebsite-Url : {web_url}\n- - - - - - - - - - - -\nBy : @Vodka_Tools</b>',parse_mode='html',disable_web_page_preview=True)
                if call.data == "acc":
                    data = requests.get(f'https://vodka-toolsx.herokuapp.com/Host-Maker/?type=1').json()
                    eml = data['Email']
                    weblogin = "<a href='https://pantheon.auth0.com/login?state=hKFo2SBKblczb3JaS3V6RHBTdnRUME5SbWdaMXFkRnVQaVljUKFupWxvZ2luo3RpZNkgU3M4S3B6YTJlUGRQaU1GRUNlaTJ3aDlfR1VDbU1mV06jY2lk2SBxOWZXajl4blB4NE9BQVk5SU5ZZGNmaVlJVGtHdmFIcg&client=q9fWj9xnPx4OAAY9INYdcfiYITkGvaHr&protocol=oauth2&response_type=code&redirect_uri=https%3A%2F%2Fdashboard.pantheon.io%2Fauth%2Fcallback&scope=login%20openid%20pantheon&connection='>Here</a>"
                    bot.send_message(call.message.chat.id,f'<b>Done Create php Host Account 🧑‍💻\n- - - - - - - - - - -\nEmail : <code>{eml}</code>\nPassword : <code>QX#kC_Gdk%a</code>\nLogin Url : {weblogin}\n- - - - - - - - - - -\nBy : @Vodka_Tools</b>',parse_mode='html',disable_web_page_preview=True) 
                                  
bot.polling(True)
