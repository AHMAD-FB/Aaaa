import requests
import telebot
from telebot import types
tokin = input("EnTeR ToKeN : ")
while True:
    try:
        bot = telebot.TeleBot(tokin)
        @bot.message_handler(commands=['start'])
        def welcome(message):
            start = types.InlineKeyboardButton(text="𝘀𝘁𝗮𝗿𝘁 ▶'✅ ",callback_data="start")
            ch0 = types.InlineKeyboardButton(text="𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿  🧑‍💻 ",url="https://t.me/Abdullah_Abd_alsalam")
            ch1 = types.InlineKeyboardButton(text="𝗞𝗲𝘆 📎",url="https://t.me/u_zzf")
            Keyboards = types.InlineKeyboardMarkup()
            Keyboards.row_width = 1
            Keyboards.add(start,ch0,ch1)
            bot.reply_to(message,text=f"<strong>  𝗔𝗽𝗽 𝗡𝗮𝗺𝗲 : Hi {message.from_user.first_name} In Bot Fake Email For 10 Minutes \n By | @Abdullah_Abd_alsalam , @u_zzf</strong>", parse_mode="html", reply_markup=Keyboards)
        @bot.callback_query_handler(func=lambda call: True)
        def bot_query_handler(call):
            if call.data == "start":
                run(call.message)
            elif call.data == "new":
                new_get(call.message)
            elif call.data == "msg":
                msg_get(call.message)
        def run(message):
            new = types.InlineKeyboardButton(text=" Get New Email ✅ ",callback_data="new")
            msg = types.InlineKeyboardButton(text=" Get New Message  ✅ ",callback_data="msg")
            Key = types.InlineKeyboardMarkup()
            Key.row_width = 1
            Key.add(new,msg)
            bot.reply_to(message,text=f"<strong>Click Get New Email Or Click On Get New Message To See New Messages\n@u_zzf 🧑‍💻 </strong>", parse_mode="html", reply_markup=Key)
        def new_get(message):
        	url = "https://10minutemail.net/address.api.php"
        	re = requests.get(url).json()
        	s = re["session_id"]
        	m = re['mail_get_mail']
        	bot.send_message(message.chat.id, text=f"<strong> Done  New Email \nEmail : {m} \n \n@u_zzf</strong>",parse_mode="html")
        	bot.send_message(message.chat.id, text=f'ID email : ```{s}```', parse_mode='markdown')
        def msg_get(message):
            mssg = bot.reply_to(message,""" 
<strong>Please Send Your Email ID To See Messages 🌝💁</strong>
""", parse_mode="html")
            bot.register_next_step_handler(mssg, run_msg)
        def run_msg(message):
        	mesg = message.text
        	code = requests.get("https://10minutemail.net/address.api.php",cookies={"PHPSESSID":mesg})
        	d = code.json()['mail_list'][0]['subject']
        	bot.send_message(message.chat.id, text=f"<strong>{d}</strong>",parse_mode="html")
        try:
            
            bot.polling(True)
        except Exception as ex:
            print(ex)
            telebot.logger.error(ex)
    except:
        continue