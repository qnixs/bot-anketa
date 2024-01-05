import telebot

TOKEN = '6769332141:AAExVUnMzcjrooAmmevPVysALd_4lVJCjyE'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "hi")


bot.polling()
