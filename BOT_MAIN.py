from telebot import types
import telebot
import random
import requests
import urllib.parse
from bs4 import BeautifulSoup
from  selenium import webdriver
import selenium
from time import sleep
import web3
from web3 import Web3, HTTPProvider
from eth_account import Account
from decimal import Decimal

global trades
trades = []

w3 = Web3(HTTPProvider("https://kovan.infura.io/v3/4e43dd6059ae4f2981f75ea4169bdcda"))
w31 = Web3(HTTPProvider("https://sokol.poa.network"))
name = 'user'
acc = web3.eth.Account.create(name)
acc.address
print(acc.address)
acct = Account.privateKeyToAccount('b3fc0f5709b87119403d0df1a0c590b897b71e248a973f3ba1a096e3a6755919')
acct.address

1
API_TOKEN = '1235901893:AAGMf_6d8yt3lYMHAx0-AG_VEhX6YCALJVc'
keyboard22 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard22.row('Русский 🇷🇺', 'English 🇺🇸')
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Change CRYPTO', 'Sell CRYPTO(В разработке)')
keyboard1.row('Cryptocurrency Rate')
keyboard5 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard5.row('Обменять крипту', 'Продать крипту(В разработке)')
keyboard5.row('Курс криптовалют')
keyboard2 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard2.row('Bitcoin/BTC')

bot = telebot.TeleBot(API_TOKEN)


global ltest
ltest = []
global lux_list
lux_list = []
global gl
gl = ''
global mn
mn = ''
global ml
ml = []
global ll
ll = ''
global mk11
mk11 = ''
global mk12
mk12 = ''
global mk13
mk13 = ''
global not_stonks
not_stonks = ''
global not_stonks1
not_stonks = ''
global not_stonks2
not_stonks = ''
global userlist
userlist = []


driver = webdriver.Chrome()
driver.get("https://blockscout.com/poa/sokol")
html = driver.page_source
#print(html)
l = '"'
soup = BeautifulSoup(html, "lxml")
x = soup.find_all("div", attrs={"class": "dashboard-banner-chart-legend-value-container"})
x1 = str(x).split('data-usd-exchange-rate="')[1]
print(x1)
for i in x1:
    gl = gl + i
    if i == '"':
        break
mn = mn.replace('>\n', '')
mn = mn.replace(' ', '')
gl = gl.replace('>\n', '')
gl = gl.replace(' ', '')
ll = ll.replace('>\n', '')
ll = ll.replace(' ', '')
mk11 = mk11.replace('>\n', '')
mk11 = mk11.replace(' ', '')
mk12 = mk12.replace('>\n', '')
mk12 = mk12.replace(' ', '')
mk13 = mk13.replace('>\n', '')
mk13 = mk13.replace(' ', '')

print(ll)
ml.append(gl[0:-1]+'$')



@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIlM1-JTbzAGkdO8dpkkPtDGIUuXh3XAAIcAAMNJJs31LHbEkjpHdsbBA')
    bot.send_message(chat_id=message.chat.id, text='Select language/Выберите язык', reply_markup=keyboard22)


@bot.message_handler(content_types=['text'])
def send_text(message):
    user_id1 = message.from_user.id
    global userlist
    global ltest
    if message.text.lower() == 'change crypto':
        mbut1 = keyboard22 = telebot.types.ReplyKeyboardMarkup(True, True)
        mbut1.row('Sokol to Kovan')
        mbut1.row('Kovan to Sokol')
        bot.send_message(message.chat.id, 'What cryptocurrency do you want to change?(Since Kovan has no price, we will take the ratio 1 POA to 0.001 KETH)', reply_markup=mbut1)
    elif message.text.lower() == 'sokol to kovan':
        userlist.append(str(message.from_user.id))
        bot.send_message(chat_id=message.chat.id, text='Min to change:5 POA'+ "\n"
                                                            'Send on this Wallet ONLY: 0x2e0ff0e7805406b1e8c61F9F7cE2ba1d919C50dA.(fee $0,5) You have 60 sec to transfer tokens and send Transaction Hash')
    elif message.text.lower() == 'kovan to sokol':
        userlist.append(str(message.from_user.id)+'"')
        bot.send_message(chat_id=message.chat.id, text='Min to change:1 KETH'+ "\n"
                                                            'Send on this Wallet ONLY: 0x2e0ff0e7805406b1e8c61F9F7cE2ba1d919C50dA.(fee $0,5) You have 60 sec to transfer tokens and send Transaction Hash')
    elif message.text.lower() == 'sokol к kovan':
        userlist.append(str(message.from_user.id))
        bot.send_message(chat_id=message.chat.id, text='Минимум к обмену:5 POA'+ "\n"
                                                            'Отпровляйте токены только на ЭТОТ КОШЕЛЁК: 0x2e0ff0e7805406b1e8c61F9F7cE2ba1d919C50dA.(fee $0,5) У вас есть 60 секунд чтобы отправить токены. Также нужно отправить - Transaction Hash')
    elif message.text.lower() == 'kovan к sokol':
        userlist.append(str(message.from_user.id)+'"')
        bot.send_message(chat_id=message.chat.id, text='Минимум к обмену:1 KETH'+ "\n"
                                                            'Отпровляйте токены только на ЭТОТ КОШЕЛЁК: 0x2e0ff0e7805406b1e8c61F9F7cE2ba1d919C50dA.(fee $0,5) У вас есть 60 секунд чтобы отправить токены. Также нужно отправить - Transaction Hash')
    elif message.text.lower() == 'sell crypto':
        mbut2 = telebot.types.InlineKeyboardMarkup()
        but4 = telebot.types.InlineKeyboardButton(text='Sokol', callback_data='BTC1')
        mbut2.add(but4)
        but5 = telebot.types.InlineKeyboardButton(text='Kovan', callback_data='ETH1')
        mbut2.add(but5)
        bot.send_message(message.chat.id, 'What cryptocurrency do you want to sell?', reply_markup=mbut2)
    elif message.text.lower() == 'cryptocurrency rate':
        mbut3 = telebot.types.InlineKeyboardMarkup()
        but7 = telebot.types.InlineKeyboardButton(text='Sokol', callback_data='BTC2')
        mbut3.add(but7)
        but8 = telebot.types.InlineKeyboardButton(text='Kovan', callback_data='ETH2')
        mbut3.add(but8)
        bot.send_message(message.chat.id, 'What cryptocurrency price do you want to know?', reply_markup=mbut3)
    elif message.text.lower() == 'english 🇺🇸':
        ltest.append(str(message.from_user.id)+'eng')
        bot.send_message(message.chat.id, 'Hello! What do you want to do with your crypto? ❗️❗️❗️To make transactions use Nifty or Metamask Wallets❗️❗️❗️', reply_markup=keyboard1)
    elif message.text.lower() == 'русский 🇷🇺':
        ltest.append(str(message.from_user.id)+'rus')
        bot.send_message(message.chat.id, 'Привет! Что вы хотите сделать с криптой? ❗️❗️❗️Для проведения транзакций используйте Nifty и Metamask Кошельки❗️❗️❗️', reply_markup=keyboard5)
    elif message.text.lower() == 'обменять крипту':
        mbut4 = telebot.types.ReplyKeyboardMarkup(True, True)
        mbut4.row('Sokol к Kovan', 'Kovan к Sokol')
        bot.send_message(message.chat.id, 'Какую на какию крипту ты хочешь поменять? Так как Kovan не имеет цены мы будем брат соотношение 1POA to 0.001KETH', reply_markup=mbut4)
    elif message.text.lower() == 'продать крипту':
        mbut5 = telebot.types.InlineKeyboardMarkup()
        but13 = telebot.types.InlineKeyboardButton(text='Sokol', callback_data='BTC4')
        mbut5.add(but13)
        but14 = telebot.types.InlineKeyboardButton(text='Kovan', callback_data='ETH4')
        mbut5.add(but14)
        bot.send_message(message.chat.id, 'What cryptocurrency do you want to sell?', reply_markup=mbut5)
    elif message.text.lower() == 'курс криптовалют':
        mbut6 = telebot.types.InlineKeyboardMarkup()
        but16 = telebot.types.InlineKeyboardButton(text='Sokol', callback_data='BTC5')
        mbut6.add(but16)
        but17 = telebot.types.InlineKeyboardButton(text='Kovan', callback_data='ETH5')
        mbut6.add(but17)
        bot.send_message(message.chat.id, 'Курс какой криптовалюты ты хочешь узнать?', reply_markup=mbut6)
    elif len(message.text) == 66:
        try:
            ml = w31.eth.getTransaction(message.text)
            print(ml['value'])
            gl = float(ml['value'] * 0.001)
            tx = {
                      'to': ml['from'],
                      'value': int(str(gl)[0:-2]),
                      'gas': 21000,
                      'gasPrice': 1000000000,
                      'nonce': w3.eth.getTransactionCount(acct.address)}
            singed_tx = acct.signTransaction(tx)
            txhash = w3.eth.sendRawTransaction(singed_tx.rawTransaction)
            trades.append('status ' + str(txhash.hex()))
            sleep(1)
            if str(message.from_user.id)+'eng' in ltest:    
                bot.send_message(message.chat.id, 'Payment of '+str(ml['value'])+' POA to '+str(ml['from']) + ' scheduled')
                bot.send_message(message.chat.id, 'Transaction Hash: ' + txhash.hex(), reply_markup=keyboard1)
            elif str(message.from_user.id)+'rus' in ltest:
                bot.send_message(message.chat.id, 'Платёж '+str(ml['value'])+' POA к '+str(ml['from']) + ' проведён!')
                bot.send_message(message.chat.id, 'Transaction Hash: ' + txhash.hex(), reply_markup=keyboard1)
        except:
            ml = w3.eth.getTransaction(message.text)
            print(ml['value'])
            tx = {
                      'to': ml['from'],
                      'value': int(ml['value']) * 100,
                      'gas': 21000,
                      'gasPrice': 1000000000,
                      'nonce': w31.eth.getTransactionCount(acct.address)}
            singed_tx = acct.signTransaction(tx)
            txhash = w31.eth.sendRawTransaction(singed_tx.rawTransaction)
            trades.append('status ' + str(txhash.hex()))
            sleep(1)
            if str(message.from_user.id)+'eng' in ltest:    
                bot.send_message(message.chat.id, 'Payment of '+str(ml['value'])+' KETH to '+str(ml['from']) + 'scheduled')
                bot.send_message(message.chat.id, 'Transaction Hash: ' + txhash.hex(), reply_markup=keyboard1)
            elif str(message.from_user.id)+'rus' in ltest:
                bot.send_message(message.chat.id, 'Платёж '+str(ml['value'])+' KETH к '+str(ml['from']) + ' +проведён!')
                bot.send_message(message.chat.id, 'Transaction Hash: ' + txhash.hex(), reply_markup=keyboard1)
            
            
@bot.callback_query_handler(func=lambda call: True)
def callback_data(call):
    global userlist
    a = str(random.randint(1000, 983918))
    if call.data == 'BTC':
        bot.send_message(chat_id=call.message.chat.id, text='Min to change:5 POA'+ "\n"
                                                            'Send on this Wallet ONLY: 0x2e0ff0e7805406b1e8c61F9F7cE2ba1d919C50dA.(fee $0,5) You have 60 sec to transfer tokens and send Transaction Hash')
        userlist.append(str(call.from_user.id)+'"')
    elif call.data == 'ETH':
        bot.send_message(chat_id=call.message.chat.id, text='Min to change:5 KETH' + "\n"
                                                            'Send on this Wallet ONLY: 0x2e0ff0e7805406b1e8c61F9F7cE2ba1d919C50dA.(fee $0,5) You have 60 sec to transfer tokens and send Transaction Hash')
        userlist.append(str(call.from_user.id))
    elif call.data == 'BTC1':
        bot.send_message(chat_id=call.message.chat.id, text='Min to sell:5 POA.'+"\n"
                                                            'Send on this Wallet ONLY: 0x2e0ff0e7805406b1e8c61F9F7cE2ba1d919C50dA.(fee $1.5) You have 60 sec to transfer tokens and send Transaction Hash')
    elif call.data == 'ETH1':
        bot.send_message(chat_id=call.message.chat.id, text='Min to sell:5 KETH.'+"\n"
                                                            'Send on this Wallet ONLY: 0x2e0ff0e7805406b1e8c61F9F7cE2ba1d919C50dA.(fee $1.5) You have 60 sec to transfer tokens and send Transaction Hash')
    elif call.data == 'BTC2':
            bot.send_message(chat_id=call.message.chat.id,text='Sokol(POA) price: ' + ml[0])
    elif call.data == 'ETH2':
        bot.send_message(chat_id=call.message.chat.id, text='Kovan(KETH) price: 0.000$')
    elif call.data == 'BTC3':
        bot.send_message(chat_id=call.message.chat.id, text='Минимально к обмену:5 POA(Комиссия: $0,5) У тебя 60 секунд, чтобы перекинуть токены и скинуть Кэш Транзакции.')
    elif call.data == 'ETH3':
        bot.send_message(chat_id=call.message.chat.id, text='Минимально к обмену:5 KETH(Комиссия: $0,5) У тебя 60 секунд, чтобы перекинуть токены и скинуть Кэш Транзакции.')
    elif call.data == 'BTC4':
        bot.send_message(chat_id=call.message.chat.id, text='Минимально к продаже:5 POA.'+"\n"
                                                            'Присылать на этот кошелёк: 0x2e0ff0e7805406b1e8c61F9F7cE2ba1d919C50dA.(Комиссия: $0.5) У тебя 60 секунд, чтобы перекинуть токены и скинуть Кэш Транзакции.')
    elif call.data == 'ETH4':
        bot.send_message(chat_id=call.message.chat.id, text='Минимально к продаже:5 KETH.'+"\n"
                                                            'Присылать на этот кошелёк: 0x2e0ff0e7805406b1e8c61F9F7cE2ba1d919C50dA.(Комиссия: $0.5)У тебя 60 секунд, чтобы перекинуть токены и скинуть Кэш Транзакции.')
    elif call.data == 'BTC5':

        bot.send_message(chat_id=call.message.chat.id, text='Sokol(POA) цена: '+ml[0])

    elif call.data == 'ETH5':
        bot.send_message(chat_id=call.message.chat.id,text='Kovan(KETH) цена: 0.000$')

@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)


bot.polling(none_stop=True)