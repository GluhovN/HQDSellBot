import telebot
import pyqiwi
import requests
import pyqiwi
import requests
import random
import os


mylogin = '79274453001'
api_access_token = 'cf849e1adbb2640c0f04b44d5e1127da'
# История платежей - последние и следующие n платежей
def payment_history_last(my_login, api_access_token, rows_num, next_TxnId, next_TxnDate):
    s = requests.Session()
    s.headers['authorization'] = 'Bearer ' + api_access_token
    parameters = {'rows': rows_num, 'nextTxnId': next_TxnId, 'nextTxnDate': next_TxnDate}
    h = s.get('https://edge.qiwi.com/payment-history/v2/persons/' + my_login + '/payments', params = parameters)
    return h.json()
lastPayments = payment_history_last(mylogin, api_access_token, '5','','')

# дата и время следующего платежа
nextTxnDate = lastPayments['nextTxnDate']

# id транзакции следующего платежа
nextTxnId = lastPayments['nextTxnId']

# История платежей - последние и следующие n платежей
orderedPayments = payment_history_last(mylogin, api_access_token, '5', nextTxnId, nextTxnDate)


global list_of_addresses
list_of_addresses = []
global addresses
addresses = []
global list_of_users
list_of_users = []


API_TOKEN = '1699438362:AAG_Umw0uAnFaXmSPoSq9ZNGolPnteMicmM'

bot = telebot.TeleBot(API_TOKEN)


HQD_name = telebot.types.InlineKeyboardMarkup()
hqd1 = telebot.types.InlineKeyboardButton(text='PUFF', callback_data='hqd1')
hqd2 = telebot.types.InlineKeyboardButton(text='ELF BAR', callback_data='hqd2')
hqd3 = telebot.types.InlineKeyboardButton(text='JUUL', callback_data='hqd3')
hqd5 = telebot.types.InlineKeyboardButton(text='HQD', callback_data='hqd5')
HQD_name.add(hqd1)
HQD_name.add(hqd2)
HQD_name.add(hqd3)
HQD_name.add(hqd5)

pay_cut = telebot.types.InlineKeyboardMarkup()
pay = telebot.types.InlineKeyboardButton(url='https://oplata.qiwi.com/form?invoiceUid=a7edb1d2-8227-49b8-8444-f64f8715a1ea', text='Оплатить', callback_data='pay')
check_status = telebot.types.InlineKeyboardButton(text='Проверить статус', callback_data='check')
pay_cut.add(pay)
pay_cut.add(check_status)

pay_cut_for_curva_plus = telebot.types.InlineKeyboardMarkup()
pay = telebot.types.InlineKeyboardButton(url='https://oplata.qiwi.com/form?invoiceUid=6b33bf5c-df68-4327-8b56-01b1b8b4659e', text='Оплатить', callback_data='pay')
check_status = telebot.types.InlineKeyboardButton(text='Проверить статус', callback_data='check')
pay_cut_for_curva_plus.add(pay)
pay_cut_for_curva_plus.add(check_status)

pay_cut_for_maxim = telebot.types.InlineKeyboardMarkup()
pay = telebot.types.InlineKeyboardButton(url='https://oplata.qiwi.com/form?invoiceUid=ab584fa6-e2b5-4ba4-a89c-6a9f40b4cfc5', text='Оплатить', callback_data='pay')
check_status = telebot.types.InlineKeyboardButton(text='Проверить статус', callback_data='check')
pay_cut_for_maxim.add(pay)
pay_cut_for_maxim.add(check_status)

pay_cut_for_mega = telebot.types.InlineKeyboardMarkup()
pay = telebot.types.InlineKeyboardButton(url='https://oplata.qiwi.com/form?invoiceUid=995541f6-f175-46ff-b0f3-21691c4d62ca', text='Оплатить', callback_data='pay')
check_status = telebot.types.InlineKeyboardButton(text='Проверить статус', callback_data='check')
pay_cut_for_mega.add(pay)
pay_cut_for_mega.add(check_status)

pay_cut_for_rosy = telebot.types.InlineKeyboardMarkup()
pay = telebot.types.InlineKeyboardButton(url='https://oplata.qiwi.com/form?invoiceUid=17d7bdf1-ff28-4285-bc08-8f4ae168fda2', text='Оплатить', callback_data='pay')
check_status = telebot.types.InlineKeyboardButton(text='Проверить статус', callback_data='check')
pay_cut_for_rosy.add(pay)
pay_cut_for_rosy.add(check_status)

pay_cut_for_stark = telebot.types.InlineKeyboardMarkup()
pay = telebot.types.InlineKeyboardButton(url='https://oplata.qiwi.com/form?invoiceUid=94a52965-598d-44dd-8171-508112f627fd', text='Оплатить', callback_data='pay')
check_status = telebot.types.InlineKeyboardButton(text='Проверить статус', callback_data='check')
pay_cut_for_stark.add(pay)
pay_cut_for_stark.add(check_status)

pay_cut_for_super = telebot.types.InlineKeyboardMarkup()
pay = telebot.types.InlineKeyboardButton(url='https://oplata.qiwi.com/form?invoiceUid=4e76d2f5-6626-4dd9-beb4-9e23187170e7', text='Оплатить', callback_data='pay')
check_status = telebot.types.InlineKeyboardButton(text='Проверить статус', callback_data='check')
pay_cut_for_super.add(pay)
pay_cut_for_super.add(check_status)

pay_cut_for_ultrastick = telebot.types.InlineKeyboardMarkup()
pay = telebot.types.InlineKeyboardButton(url='https://oplata.qiwi.com/form?invoiceUid=ff07f45f-7285-42e2-b401-8d0e6f41fec5', text='Оплатить', callback_data='pay')
check_status = telebot.types.InlineKeyboardButton(text='Проверить статус', callback_data='check')
pay_cut_for_ultrastick.add(pay)
pay_cut_for_ultrastick.add(check_status)

pay_cut_for_juul = telebot.types.InlineKeyboardMarkup()
pay = telebot.types.InlineKeyboardButton(url='https://oplata.qiwi.com/form?invoiceUid=97348784-0b18-48ea-a155-38d9e19f087a', text='Оплатить', callback_data='pay')
check_status = telebot.types.InlineKeyboardButton(text='Проверить статус', callback_data='check')
pay_cut_for_juul.add(pay)
pay_cut_for_juul.add(check_status)

pay_cut_for_puff = telebot.types.InlineKeyboardMarkup()
pay = telebot.types.InlineKeyboardButton(url='https://oplata.qiwi.com/form?invoiceUid=2696b13c-389e-492e-ac92-971f21f12f65', text='Оплатить', callback_data='pay')
check_status = telebot.types.InlineKeyboardButton(text='Проверить статус', callback_data='check')
pay_cut_for_puff.add(pay)
pay_cut_for_puff.add(check_status)

pay_cut_for_puff_pls = telebot.types.InlineKeyboardMarkup()
pay = telebot.types.InlineKeyboardButton(url='https://oplata.qiwi.com/form?invoiceUid=8875ae86-bbd8-46ec-9790-0a12aec6b8f2', text='Оплатить', callback_data='pay')
check_status = telebot.types.InlineKeyboardButton(text='Проверить статус', callback_data='check')
pay_cut_for_puff_pls.add(pay)
pay_cut_for_puff_pls.add(check_status)

pay_cut_for_juul_5 = telebot.types.InlineKeyboardMarkup()
pay = telebot.types.InlineKeyboardButton(url='https://oplata.qiwi.com/form?invoiceUid=c2d08f1f-e596-486f-871a-6d007bae20ab', text='Оплатить', callback_data='pay')
check_status = telebot.types.InlineKeyboardButton(text='Проверить статус', callback_data='check')
pay_cut_for_juul_5.add(pay)
pay_cut_for_juul_5.add(check_status)

pay_cut_for_juul_apex = telebot.types.InlineKeyboardMarkup()
pay = telebot.types.InlineKeyboardButton(url='https://oplata.qiwi.com/form?invoiceUid=98305125-46ab-420d-be7b-f46d3a225733', text='Оплатить', callback_data='pay')
check_status = telebot.types.InlineKeyboardButton(text='Проверить статус', callback_data='check')
pay_cut_for_juul_apex.add(pay)
pay_cut_for_juul_apex.add(check_status)

pay_cut_for_elf_bar = telebot.types.InlineKeyboardMarkup()
pay = telebot.types.InlineKeyboardButton(url='https://oplata.qiwi.com/form?invoiceUid=f714ae0e-92f2-4743-abad-3cd19d687605', text='Оплатить', callback_data='pay')
check_status = telebot.types.InlineKeyboardButton(text='Проверить статус', callback_data='check')
pay_cut_for_elf_bar.add(pay)
pay_cut_for_elf_bar.add(check_status)

geo = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
button_geo = telebot.types.KeyboardButton(text="🗺 Отправить геопозицию", request_location=True)
button_ne_geo = telebot.types.KeyboardButton(text="🖊 Ввести вручную")
geo.add(button_geo)
geo.add(button_ne_geo)

back_button = telebot.types.InlineKeyboardButton(text='Назад', callback_data='back')

settings = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
button_SET = telebot.types.KeyboardButton(text="⚙️ПОМЕНЯТЬ АДРЕС", request_location=True)
settings.add(button_SET)

types_of_hqd = telebot.types.InlineKeyboardMarkup()
Cuvie = telebot.types.InlineKeyboardButton(text='Cuvie', callback_data='cuvie')
Cuvie_plus = telebot.types.InlineKeyboardButton(text='Cuvie Plus', callback_data='cuvie_pl')
Maxim = telebot.types.InlineKeyboardButton(text='Maxim', callback_data='maxim')
Mega = telebot.types.InlineKeyboardButton(text='Mega', callback_data='mega')
ROSY = telebot.types.InlineKeyboardButton(text='ROSY', callback_data='rosy')
Stark = telebot.types.InlineKeyboardButton(text='Stark', callback_data='startk')
Super = telebot.types.InlineKeyboardButton(text='Super', callback_data='super')
Ultrastick = telebot.types.InlineKeyboardButton(text='Ultrastick', callback_data='ultradick')
types_of_hqd.add(Cuvie, Cuvie_plus, Maxim)
types_of_hqd.add(Mega, ROSY, Stark)
types_of_hqd.add(Super, Ultrastick)
types_of_hqd.add(back_button)

types_of_juul = telebot.types.InlineKeyboardMarkup()
device = telebot.types.InlineKeyboardButton(text='Device', callback_data='device')
pods = telebot.types.InlineKeyboardButton(text='Juul Pods', callback_data='jull_pods')
types_of_juul.add(pods,device)
types_of_juul.add(back_button)

types_of_puffs = telebot.types.InlineKeyboardMarkup()
puff_class = telebot.types.InlineKeyboardButton(text='Puff bar', callback_data='puff_class')
puff_plus = telebot.types.InlineKeyboardButton(text='Puff plus', callback_data='puff_plus')
types_of_puffs.add(puff_class, puff_plus)
types_of_puffs.add(back_button)

#jull == device == 990 rub
juul_pods_typs = telebot.types.InlineKeyboardMarkup()
apex_pod = telebot.types.InlineKeyboardButton(text='Apex Pods', callback_data='apex')
pod_5 = telebot.types.InlineKeyboardButton(text='Jull Pods', callback_data='pods-5')
juul_pods_typs.add(apex_pod, pod_5)
juul_pods_typs.add(back_button)

tastes_for_elf = telebot.types.InlineKeyboardMarkup()
taste1 = telebot.types.InlineKeyboardButton(text='ВИНОГРАД🍇', callback_data='taste1')
taste2 = telebot.types.InlineKeyboardButton(text='МАНГО🥭', callback_data='taste2')
taste3 = telebot.types.InlineKeyboardButton(text='ЧЕРНИКА \u1FAD0 ', callback_data='taste3')
taste4 = telebot.types.InlineKeyboardButton(text='ЛЕДЯНАЯ МЯТА🧊', callback_data='taste4')
taste5 = telebot.types.InlineKeyboardButton(text='ЛЕДЯНОЙ БАНАН🧊', callback_data='taste5')
taste6 = telebot.types.InlineKeyboardButton(text='ЛЕДЯНАЯ КЛУБНИКА🧊', callback_data='taste6')
tastes_for_elf.add(taste1, taste2)
tastes_for_elf.add(taste3, taste4)
tastes_for_elf.add(taste5, taste6)
tastes_for_elf.add(back_button)



tastes_for_puff_bar = telebot.types.InlineKeyboardMarkup()
taste_puff1 = telebot.types.InlineKeyboardButton(text='Ананас 🍍', callback_data='taste_puff1')
taste_puff2 = telebot.types.InlineKeyboardButton(text='Виноград 🍇', callback_data='taste_puff2')
taste_puff3 = telebot.types.InlineKeyboardButton(text='Ледяная дыня 🧊', callback_data='taste_puff3')
taste_puff4 = telebot.types.InlineKeyboardButton(text='Вкус с секретом 🍈', callback_data='taste_puff4')
taste_puff5 = telebot.types.InlineKeyboardButton(text='Клубника 🍓', callback_data='taste_puff5')
taste_puff6 = telebot.types.InlineKeyboardButton(text='Мята с холодком 🍃', callback_data='taste_puff6')
taste_puff7 = telebot.types.InlineKeyboardButton(text='Малиновый мармелад 🧊', callback_data='taste_puff7')
tastes_for_puff_bar.add(taste_puff1, taste_puff2, taste_puff3)
tastes_for_puff_bar.add(taste_puff4, taste_puff5, taste_puff6)
tastes_for_puff_bar.add(taste_puff7)
tastes_for_puff_bar.add(back_button)

tastes_for_puff_plus = telebot.types.InlineKeyboardMarkup()
taste_puff1 = telebot.types.InlineKeyboardButton(text='Алоэ-Виноград 🍇', callback_data='taste_puff_1')
taste_puff2 = telebot.types.InlineKeyboardButton(text='Арбуз-Киви-Фрукты 🍉 ', callback_data='taste_puff_2')
taste_puff3 = telebot.types.InlineKeyboardButton(text='Арбуз-лимон со льдом 🧊', callback_data='taste_puff_3')
taste_puff4 = telebot.types.InlineKeyboardButton(text='Банан со льдом 🧊', callback_data='taste_puff4_')
taste_puff5 = telebot.types.InlineKeyboardButton(text='Банановое мороженное 🍌', callback_data='taste_puff5_')
taste_puff6 = telebot.types.InlineKeyboardButton(text='Виноград 🍇', callback_data='taste_puff6_')
taste_puff7 = telebot.types.InlineKeyboardButton(text='Гранат', callback_data='taste_puff7_')
taste_puff8 = telebot.types.InlineKeyboardButton(text='Драгонфрут-Клубника 🍓', callback_data='taste_puff8_')
taste_puff9 = telebot.types.InlineKeyboardButton(text='Ледяная дыня 🧊', callback_data='taste_puff9_')
taste_puff10 = telebot.types.InlineKeyboardButton(text='Клубника-банан 🍹', callback_data='taste_puff10_')
taste_puff11 = telebot.types.InlineKeyboardButton(text='Космополитан 🍸', callback_data='taste_puff11_')
taste_puff12 = telebot.types.InlineKeyboardButton(text='Лимонад из синей малины 🍾', callback_data='taste_puff12_')
taste_puff13 = telebot.types.InlineKeyboardButton(text='Личи со льдом 🧊', callback_data='taste_puff13_')
taste_puff14 = telebot.types.InlineKeyboardButton(text='Лонг Айленд 🥂', callback_data='taste_puff14_')
taste_puff15 = telebot.types.InlineKeyboardButton(text='Май Тай 🧉', callback_data='taste_puff15_')
taste_puff16 = telebot.types.InlineKeyboardButton(text='Манго 🥭', callback_data='taste_puff16_')
taste_puff17 = telebot.types.InlineKeyboardButton(text='Манго-Ананас 🍍', callback_data='taste_puff17_')
taste_puff18 = telebot.types.InlineKeyboardButton(text='Персик со льдом 🧊', callback_data='taste_puff18_')
taste_puff19 = telebot.types.InlineKeyboardButton(text='Пина Колада 🍾', callback_data='taste_puff19_')
taste_puff20 = telebot.types.InlineKeyboardButton(text='Яблоко-ягоды 🍎', callback_data='taste_puff20_')
taste_puff21 = telebot.types.InlineKeyboardButton(text='Ягодный Микс 🍒', callback_data='taste_puff21_')
tastes_for_puff_plus.add(taste_puff1)
tastes_for_puff_plus.add(taste_puff2, taste_puff3)
tastes_for_puff_plus.add(taste_puff4, taste_puff5)
tastes_for_puff_plus.add(taste_puff6, taste_puff7)
tastes_for_puff_plus.add(taste_puff8, taste_puff9)
tastes_for_puff_plus.add(taste_puff10, taste_puff11)
tastes_for_puff_plus.add(taste_puff12, taste_puff13)
tastes_for_puff_plus.add(taste_puff14, taste_puff15)
tastes_for_puff_plus.add(taste_puff16, taste_puff17)
tastes_for_puff_plus.add(taste_puff18, taste_puff19)
tastes_for_puff_plus.add(taste_puff20, taste_puff21)
tastes_for_puff_plus.add(back_button)


tastes_for_juul = telebot.types.InlineKeyboardMarkup()
taste_jull1 = telebot.types.InlineKeyboardButton(text='МЕНТОЛ', callback_data='taste_jull1')
taste_jull2 = telebot.types.InlineKeyboardButton(text='ОГУРЕЦ', callback_data='taste_jull2')
taste_jull3 = telebot.types.InlineKeyboardButton(text='ТАБАК', callback_data='taste_jull3')
taste_jull4 = telebot.types.InlineKeyboardButton(text='МАНГО', callback_data='taste_jull4')

tastes_for_juul.add(taste_jull1, taste_jull2)
tastes_for_juul.add(taste_jull4, taste_jull3)
tastes_for_juul.add(back_button)

tastes_for_juul_apex = telebot.types.InlineKeyboardMarkup()
taste_jull_1 = telebot.types.InlineKeyboardButton(text='МЕНТОЛ', callback_data='taste_jull_1')
taste_jull_2 = telebot.types.InlineKeyboardButton(text='ОГУРЕЦ', callback_data='taste_jull_2')
taste_jull_3 = telebot.types.InlineKeyboardButton(text='ТАБАК', callback_data='taste_jull_3')
taste_jull_4 = telebot.types.InlineKeyboardButton(text='МАНГО', callback_data='taste_jull_4')
tastes_for_juul_apex.add(taste_jull_1, taste_jull_2)
tastes_for_juul_apex.add(taste_jull_4, taste_jull_3)
tastes_for_juul_apex.add(back_button)

culve__tastes = telebot.types.InlineKeyboardMarkup()
taste__culve1 = telebot.types.InlineKeyboardButton(text='АНАНАС 🍍', callback_data='taste__culve1')
taste__culve2 = telebot.types.InlineKeyboardButton(text='АПЕЛЬСИН 🍊', callback_data='taste__culve2')
taste__culve3 = telebot.types.InlineKeyboardButton(text='АРБУЗ 🍉', callback_data='taste__culve3')
taste__culve4 = telebot.types.InlineKeyboardButton(text='БАНАН 🍌', callback_data='taste__culve4')
taste__culve5 = telebot.types.InlineKeyboardButton(text='ВИНОГРАД 🍇', callback_data='taste__culve5')
taste__culve6 = telebot.types.InlineKeyboardButton(text='ГУАВА-АПЕЛЬСИН ', callback_data='taste__culve6')
taste__culve7 = telebot.types.InlineKeyboardButton(text='ДЫНЯ', callback_data='taste__culve7')
taste__culve8 = telebot.types.InlineKeyboardButton(text='ЖВАЧКА', callback_data='taste__culve8')
taste__culve9 = telebot.types.InlineKeyboardButton(text='КЛУБНИКА 🍓', callback_data='taste__culve9')
taste__culve10 = telebot.types.InlineKeyboardButton(text='КОЛА 🥤', callback_data='taste__culve10')
taste__culve11 = telebot.types.InlineKeyboardButton(text='ЛИЧИ 🍓', callback_data='taste__culve11')
taste__culve12 = telebot.types.InlineKeyboardButton(text='МЯТА', callback_data='taste__culve12')
taste__culve13 = telebot.types.InlineKeyboardButton(text='МУЛЬТФРУКТ 🍑', callback_data='taste__culve3')
taste__culve14 = telebot.types.InlineKeyboardButton(text='РОЗОВЫЙ ЛИМОНАД', callback_data='taste__culve14')
taste__culve15 = telebot.types.InlineKeyboardButton(text='ЧЕРНИКА', callback_data='taste__culve15')
taste__culve16 = telebot.types.InlineKeyboardButton(text='ШОРИА', callback_data='taste__culve16')
taste__culve17 = telebot.types.InlineKeyboardButton(text='ЭНЕРГЕТИК 🥤', callback_data='taste__culve17')
taste__culve18 = telebot.types.InlineKeyboardButton(text='ЯБЛОКО 🍎', callback_data='taste__culve18')
culve__tastes.add(taste__culve1, taste__culve2)
culve__tastes.add(taste__culve3, taste__culve4)
culve__tastes.add(taste__culve5, taste__culve6)
culve__tastes.add(taste__culve7, taste__culve8)
culve__tastes.add(taste__culve9, taste__culve10)
culve__tastes.add(taste__culve11, taste__culve12)
culve__tastes.add(taste__culve13, taste__culve14)
culve__tastes.add(taste__culve15, taste__culve16)
culve__tastes.add(taste__culve17, taste__culve18)
culve__tastes.add(back_button)

culve_tastes = telebot.types.InlineKeyboardMarkup()
taste_culve1 = telebot.types.InlineKeyboardButton(text='АНАНАС 🍍', callback_data='taste_culve1')
taste_culve2 = telebot.types.InlineKeyboardButton(text='АПЕЛЬСИН 🍊', callback_data='taste_culve2')
taste_culve3 = telebot.types.InlineKeyboardButton(text='АРБУЗ 🍉', callback_data='taste_culve3')
taste_culve4 = telebot.types.InlineKeyboardButton(text='БАНАН 🍌', callback_data='taste_culve4')
taste_culve5 = telebot.types.InlineKeyboardButton(text='ВИНОГРАД 🍇', callback_data='taste_culve5')
taste_culve6 = telebot.types.InlineKeyboardButton(text='ГУАВА-АПЕЛЬСИН ', callback_data='taste_culve6')
taste_culve7 = telebot.types.InlineKeyboardButton(text='ДЫНЯ', callback_data='taste_culve7')
taste_culve8 = telebot.types.InlineKeyboardButton(text='ЖВАЧКА', callback_data='taste_culve8')
taste_culve9 = telebot.types.InlineKeyboardButton(text='КЛУБНИКА 🍓', callback_data='taste_culve9')
taste_culve10 = telebot.types.InlineKeyboardButton(text='КОЛА 🥤', callback_data='taste_culve10')
taste_culve11 = telebot.types.InlineKeyboardButton(text='ЛИЧИ 🍓', callback_data='taste_culve11')
taste_culve12 = telebot.types.InlineKeyboardButton(text='МЯТА', callback_data='taste_culve12')
taste_culve13 = telebot.types.InlineKeyboardButton(text='МУЛЬТФРУКТ 🍑', callback_data='taste_culve3')
taste_culve14 = telebot.types.InlineKeyboardButton(text='РОЗОВЫЙ ЛИМОНАД', callback_data='taste_culve14')
taste_culve15 = telebot.types.InlineKeyboardButton(text='ЧЕРНИКА', callback_data='taste_culve15')
taste_culve16 = telebot.types.InlineKeyboardButton(text='ШОРИА', callback_data='taste_culve16')
taste_culve17 = telebot.types.InlineKeyboardButton(text='ЭНЕРГЕТИК 🥤', callback_data='taste_culve17')
taste_culve18 = telebot.types.InlineKeyboardButton(text='ЯБЛОКО 🍎', callback_data='taste_culve18')
culve_tastes.add(taste_culve1, taste_culve2)
culve_tastes.add(taste_culve3, taste_culve4)
culve_tastes.add(taste_culve5, taste_culve6)
culve_tastes.add(taste_culve7, taste_culve8)
culve_tastes.add(taste_culve9, taste_culve10)
culve_tastes.add(taste_culve11, taste_culve12)
culve_tastes.add(taste_culve13, taste_culve14)
culve_tastes.add(taste_culve15, taste_culve16)
culve_tastes.add(taste_culve17, taste_culve18)
culve_tastes.add(back_button)

maxim_tastes = telebot.types.InlineKeyboardMarkup()
maxim_tastes1 = telebot.types.InlineKeyboardButton(text='АПЕЛЬСИН', callback_data='taste_maxim1')
maxim_tastes2 = telebot.types.InlineKeyboardButton(text='БАНАН', callback_data='taste_maxim2')
maxim_tastes3 = telebot.types.InlineKeyboardButton(text='ВИНОГРАД', callback_data='taste_maxim3')
maxim_tastes4 = telebot.types.InlineKeyboardButton(text='ДЫНЯ', callback_data='taste_maxim4')
maxim_tastes5 = telebot.types.InlineKeyboardButton(text='КЛУБНИКА', callback_data='taste_maxim5')
maxim_tastes6 = telebot.types.InlineKeyboardButton(text='КОЛА', callback_data='taste_maxim6')
maxim_tastes7 = telebot.types.InlineKeyboardButton(text='КОРИЦА', callback_data='taste_maxim7')
maxim_tastes8 = telebot.types.InlineKeyboardButton(text='ЛИМОННЫЙ ПИРОГ', callback_data='taste_maxim8')
maxim_tastes9 = telebot.types.InlineKeyboardButton(text='МАНГО', callback_data='taste_maxim9')
maxim_tastes10 = telebot.types.InlineKeyboardButton(text='МУЛЬТИФРУКТ', callback_data='taste_maxim10')
maxim_tastes11 = telebot.types.InlineKeyboardButton(text='МЯТА', callback_data='taste_maxim11')
maxim_tastes12 = telebot.types.InlineKeyboardButton(text='ЧЕРНИКА', callback_data='taste_maxim12')
maxim_tastes.add(maxim_tastes1, maxim_tastes2)
maxim_tastes.add(maxim_tastes3, maxim_tastes4)
maxim_tastes.add(maxim_tastes5, maxim_tastes6)
maxim_tastes.add(maxim_tastes7, maxim_tastes8)
maxim_tastes.add(maxim_tastes9, maxim_tastes10)
maxim_tastes.add(maxim_tastes11, maxim_tastes12)
maxim_tastes.add(back_button)

mega_tastes = telebot.types.InlineKeyboardMarkup()
mega_taste1 = telebot.types.InlineKeyboardButton(text='АНАНАС', callback_data='taste_mega1')
mega_taste2 = telebot.types.InlineKeyboardButton(text='АРБУЗ', callback_data='taste_mega2')
mega_taste3 = telebot.types.InlineKeyboardButton(text='КЛУБНИЧНЫЙ ПОНЧИК', callback_data='taste_mega3')
mega_taste4 = telebot.types.InlineKeyboardButton(text='КОНФЕТНОЕ БЕЗУМИЕ', callback_data='taste_mega4')
mega_taste5 = telebot.types.InlineKeyboardButton(text='ЛЕСНЫЕ ЯГОДЫ', callback_data='taste_mega5')
mega_taste6 = telebot.types.InlineKeyboardButton(text='МАНГО-ДЫНЯ', callback_data='taste_mega6')
mega_taste7 = telebot.types.InlineKeyboardButton(text='ПИНА КОЛАДА', callback_data='taste_mega7')
mega_taste8 = telebot.types.InlineKeyboardButton(text='СОЧНЫЙ ВИНОГРАД', callback_data='taste_mega8')
mega_tastes.add(mega_taste1, mega_taste2)
mega_tastes.add(mega_taste3, mega_taste4)
mega_tastes.add(mega_taste5, mega_taste6)
mega_tastes.add(mega_taste7, mega_taste8)
mega_tastes.add(back_button)

rosy_tastes = telebot.types.InlineKeyboardMarkup()
rosy_taste1 = telebot.types.InlineKeyboardButton(text='АНАНАС', callback_data='taste_rosy1')
rosy_taste2 = telebot.types.InlineKeyboardButton(text='ВИНОГРАД', callback_data='taste_rosy2')
rosy_taste3 = telebot.types.InlineKeyboardButton(text='ГРЕЙПФРУТ', callback_data='taste_rosy3')
rosy_taste4 = telebot.types.InlineKeyboardButton(text='ГУАВА', callback_data='taste_rosy4')
rosy_taste5 = telebot.types.InlineKeyboardButton(text='ДЫНЯ', callback_data='taste_rosy5')
rosy_taste6 = telebot.types.InlineKeyboardButton(text='ЕЖЕВИКА', callback_data='taste_rosy6')
rosy_taste7 = telebot.types.InlineKeyboardButton(text='КИВИ-ГРАНАТ', callback_data='taste_rosy7')
rosy_taste8 = telebot.types.InlineKeyboardButton(text='КОЛА', callback_data='taste_rosy8')
rosy_taste9 = telebot.types.InlineKeyboardButton(text='ЛИЧИ', callback_data='taste_rosy9')
rosy_taste10 = telebot.types.InlineKeyboardButton(text='МАНГО-МАРАКУЙЯ', callback_data='taste_rosy10')
rosy_taste11 = telebot.types.InlineKeyboardButton(text='МАНГО', callback_data='taste_rosy11')
rosy_taste12 = telebot.types.InlineKeyboardButton(text='МЯТА', callback_data='taste_rosy12')
rosy_taste13 = telebot.types.InlineKeyboardButton(text='МОХИТО', callback_data='taste_rosy13')
rosy_taste14 = telebot.types.InlineKeyboardButton(text='ОГНИ МАЙАМИ', callback_data='taste_rosy14')
rosy_taste15 = telebot.types.InlineKeyboardButton(text='ПЕРСИК', callback_data='taste_rosy15')
rosy_taste16 = telebot.types.InlineKeyboardButton(text='РОЗОВЫЙ ЛИМОНАД', callback_data='taste_rosy16')
rosy_taste17 = telebot.types.InlineKeyboardButton(text='ЧЕРНИКА', callback_data='taste_rosy17')
rosy_taste18 = telebot.types.InlineKeyboardButton(text='ЯБЛОКО', callback_data='taste_rosy18')
rosy_tastes.add(rosy_taste1, rosy_taste2)
rosy_tastes.add(rosy_taste3, rosy_taste4)
rosy_tastes.add(rosy_taste5, rosy_taste6)
rosy_tastes.add(rosy_taste7, rosy_taste8)
rosy_tastes.add(rosy_taste9, rosy_taste10)
rosy_tastes.add(rosy_taste11, rosy_taste12)
rosy_tastes.add(rosy_taste13, rosy_taste14)
rosy_tastes.add(rosy_taste15, rosy_taste16)
rosy_tastes.add(rosy_taste17, rosy_taste18)
rosy_tastes.add(back_button)

stark_tastes = telebot.types.InlineKeyboardMarkup()
stark_taste1 = telebot.types.InlineKeyboardButton(text='ВИШНЯ', callback_data='taste_stark1')
stark_taste2 = telebot.types.InlineKeyboardButton(text='КОРИЦА', callback_data='taste_stark2')
stark_tastes.add(stark_taste1, stark_taste2)
stark_tastes.add(back_button)

super_tastes = telebot.types.InlineKeyboardMarkup()
super_taste1 = telebot.types.InlineKeyboardButton(text='АПЕЛЬСИН', callback_data='taste_super1')
super_taste2 = telebot.types.InlineKeyboardButton(text='ВИНОГРАД', callback_data='taste_super2')
super_taste3 = telebot.types.InlineKeyboardButton(text='ДЫНЯ', callback_data='taste_super3')
super_taste4 = telebot.types.InlineKeyboardButton(text='КЛУБНИКА-БАНАН', callback_data='taste_super4')
super_taste5 = telebot.types.InlineKeyboardButton(text='КЛУБНИКА-АРБУЗ', callback_data='taste_super5')
super_taste6 = telebot.types.InlineKeyboardButton(text='ЛИЧИ', callback_data='taste_super6')
super_taste7 = telebot.types.InlineKeyboardButton(text='МАНГО-ЛИЧИ', callback_data='taste_super7')
super_taste8 = telebot.types.InlineKeyboardButton(text='МУЛЬТИФРУКТ', callback_data='taste_super8')
super_taste9 = telebot.types.InlineKeyboardButton(text='МЯТА', callback_data='taste_super9')
super_taste10 = telebot.types.InlineKeyboardButton(text='ЧЕРНИКА', callback_data='taste_super10')
super_tastes.add(super_taste1, super_taste2)
super_tastes.add(super_taste3, super_taste4)
super_tastes.add(super_taste5, super_taste6)
super_tastes.add(super_taste7, super_taste8)
super_tastes.add(super_taste9, super_taste10)
super_tastes.add(back_button)

Ultrastick_tastes = telebot.types.InlineKeyboardMarkup()
Ultrastick_taste1 = telebot.types.InlineKeyboardButton(text='АНАНАС', callback_data='taste_ultra1')
Ultrastick_taste2 = telebot.types.InlineKeyboardButton(text='АРБУЗ', callback_data='taste_ultra2')
Ultrastick_taste3 = telebot.types.InlineKeyboardButton(text='ДЫНЯ', callback_data='taste_ultra3')
Ultrastick_taste4 = telebot.types.InlineKeyboardButton(text='ЖВАЧКА', callback_data='taste_ultra4')
Ultrastick_taste5 = telebot.types.InlineKeyboardButton(text='КЛУБНИКА', callback_data='taste_ultra5')
Ultrastick_taste6 = telebot.types.InlineKeyboardButton(text='КОЛА', callback_data='taste_ultra6')
Ultrastick_taste7 = telebot.types.InlineKeyboardButton(text='КОРИЦА', callback_data='taste_ultra7')
Ultrastick_taste8 = telebot.types.InlineKeyboardButton(text='МАНГО', callback_data='taste_ultra8')
Ultrastick_taste9 = telebot.types.InlineKeyboardButton(text='МЯТА', callback_data='taste_ultra9')
Ultrastick_taste10 = telebot.types.InlineKeyboardButton(text='ПЕРСИК', callback_data='taste_ultra10')
Ultrastick_taste11 = telebot.types.InlineKeyboardButton(text='РОЗОВЫЙ ЛИМОНАД', callback_data='taste_ultra11')
Ultrastick_taste12 = telebot.types.InlineKeyboardButton(text='ЯБЛОКО', callback_data='taste_ultra12')
Ultrastick_tastes.add(Ultrastick_taste1, Ultrastick_taste2)
Ultrastick_tastes.add(Ultrastick_taste3, Ultrastick_taste4)
Ultrastick_tastes.add(Ultrastick_taste5, Ultrastick_taste6)
Ultrastick_tastes.add(Ultrastick_taste7, Ultrastick_taste8)
Ultrastick_tastes.add(Ultrastick_taste9, Ultrastick_taste10)
Ultrastick_tastes.add(Ultrastick_taste11, Ultrastick_taste12)
Ultrastick_tastes.add(back_button)

Classic_keys = telebot.types.ReplyKeyboardMarkup(True, True)
Classic_keys.row('💨Купить одноразки💨')


print('a')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    print('a')
    bot.send_message(chat_id=message.chat.id, text='Добро пожаловать! После оформления заказа с вами свяжется менеджер. \nВведите адрес доставки', reply_markup=geo)
    list_of_users.append(message.chat.id)

@bot.message_handler(commands=['help'])
def help_butt(message):
    bot.send_message(chat_id=message.chat.id, text='Список команд: \n/catalog - Каталог'
                                                   '\n/history — История заказов \n/news — Наши новости и акции '
                                                   '\n/help — Справка '
                                                   '\n/about — О проекте \n/start — Главное меню '
                                                   '\n/off — Выключить подписку на бота '
                                                   '\n/on — Включить подписку на бота', reply_markup=Classic_keys)

@bot.message_handler(content_types=['text'])
def echo_message(message):
    if message.text.lower() == 'иди нахуй':
        bot.send_message(message.chat.id, text='Иди нахуй')
    elif message.text.lower() == '💨купить одноразки💨':
        bot.send_message(message.chat.id, text='Выберете одноразку:', reply_markup=HQD_name)
    elif 'ввести вручную' in message.text.lower():
        bot.send_message(message.chat.id, text='Введите адрес досавки(включая город)')
        list_of_addresses.append(message.chat.id)
    elif 'доставки' in message.text.lower():
        bot.send_message(message.chat.id, text='Введите адрес доставки', reply_markup=geo)
    else:
        for address in list_of_addresses:
            if address == message.chat.id:
                addresses.append(str(message.text))
                list_of_addresses.remove(address)
                bot.send_message(message.chat.id, text='Принято! Чтобы изменить адрес доставки введите:"Изменить адрес доставки" Выберете услугу:', reply_markup=Classic_keys)

@bot.callback_query_handler(func=lambda call: True)
def callback_data(call):
    if call.data == 'taste1':
        bot.send_message(call.message.chat.id, text='✅Вы выбрали вкус: ВИНОГРАД🍇. \n Комментарием к оплате укажите:' + str(call.message.chat.id),
                         reply_markup=pay_cut_for_elf_bar)
    elif call.data == 'taste2':
        bot.send_message(call.message.chat.id, text='✅Вы выбрали вкус: МАНГО🥭. \n Комментарием к оплате укажите: ' + str(call.message.chat.id),
                         reply_markup=pay_cut_for_elf_bar)
    elif call.data == 'taste3':
        bot.send_message(call.message.chat.id, text='✅Вы выбрали вкус: ЧЕРНИКА \u1FAD0 \n Комментарием к оплате укажите: ' + str(call.message.chat.id),
                         reply_markup=pay_cut_for_elf_bar)
    elif call.data == 'taste4':
        bot.send_message(call.message.chat.id, text='✅Вы выбрали вкус: ЛЕДЯНАЯ МЯТА🧊. \n Комментарием к оплате укажите: ' + str(call.message.chat.id),
                         reply_markup=pay_cut_for_elf_bar)
    elif call.data == 'taste5':
        bot.send_message(call.message.chat.id, text='✅Вы выбрали вкус: ЛЕДЯНОЙ БАНАН🧊. \n Комментарием к оплате укажите: ' + str(call.message.chat.id),
                         reply_markup=pay_cut_for_elf_bar)
    elif call.data == 'taste6':
        bot.send_message(call.message.chat.id, text='✅Вы выбрали вкус: ЛЕДЯНАЯ КЛУБНИКА🧊. \n Комментарием к оплате укажите: ' + str(call.message.chat.id),
                         reply_markup=pay_cut_for_elf_bar)
    elif call.data == 'taste_puff1':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: Ананас 🍍. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_puff)
    elif call.data == 'taste_puff2':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: Виноград 🍇. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_puff)
    elif call.data == 'taste_puff3':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: Ледяная дыня 🧊. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_puff)
    elif call.data == 'taste_puff4':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: Вкус с секретом 🍈. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_puff)
    elif call.data == 'taste_puff5':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: Клубника 🍓. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_puff)
    elif call.data == 'taste_puff6':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: Мята с холодком 🍃. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_puff)
    elif call.data == 'taste_puff7':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: Малиновый мармелад 🧊. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_puff)
    elif call.data == 'taste_puff_1':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: Алоэ-Виноград 🍇. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_puff_pls)
    elif call.data == 'taste_puff_2':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: Арбуз-Киви-Фрукты 🍉. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_puff_pls)
    elif call.data == 'taste_puff_3':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: Арбуз-лимон со льдом 🧊. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_puff_pls)
    elif call.data == 'taste_puff4_':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: Банан со льдом 🧊. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_puff_pls)
    elif call.data == 'taste_puff5_':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: Банановое мороженное 🍌. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_puff_pls)
    elif call.data == 'taste_puff6_':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: Виноград 🍇. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_puff_pls)
    elif call.data == 'taste_puff7_':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: Гранат. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_puff_pls)
    elif call.data == 'taste_puff8_':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: Драгонфрут-Клубника 🍓. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_puff_pls)
    elif call.data == 'taste_puff9_':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: Ледяная дыня 🧊. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_puff_pls)
    elif call.data == 'taste_puff10_':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: Клубника-банан 🍹. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_puff_pls)
    elif call.data == 'taste_puff11_':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: Космополитан 🍸. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_puff_pls)
    elif call.data == 'taste_puff12_':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: Лимонад из синей малины 🍾. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_puff_pls)
    elif call.data == 'taste_puff13_':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: Личи со льдом 🧊. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_puff_pls)
    elif call.data == 'taste_puff14_':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: Лонг Айленд 🥂. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_puff_pls)
    elif call.data == 'taste_puff15_':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: Май Тай 🧉. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_puff_pls)
    elif call.data == 'taste_puff16_':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: Манго 🥭. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_puff_pls)
    elif call.data == 'taste_puff17_':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: Манго-Ананас 🍍. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_puff_pls)
    elif call.data == 'taste_puff18_':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: Персик со льдом 🧊. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_puff_pls)
    elif call.data == 'taste_puff19_':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: Пина Колада 🍾. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_puff_pls)
    elif call.data == 'taste_puff20_':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: Яблоко-ягоды 🍎. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_puff_pls)
    elif call.data == 'taste_puff21_':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: Ягодный Микс 🍒. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_puff_pls)
    elif call.data == 'taste_jull1':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: МЕНТОЛ. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_juul_5)
    elif call.data == 'taste_jull2':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: ОГУРЕЦ. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_juul_5)
    elif call.data == 'taste_jull3':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: ТАБАК. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_juul_5)
    elif call.data == 'taste_jull4':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: МАНГО. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_juul_5)
    elif call.data == 'taste_jull_1':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: МЕНТОЛ. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_juul_apex)
    elif call.data == 'taste_jull_2':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: ОГУРЕЦ. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_juul_apex)
    elif call.data == 'taste_jull_3':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: ТАБАК. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_juul_apex)
    elif call.data == 'taste_jull_4':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: МАНГО. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_juul_apex)
    elif call.data == 'taste_culve1':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: АНАНАС 🍍. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut)
    elif call.data == 'taste_culve2':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: АПЕЛЬСИН 🍊. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut)
    elif call.data == 'taste_culve3':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: АРБУЗ 🍉. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut)
    elif call.data == 'taste_culve4':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: БАНАН 🍌. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut)
    elif call.data == 'taste_culve5':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: ВИНОГРАД 🍇. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut)
    elif call.data == 'taste_culve6':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: ГУАВА-АПЕЛЬСИН. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut)
    elif call.data == 'taste_culve7':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: ДЫНЯ. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut)
    elif call.data == 'taste_culve8':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: ЖВАЧКА. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut)
    elif call.data == 'taste_culve9':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: КЛУБНИКА 🍓. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut)
    elif call.data == 'taste_culve10':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: КОЛА 🥤. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut)
    elif call.data == 'taste_culve11':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: ЛИЧИ 🍓. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut)
    elif call.data == 'taste_culve12':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: МЯТА. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut)
    elif call.data == 'taste_culve13':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: МУЛЬТФРУКТ 🍑. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut)
    elif call.data == 'taste_culve14':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: РОЗОВЫЙ ЛИМОНАД. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut)
    elif call.data == 'taste_culve15':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: ЧЕРНИКА. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut)
    elif call.data == 'taste_culve16':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: ШОРИА. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut)
    elif call.data == 'taste_culve17':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: ЭНЕРГЕТИК 🥤. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut)
    elif call.data == 'taste_culve18':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: ЯБЛОКО 🍎. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut)
    elif call.data == 'taste__culve1':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: АНАНАС 🍍. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_curva_plus)
    elif call.data == 'taste__culve2':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: АПЕЛЬСИН 🍊. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_curva_plus)
    elif call.data == 'taste__culve3':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: АРБУЗ 🍉. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_curva_plus)
    elif call.data == 'taste__culve4':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: БАНАН 🍌. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_curva_plus)
    elif call.data == 'taste__culve5':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: ВИНОГРАД 🍇. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_curva_plus)
    elif call.data == 'taste__culve6':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: ГУАВА-АПЕЛЬСИН. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_curva_plus)
    elif call.data == 'taste__culve7':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: ДЫНЯ. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_curva_plus)
    elif call.data == 'taste__culve8':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: ЖВАЧКА. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_curva_plus)
    elif call.data == 'taste__culve9':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: КЛУБНИКА 🍓. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_curva_plus)
    elif call.data == 'taste__culve10':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: КОЛА 🥤. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_curva_plus)
    elif call.data == 'taste__culve11':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: ЛИЧИ 🍓. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_curva_plus)
    elif call.data == 'taste__culve12':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: МЯТА. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_curva_plus)
    elif call.data == 'taste__culve13':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: МУЛЬТФРУКТ 🍑. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_curva_plus)
    elif call.data == 'taste__culve14':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: РОЗОВЫЙ ЛИМОНАД. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_curva_plus)
    elif call.data == 'taste__culve15':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: ЧЕРНИКА. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_curva_plus)
    elif call.data == 'taste__culve16':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: ШОРИА. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_curva_plus)
    elif call.data == 'taste__culve17':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: ЭНЕРГЕТИК 🥤. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_curva_plus)
    elif call.data == 'taste__culve18':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: ЯБЛОКО 🍎. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_curva_plus)
    elif call.data == 'taste_maxim1':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: АПЕЛЬСИН. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_maxim)
    elif call.data == 'taste_maxim2':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: БАНАН. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_maxim)
    elif call.data == 'taste_maxim3':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: ВИНОГРАД. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_maxim)
    elif call.data == 'taste_maxim4':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: ДЫНЯ. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_maxim)
    elif call.data == 'taste_maxim5':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: КЛУБНИКА. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_maxim)
    elif call.data == 'taste_maxim6':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: КОЛА. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_maxim)
    elif call.data == 'taste_maxim7':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: КОРИЦА. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_maxim)
    elif call.data == 'taste_maxim8':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: ЛИМОННЫЙ ПИРОГ. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_maxim)
    elif call.data == 'taste_maxim9':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: МАНГО. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_maxim)
    elif call.data == 'taste_maxim10':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: МУЛЬТИФРУКТ. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_maxim)
    elif call.data == 'taste_maxim11':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: МЯТА. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_maxim)
    elif call.data == 'taste_maxim12':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: ЧЕРНИКА. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_maxim)
    elif call.data == 'taste_mega1':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: АНАНАС 🍍. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_mega)
    elif call.data == 'taste_mega2':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: АРБУЗ. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_mega)
    elif call.data == 'taste_mega3':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: КЛУБНИЧНЫЙ ПОНЧИК. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_mega)
    elif call.data == 'taste_mega4':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: КОНФЕТНОЕ БЕЗУМИЕ. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_mega)
    elif call.data == 'taste_mega5':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: ЛЕСНЫЕ ЯГОДЫ. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_mega)
    elif call.data == 'taste_mega6':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: МАНГО-ДЫНЯ. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_mega)
    elif call.data == 'taste_mega7':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: ПИНА КОЛАДА. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_mega)
    elif call.data == 'taste_mega8':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: СОЧНЫЙ ВИНОГРАД. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_mega)
    elif call.data == 'taste_rosy1':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: АНАНАС 🍍. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_rosy)
    elif call.data == 'taste_rosy2':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: ВИНОГРАД. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_rosy)
    elif call.data == 'taste_rosy3':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: ГРЕЙПФРУТ. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_rosy)
    elif call.data == 'taste_rosy4':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: ГУАВА. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_rosy)
    elif call.data == 'taste_rosy5':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: ДЫНЯ. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_rosy)
    elif call.data == 'taste_rosy6':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: ЕЖЕВИКА. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_rosy)
    elif call.data == 'taste_rosy7':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: КИВИ-ГРАНАТ. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_rosy)
    elif call.data == 'taste_rosy8':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: КОЛА. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_rosy)
    elif call.data == 'taste_rosy9':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: ЛИЧИ. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_rosy)
    elif call.data == 'taste_rosy10':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: МАНГО-МАРАКУЙЯ. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_rosy)
    elif call.data == 'taste_rosy11':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: МАНГО. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_rosy)
    elif call.data == 'taste_rosy12':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: МЯТА. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_rosy)
    elif call.data == 'taste_rosy13':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: МОХИТО. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_rosy)
    elif call.data == 'taste_rosy14':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: ОГНИ МАЙАМИ. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_rosy)
    elif call.data == 'taste_rosy15':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: ПЕРСИК. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_rosy)
    elif call.data == 'taste_rosy16':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: РОЗОВЫЙ ЛИМОНАД. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_rosy)
    elif call.data == 'taste_rosy17':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: ЧЕРНИКА. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_rosy)
    elif call.data == 'taste_rosy18':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: ЯБЛОКО. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_rosy)
    elif call.data == 'taste_stark1':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: ВИШНЯ. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_stark)
    elif call.data == 'taste_stark2':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: КОРИЦА. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_stark)
    elif call.data == 'taste_super1':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: АПЕЛЬСИН. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_super)
    elif call.data == 'taste_super2':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: ВИНОГРАД. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_super)
    elif call.data == 'taste_super3':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: ДЫНЯ. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_super)
    elif call.data == 'taste_super4':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: КЛУБНИКА-БАНАН. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_super)
    elif call.data == 'taste_super5':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: КЛУБНИКА-АРБУЗ. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_super)
    elif call.data == 'taste_super6':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: ЛИЧИ. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_super)
    elif call.data == 'taste_super7':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: МАНОГ-ЛИЧИ. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_super)
    elif call.data == 'taste_super8':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: МУЛЬТИФРУКТ. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_super)
    elif call.data == 'taste_super9':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: МЯТА. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_super)
    elif call.data == 'taste_super10':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: ЧЕРНИКА. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_super)
    elif call.data == 'taste_ultra1':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: АНАНАС. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_ultrastick)
    elif call.data == 'taste_ultra2':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: АРБУЗ. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_ultrastick)
    elif call.data == 'taste_ultra3':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: ДЫНЯ. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_ultrastick)
    elif call.data == 'taste_ultra4':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: ЖВАЧКА. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_ultrastick)
    elif call.data == 'taste_ultra5':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: КЛУБНИКА. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_ultrastick)
    elif call.data == 'taste_ultra6':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: КОЛА. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_ultrastick)
    elif call.data == 'taste_ultra7':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: КОРИЦА. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_ultrastick)
    elif call.data == 'taste_ultra8':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: МАНГО. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_ultrastick)
    elif call.data == 'taste_ultra9':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: МЯТА. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_ultrastick)
    elif call.data == 'taste_ultra10':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: ПЕРСИК. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_ultrastick)
    elif call.data == 'taste_ultra11':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: РОЗОВЫЙ ЛИМОНАД. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_ultrastick)
    elif call.data == 'taste_ultra12':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали вкус: ЯБЛОКО. \n Комментарием к оплате укажите: ' + str(
                             call.message.chat.id),
                         reply_markup=pay_cut_for_ultrastick)


    elif call.data == 'device':
        bot.send_photo(call.message.chat.id, photo=open('hpue9th-KTM.jpg', 'rb'))
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали Juul DEVICE цена: 990₽', reply_markup=pay_cut
                         )
    elif call.data == 'jull_pods':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали Juul PODS \nВыберете тип:', reply_markup= juul_pods_typs
                         )
    elif call.data == 'apex':
        photo = open('225-800x800.jpg', 'rb')
        bot.send_photo(call.message.chat.id, photo)
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали Juul APEX PODS\nЦена:350\nВыберете вкус:', reply_markup= tastes_for_juul_apex
                         )
    elif call.data == 'pods-5':
        photo = open('juul-menthol-4-pack.jpg', 'rb')
        bot.send_photo(call.message.chat.id, photo)
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали Juul PODS 5%\nЦена:350₽\nВыберете вкус:', reply_markup=tastes_for_juul
                         )
    elif call.data == 'puff_class':
        photo = open('RLTs2QOYiL4.jpg', 'rb')
        bot.send_photo(call.message.chat.id, photo)
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали PUFF BAR\nЦена:300₽\nВыберете вкус:',
                         reply_markup=tastes_for_puff_bar)
    elif call.data == 'puff_plus':
        photo = open('45HsKyRi2F8.jpg', 'rb')
        bot.send_photo(call.message.chat.id, photo)
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали PUFF PLUS\nЦена:500₽\nВыберете вкус:',
                         reply_markup=tastes_for_puff_plus)
    elif call.data == 'cuvie':
        photo = open('pXGcjie7FkE.jpg', 'rb')
        bot.send_photo(call.message.chat.id, photo)
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали HQD CUVIE\nЦена:300₽\n300 ЗАТЯЖЕК\nВыберете вкус:',
                         reply_markup=culve_tastes)
    elif call.data == 'cuvie_pl':
        photo = open('s4-A9Z4xa6Q.jpg', 'rb')
        bot.send_photo(call.message.chat.id, photo)
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали HQD CUVIE PLUS\nЦена:600₽\n300 ЗАТЯЖЕК\nВыберете вкус:',
                         reply_markup=culve_tastes)
    elif call.data == 'maxim':
        photo = open('2gj37tcpJbs.jpg', 'rb')
        bot.send_photo(call.message.chat.id, photo)
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали HQD MAXIM\nЦена:400₽\n400 ЗАТЯЖЕК\nВыберете вкус:',
                         reply_markup=maxim_tastes)
    elif call.data == 'mega':
        photo = open('JYwOLcICM3U.jpg', 'rb')
        bot.send_photo(call.message.chat.id, photo)
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали HQD MEGA\nЦена:950₽\n1800 ЗАТЯЖЕК\nВыберете вкус:',
                         reply_markup=mega_tastes)
    elif call.data == 'rosy':
        photo = open('dVrzM6mKzuo.jpg', 'rb')
        bot.send_photo(call.message.chat.id, photo)
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали HQD ROSY\nЦена:450₽\n450 ЗАТЯЖЕК\nВыберете вкус:',
                         reply_markup=rosy_tastes)
    elif call.data == 'startk':
        photo = open('Nc-TNivO7ls.jpg', 'rb')
        bot.send_photo(call.message.chat.id, photo)
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали HQD STARK\nЦена:350₽\n300 ЗАТЯЖЕК\nВыберете вкус:',
                         reply_markup=stark_tastes)
    elif call.data == 'super':
        photo = open('DDusCy4ia5M.jpg', 'rb')
        bot.send_photo(call.message.chat.id, photo)
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали HQD SUPER\nЦена:550₽\n800 ЗАТЯЖЕК\nВыберете вкус:',
                         reply_markup=super_tastes)
    elif call.data == 'ultradick':
        photo = open('fY8-T3xPm4Y.jpg', 'rb')
        bot.send_photo(call.message.chat.id, photo)
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали HQD ULTRASTICK\nЦена:420₽\nВыберете вкус:',
                         reply_markup=Ultrastick_tastes)
    elif call.data == 'hqd1':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали PUFF. Выберете тип:',
                         reply_markup=types_of_puffs)
    elif call.data == 'hqd2':
        photo = open('eq0hy30qh9w8kco8oko0kwsw4gks44.jpg', 'rb')
        bot.send_photo(call.message.chat.id, photo)
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали ELF BAR.\nЦена:550₽\nВыберете вкус:',
                         reply_markup=tastes_for_elf)
    elif call.data == 'hqd3':
        bot.send_message(call.message.chat.id,
                         text='✅Вы выбрали JUUL. Выберете тип:',
                         reply_markup=types_of_juul)
    elif call.data == 'hqd5':
        bot.send_message(call.message.chat.id, text='✅Вы выбрали HQD. Выберете тип:',
                         reply_markup=types_of_hqd)
    elif call.data == 'back':
        bot.send_message(call.message.chat.id, text='Выберете одноразку:',
                         reply_markup=HQD_name)
    elif call.data == 'pay':
        pass
    elif call.data == 'check':
        lastPayments = payment_history_last(mylogin, api_access_token, '5','','')
        if str(call.message.chat.id) in lastPayments['data'][0]['comment']:
            bot.send_message(call.message.chat.id, text='non-empty')
        elif 'NETFLIX WEB>MOSCOW' in lastPayments['data'][0]['comment']:
            bot.send_message(call.message.chat.id, text='Платёж проведён')
        else:
            bot.send_message(call.message.chat.id, text='В обработке!')



@bot.message_handler(content_types=['location'])
def location (message):
    if message.location is not None:
        print(message.location)
        bot.send_message(message.chat.id, text='Геопозиция принята', reply_markup=Classic_keys)


bot.polling(none_stop= True)