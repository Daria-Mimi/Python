import telebot

bot = telebot.TeleBot('1944569305:AAHtdGr1PKk5QHBK-fow25aJEgMxC7MUHZ4')

# TOKEN = "1944569305:AAHtdGr1PKk5QHBK-fow25aJEgMxC7MUHZ4"
#
# @bot.message_handler(content_types=['Hello!'])
# def get_text_messages(message):


token = '123456'
TelegramBot = telebot.Bot(token)
print(TelegramBot.getMe())