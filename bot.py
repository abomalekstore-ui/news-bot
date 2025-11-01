import telebot
import time

# التوكن الخاص بالبوت
TOKEN = "8376936171:AAFxfdp4S4RtyCI9f-ZDUi7vMQTXEuPQUs4"
bot = telebot.TeleBot(TOKEN)

# الأمر /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "👋 أهلاً بيك في بوت الأخبار! اكتب /news لآخر الأخبار 🔥")

# أمر /id
@bot.message_handler(commands=['id'])
def get_chat_id(message):
    bot.reply_to(message, f"📍 Chat ID الخاص بهذه القناة أو المجموعة هو:\n{message.chat.id}")

# تشغيل البوت باستمرار
while True:
    try:
        bot.polling()
    except Exception as e:
        print(e)
        time.sleep(5)
