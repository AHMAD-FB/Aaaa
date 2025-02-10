import telebot
import json
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "توكنك"
ADMIN_ID = ايدي

bot = telebot.TeleBot(TOKEN)

try:
    with open("users.json", "r") as file:
        users = json.load(file)
except:
    users = {}

pending_replies = {}

def save_users():
    with open("users.json", "w") as file:
        json.dump(users, file)

@bot.message_handler(commands=['start'])
def start(message):
    user_id = str(message.chat.id)
    if user_id not in users:
        users[user_id] = True
        save_users()

    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("👤 المطور", url="https://t.me/sjadiraqi"))

    bot.send_message(message.chat.id, "اهلا بيك عزيزي في بوت التواصل تقدر تتواصل وياي من البوت 👾

برمجة سجاد", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.chat.id != ADMIN_ID)
def forward_to_admin(message):
    msg = bot.forward_message(ADMIN_ID, message.chat.id, message.message_id)
    pending_replies[msg.message_id] = message.chat.id
    bot.send_message(message.chat.id, "تم توصيل رسالتك بعد شوية يجيك الرد 👾")

@bot.message_handler(func=lambda message: message.chat.id == ADMIN_ID and message.reply_to_message)
def reply_to_user(message):
    original_msg = message.reply_to_message.message_id

    if original_msg in pending_replies:
        user_id = pending_replies[original_msg]
                bot.send_message(user_id, f"📩 رد الادمن الك :\n{message.text}")
        bot.send_message(ADMIN_ID, "تمم 👾⚪")
    else:
        bot.send_message(ADMIN_ID, "error 404")

@bot.message_handler(commands=['a'])
def admin_panel(message):
    if message.chat.id == ADMIN_ID:
        keyboard = InlineKeyboardMarkup()
        keyboard.add(
            InlineKeyboardButton("عدد المستخدمين", callback_data="aa1"),
            InlineKeyboardButton("اذاعة", callback_data="broadcast")
        )
        bot.send_message(ADMIN_ID, "لوحة ادمن بسيطةة", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.message.chat.id == ADMIN_ID)
def handle_admin_buttons(call):
    if call.data == "aa1":
        bot.answer_callback_query(call.id, f"📊 عدد المستخدمين: {len(users)}")

    elif call.data == "broadcast":
        bot.send_message(ADMIN_ID, "✍️ أرسل رسالة ليتم إرسالها إلى جميع المشتركين.")

        @bot.message_handler(func=lambda message: message.chat.id == ADMIN_ID)
        def send_broadcast(message):
            for user in users.keys():
                try:
                    bot.send_message(int(user), f"📢 إذاعة :\n\n{message.text}")
                except:
                    pass
            bot.send_message(ADMIN_ID, "تمت الاذاعة.")

bot.polling()olling()