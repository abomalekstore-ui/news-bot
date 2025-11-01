import telebot
import requests
import time
import threading

# التوكن الخاص بالبوت
TOKEN = "8376936171:AAFxfdp4S4RtyCI9f-ZDUi7vMQTXEuPQUs4"
bot = telebot.TeleBot(TOKEN)

# API KEY من NewsAPI
NEWS_API_KEY = "bf8873129ecd453d8ad8d6fac0987f7f"

# Chat ID الخاص بالقناة أو الجروب
CHAT_ID = "-7595110139"  # لو مجموعة خاصة أو قناة استخدم السالب - قبل الرقم

# دالة لجلب الأخبار
def get_latest_news():
    url = f"https://newsapi.org/v2/top-headlines?country=eg&apiKey={NEWS_API_KEY}&pageSize=5"
    response = requests.get(url)
    data = response.json()
    articles = data.get("articles", [])
    news_list = []
    for article in articles:
        title = article["title"]
        url = article["url"]
        news_list.append(f"📰 {title}\n🔗 {url}")
    return "\n\n".join(news_list) if news_list else "❌ لا توجد أخبار حالياً."

# دالة إرسال الأخبار تلقائيًا كل 15 دقيقة
def auto_send_news():
    while True:
        try:
            news = get_latest_news()
            bot.send_message(CHAT_ID, f"🗞️ آخر الأخبار:\n\n{news}")
        except Exception as e:
            print("Error sending news:", e)
        time.sleep(900)  # كل 15 دقيقة = 900 ثانية

# الأمر /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "👋 أهلاً بيك في بوت الأخبار!\nاكتب /news لعرض أحدث الأخبار 🔥")

# الأمر /news
@bot.message_handler(commands=['news'])
def send_news_now(message):
    news = get_latest_news()
    bot.reply_to(message, f"🗞️ آخر الأخبار:\n\n{news}")

# تشغيل الخيط التلقائي للأخبار
threading.Thread(target=auto_send_news, daemon=True).start()

# تشغيل البوت
bot.polling(non_stop=True)
    
