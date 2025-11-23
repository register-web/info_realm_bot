import os
import telebot
from telebot import types

# Получаем токен бота из переменной окружения BOT_TOKEN
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(msg):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(
        types.InlineKeyboardButton(
            text="инфа и как попасть на сервер",
            url="https://realm-webapp.vercel.app/"
        )
    )

    text = (
        "Welcome to Realm!🎉🎉🎉\n\n"
        "Realm — майнкрафт проект/сервер, нацеленный на убийство вашего свободного времени☺️\n\n"
        "Если кратко:\n"
        "интересно повыживать как в обычных дружеских играх на недельку,\n"
        "только с минимальными ограничениями для поддержки сервера,\n"
        "без донатов, без читов, без команд.\n\n"
        "Чистая ванилка 🍀"
    )

    with open("info_foto.png", "rb") as photo:
        bot.send_photo(
            msg.chat.id,
            photo,
            caption=text,
            reply_markup=keyboard
        )

# Основной запуск бота для Render
bot.infinity_polling()
