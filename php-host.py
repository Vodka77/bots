import telebot
import requests
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
    ca = types.InlineKeyboardButton(text ="- Create Account",callback_data = 'acc')
    ch = types.InlineKeyboardButton(text ="- Channel",url='https://t.me/Vodka_Tools')    
    maac.row_width = 2
    maac.add(ca,ch)    
    bro = f"<a href='https://t.me/{message.from_user.username}'>{message.from_user.first_name}</a>"            
    bot.send_message(message.chat.id , f'<b>Hi {bro}\n- - - - - - - - - - - - - -\nWelcome To Host pantheonsite Account Maker\nClick Create Account To Create One\n- - - - - - - - - - - - - -\nBy  : @PPPK_P</b>', parse_mode="html",disable_web_page_preview=True,reply_to_message_id=message.message_id, reply_markup=maac)
@bot.message_handler(commands=['about'])
def start(message):
    bot.send_message(message.chat.id,f'<b>Hello Dear\nI Make This To Be Easy To php Host For Bots Api ...\nThe Bot Make a 100% Host It Works Correct\n Without Any Problems\nIf You Have Any Problem \nContact Here : @l_dll</b> ',parse_mode='html')
@bot.callback_query_handler(func=(lambda call:True))
def callback_inline(call):
    if call.data == "acc":
        data = requests.get(f'https://vodka-toolsx.herokuapp.com/Host-Maker/?type=1').json()
        eml = data['Email']

        weblogin = "<a href='https://pantheon.auth0.com/login?state=hKFo2SBKblczb3JaS3V6RHBTdnRUME5SbWdaMXFkRnVQaVljUKFupWxvZ2luo3RpZNkgU3M4S3B6YTJlUGRQaU1GRUNlaTJ3aDlfR1VDbU1mV06jY2lk2SBxOWZXajl4blB4NE9BQVk5SU5ZZGNmaVlJVGtHdmFIcg&client=q9fWj9xnPx4OAAY9INYdcfiYITkGvaHr&protocol=oauth2&response_type=code&redirect_uri=https%3A%2F%2Fdashboard.pantheon.io%2Fauth%2Fcallback&scope=login%20openid%20pantheon&connection='>Here</a>"
        bot.send_message(call.message.chat.id,f'<b>Done Create Host Account 🧑‍💻\n- - - - - - - - - - -\nEmail : <code>{eml}</code>\nPassword : <code>QX#kC_Gdk%a</code>\nLogin Url : {weblogin}\n- - - - - - - - - - -\nBy : @Vodka_Tools</b>',parse_mode='html')    

bot.polling(True)            
