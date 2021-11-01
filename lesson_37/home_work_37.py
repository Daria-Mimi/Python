from telebot import TeleBot

TOKEN = "2088516025:AAEe1W6IDI_udqJuHvJgNw0Jq3Uxbx3nqS8"
bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, "Добрый день! \nДобро пожаловать в чат-бот по подготовке к собеседованию!")

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.from_user.id, "Данный бот написан для того, чтобы помочь тебе подготовиться к собеседованию.\n"
                                           "Чтобы начать собеседование, выполни команду /ask_me.")

@bot.message_handler(commands=['ask_me'])
def ask_me(message):
    bot.send_message(message.from_user.id, "Строки (str) относятся к изменяемуму типу данных?")
    if message.text == "Нет":
        bot.send_message(message.from_user.id, "Правильный ответ!")
    elif message.text == "Да":
        bot.send_message(message.from_user.id, "Это не правильный ответ. Ознакомься с информацией на сайте:\n"
                                                      "http://old.pynsk.ru/posts/2015/Aug/17/sintaksis-python-izmeniaemye-i-neizmeniaemye-tipy-dannykh/#.YYAQoZ5Bw2w")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю.")


bot.polling()