import telebot
from telebot.types import Message
from dotenv import load_dotenv
import phonenumbers
from phonenumbers.phonenumberutil import NumberParseException
import os
from phone_tracker import phone_found
from telebot import types
import re

load_dotenv()
API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

commands = [
    types.BotCommand('start', 'Запуск бота и приветствие'),
    types.BotCommand('help', 'Список команд'),
    types.BotCommand('phone', 'Пробив по номеру телефона'),
    types.BotCommand('ip', 'Пробив по IP-адресу'),
]
welcome_text = (
    "👋 Привет! Добро пожаловать в IP-Tracker\n"
    "🔎 Я помогу тебе получить информацию по номеру телефона или IP-адресу.\n\n"
    "Вот что я умею:\n"
    "📱 Пробить по номеру телефона: оператор, регион, возможные утечки\n"
    "🌐 Пробить по IP-адресу: геолокация, провайдер, подозрительная активность\n\n"
    "❗️ Используй команды:\n"
    "/phone — для пробива по номеру\n"
    "/ip — для пробива по IP\n"
)
help_text = (
    "📌 Доступные команды:\n\n"
    "/phone — пробив по номеру телефона\n"
    "/ip — пробив по IP"
)
phone_text = "⚠️ Номер вводите в формате: +71234567890 (без пробелов)"
invalid_number_text = (
    "❌ Неверный формат номера.\n"
    "Пожалуйста, введи номер в формате: +71234567890 (без пробелов и символов)."
)


@bot.message_handler(commands=['start', 'START'])
def start(message: Message) -> None:
    bot.send_message(message.chat.id, welcome_text)


@bot.message_handler(commands=['help', 'HELP'])
def help(message: Message) -> None:
    bot.send_message(message.chat.id, help_text)


@bot.message_handler(commands=['phone', 'PHONE'])
def phone_message(message: Message) -> None:
    bot.send_message(message.chat.id, phone_text)
    bot.register_next_step_handler(message, phone_input_info)


def phone_input_info(message: Message) -> None:
    number = message.text.strip()
    number_re_check = re.fullmatch(r'\+\d{11}', number)
    try:
        parse_number = phonenumbers.parse(number)
        if phonenumbers.is_valid_number(parse_number) and number_re_check:
            result_list_info = phone_found(number)
            result_text = (
                f"📞 Результаты по номеру:\n\n"
                f"Страна: {result_list_info['Страна']}\n"
                f"Город: {result_list_info['Город']}\n"
                f"Оператор: {result_list_info['Оператор']}"
            )
            bot.send_message(message.chat.id, result_text)
        else:
            bot.send_message(message.chat.id, invalid_number_text)
            bot.register_next_step_handler(message, phone_input_info)
    except NumberParseException:
        bot.send_message(message.chat.id, invalid_number_text)
        bot.register_next_step_handler(message, phone_input_info)

@bot.message_handler(commands=['ip', 'IP'])
def ip_message(message: Message) -> None:
    bot.send_message(message.chat.id, "⚠️ Эта функция ещё в разработке и скоро будет доступна. Спасибо за понимание!")


bot.set_my_commands(commands)
bot.polling(none_stop=True)
