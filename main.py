import telebot
from info import user_data

TOKEN = '6769332141:AAExVUnMzcjrooAmmevPVysALd_4lVJCjyE'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "i")


@bot.message_handler(commands=['start'])
def handle_start(message):
    user_id = message.from_user.id
    if user_id not in user_data:
        bot.send_message(message.chat.id, "Пожалуйста, пришли сначала свой возраст.")


bot.polling()
