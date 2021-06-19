import telebot
from telebot import types
from flask import Flask, request
import os

# pip3 install pyTelegramBotAPI

# свой токен бота из botFather
TOKEN = '1801416631:AAF9HsyblY1WhIYLJDfZPV616ca8Sm4NcpI'

SITE = 'https://www.005.ru/?name='

# ссылка на контакт в телеграмме
CONTACT = '@ark_005'

bot = telebot.TeleBot(TOKEN, parse_mode=None)


@bot.message_handler(commands=['start'])
def hello_new_user(message):
    bot.reply_to(message, 'Команда полиграфического сервиса 005.ru приветствует Вас! Хотите найти продукт - наберите /f и название продукта (например: /f этикетка), хотите задать вопрос - наберите /q и пишите вопрос, ')

@bot.message_handler(commands=['f'])
def find_on_site(message):
    msg = message.text
    name = msg[3:]
    href = SITE + name
    final_result = f'результат по поиску {name} находится на {href}'
    bot.reply_to(message, str(final_result))


@bot.message_handler(commands=['q'])
def user_questions(message):
    msg = message.text
    question = msg[3:]
    questions = {'work': 'we work in club', 'help': 'i help you'}
    if question in questions:
        bot.reply_to(message, str(questions[question]))
    else:
        bot.reply_to(message, f"Такого вопроса нету свяжитесь с {CONTACT}")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, 'Комманды: \n Найти на сайте продукт поиска наберите /f (название продукта) \n Задать вопрос - наберите /q (вопрос) ')


@bot.message_handler(content_types=["new_chat_members"])
def handler_new_member(message):
    user_name = message.new_chat_member.first_name
    bot.send_message(message.chat.id, "Добро пожаловать, {0}!".format(user_name))

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)

server = Flask(__name__)
@server.route("/bot", methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200
@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url="https://telegram-005bot.herokuapp.com/bot") # этот url нужно заменить на url вашего Хероку приложения
    return "?", 200

server.run(host="0.0.0.0", port=os.environ.get('PORT', 80))

