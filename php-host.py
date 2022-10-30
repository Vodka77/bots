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
bot = telebot.TeleBot('5609332892:AAFAbSMpaHDPEQZNYEA5nBj7DIpB9-89WTE')
@bot.message_handler(commands=['start','help'])
def start(message):
    print(message.from_user.id)
    print('@',message.from_user.username)
    maac = types.InlineKeyboardMarkup()
    ca = types.InlineKeyboardButton(text ="- PHP Host",callback_data = 'acc')
    py = types.InlineKeyboardButton(text ="- Python Host",callback_data = 'make')
    ch = types.InlineKeyboardButton(text ="- Channel",url='https://t.me/Vodka_Tools')    
    maac.row_width = 2
    maac.add(ca,py,ch)    
    bro = f"<a href='https://t.me/{message.from_user.username}'>{message.from_user.first_name}</a>"            
    bot.send_message(message.chat.id , f'<b>Hi {bro}\n- - - - - - - - - - - - - -\nWelcome To Host pantheonsite Account Maker\nClick Create Account To Create One\n- - - - - - - - - - - - - -\nBy  : @PPPK_P</b>', parse_mode="html",disable_web_page_preview=True,reply_to_message_id=message.message_id, reply_markup=maac)
@bot.message_handler(commands=['about'])
def start(message):
    bot.send_message(message.chat.id,f'<b>Hello Dear\nI Make This To Be Easy To php Host For Bots Api ...\nThe Bot Make a 100% Host It Works Correct\n Without Any Problems\nIf You Have Any Problem \nContact Here : @l_dll</b> ',parse_mode='html')
@bot.callback_query_handler(func=(lambda call:True))
def callback_inline(call):
    if call.data == 'make':
        host = requests.get('https://apisx.pythonanywhere.com/Host/Maker').json()['result']
        user = host['user']
        email = host['email']
        passw = host['pass']
        login = host['login']
        web_url = host['Website-Url']
        log = f"<a href='{login}'>Login-Url</a>"  
        name = f"<a href='{call.from_user.first_name}'>{call.from_user.first_name}</a>" 
        maac = types.InlineKeyboardMarkup()
        make = types.InlineKeyboardButton(text="Make Host",callback_data='make2')
        maac.row_width = 2
        maac.add(make)
        bot.edit_message_text(chat_id=(call.message.chat.id),message_id=(call.message.id),text=f'<b>Hi {name}\n- - - - - - - -\nEmail : {email}\nUserName : {user}\nPassword : {passw}\nLogin : {log}\nWebsite-Url : {web_url}\n- - - - - - - -\nBy : @Vodka_Tools</b>',parse_mode='html',reply_markup=maac,disable_web_page_preview=True)
    if call.data == 'make2':
        host2 = requests.get('https://apisx.pythonanywhere.com/Host/Maker').json()['result']
        user = host2['user']
        email = host2['email']
        passw = host2['pass']
        login = host2['login']
        web_url = host2['Website-Url']
        log = f"<a href='{login}'>Login-Url</a>"  
        name = f"<a href='{call.from_user.first_name}'>{call.from_user.first_name}</a>" 
        maac = types.InlineKeyboardMarkup()
        make = types.InlineKeyboardButton(text="Make Host",callback_data='make2')
        maac.row_width = 2
        maac.add(make)
        bot.edit_message_text(chat_id=(call.message.chat.id),message_id=(call.message.id),text=f'<b>Hi {name}\n- - - - - - - -\nEmail : {email}\nUserName : {user}\nPassword : {passw}\nLogin : {log}\nWebsite-Url : {web_url}\n- - - - - - - -\nBy : @Vodka_Tools</b>',parse_mode='html',reply_markup=maac,disable_web_page_preview=True)
    if call.data == "acc":
        maac3 = types.InlineKeyboardMarkup()
        make1 = types.InlineKeyboardButton(text="Make Host",callback_data='make22')
        maac3.row_width = 2
        maac3.add(make1)
        data = requests.get(f'https://vodka-toolsx.herokuapp.com/Host-Maker/?type=1').json()
        eml = data['Email']
        weblogin = "<a href='https://pantheon.auth0.com/login?state=hKFo2SBKblczb3JaS3V6RHBTdnRUME5SbWdaMXFkRnVQaVljUKFupWxvZ2luo3RpZNkgU3M4S3B6YTJlUGRQaU1GRUNlaTJ3aDlfR1VDbU1mV06jY2lk2SBxOWZXajl4blB4NE9BQVk5SU5ZZGNmaVlJVGtHdmFIcg&client=q9fWj9xnPx4OAAY9INYdcfiYITkGvaHr&protocol=oauth2&response_type=code&redirect_uri=https%3A%2F%2Fdashboard.pantheon.io%2Fauth%2Fcallback&scope=login%20openid%20pantheon&connection='>Here</a>"
        bot.edit_message_text(chat_id=(call.message.chat.id),message_id=(call.message.id),text='<b>Done Create Host Account 🧑‍💻\n- - - - - - - - - - -\nEmail : <code>{eml}</code>\nPassword : <code>QX#kC_Gdk%a</code>\nLogin Url : {weblogin}\n- - - - - - - - - - -\nBy : @Vodka_Tools</b>',parse_mode='html',reply_markup=maac3,disable_web_page_preview=True) 
    if call.data == "make22":
        maac3 = types.InlineKeyboardMarkup()
        make1 = types.InlineKeyboardButton(text="Make Host",callback_data='make22')
        maac3.row_width = 2
        maac3.add(make1)
        data = requests.get(f'https://vodka-toolsx.herokuapp.com/Host-Maker/?type=1').json()
        eml = data['Email']
        weblogin = "<a href='https://pantheon.auth0.com/login?state=hKFo2SBKblczb3JaS3V6RHBTdnRUME5SbWdaMXFkRnVQaVljUKFupWxvZ2luo3RpZNkgU3M4S3B6YTJlUGRQaU1GRUNlaTJ3aDlfR1VDbU1mV06jY2lk2SBxOWZXajl4blB4NE9BQVk5SU5ZZGNmaVlJVGtHdmFIcg&client=q9fWj9xnPx4OAAY9INYdcfiYITkGvaHr&protocol=oauth2&response_type=code&redirect_uri=https%3A%2F%2Fdashboard.pantheon.io%2Fauth%2Fcallback&scope=login%20openid%20pantheon&connection='>Here</a>"
        bot.edit_message_text(chat_id=(call.message.chat.id),message_id=(call.message.id),text='<b>Done Create Host Account 🧑‍💻\n- - - - - - - - - - -\nEmail : <code>{eml}</code>\nPassword : <code>QX#kC_Gdk%a</code>\nLogin Url : {weblogin}\n- - - - - - - - - - -\nBy : @Vodka_Tools</b>',parse_mode='html',reply_markup=maac3,disable_web_page_preview=True) 

bot.polling(True)            
