from telebot import TeleBot

TOKEN = "1234567890"
bot = TeleBot(TOKEN)

# doc = open("t_bot.txt", mode="a")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, f"Добрый день, {message.from_user.full_name}!\nДобро пожаловать в чат-бот по подготовке к собеседованию!")

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.from_user.id, "Данный бот написан для того, чтобы помочь тебе подготовиться к собеседованию.\n"
                                           "Чтобы начать собеседование, выполни команду /ask_me.")

def ask_me(func):
    def inner(*args, **kwargs):
        func(*args, **kwargs)
    return inner

@bot.message_handler(commands=['ask_me'])
@ask_me
def question_1(message):
    bot.reply_to(message, text="Строки (str) относятся к изменяемуму типу данных?")
    bot.register_next_step_handler(message, question_2)

@ask_me
def question_2(message):
    if message.text.lower() == "нет":
        bot.send_message(message.from_user.id, "Правильный ответ!")
    else:
        message.text == message.text
        bot.send_message(message.from_user.id, "Это не правильный ответ. Ознакомься с информацией на сайте:\n"
                                               "http://old.pynsk.ru/posts/2015/Aug/17/sintaksis-python-izmeniaemye-i-neizmeniaemye-tipy-dannykh/#.YYAQoZ5Bw2w")
    bot.reply_to(message, text="Каким языком программирования является Python?")
    bot.register_next_step_handler(message, question_3)

@ask_me
def question_3(message):
    if message.text.lower() == "интерпретируемым":
        bot.send_message(message.from_user.id, "Правильный ответ!")
    else:
        message.text == message.text
        bot.send_message(message.from_user.id, "Это не правильный ответ. Ознакомься с информацией на сайте:\n"
                                               "https://otus.ru/nest/post/1547/")
    bot.reply_to(message, "На этом пока все")



bot.polling()
