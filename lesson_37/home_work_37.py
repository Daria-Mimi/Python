from telebot import TeleBot

TOKEN = "2088516025:AAEe1W6IDI_udqJuHvJgNw0Jq3Uxbx3nqS8"
bot = TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Добрый день! Добро пожаловать в чат-бот по подготовке к собеседованию!")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Данный бот написан для того, чтобы помочь тебе подготовиться к собеседованию. "
                                               "Чтобы начать выполни команду /go.")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

bot.polling()