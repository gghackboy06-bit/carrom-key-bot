import telebot
import os

TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(
        message,
        "🎮 Welcome to Carrom Pool Key Store!\n\n"
        "🛒 Purchase Products\n"
        "💰 Check Balance\n"
        "➕ Add Balance"
    )

print("Bot Started...")
bot.infinity_polling()
