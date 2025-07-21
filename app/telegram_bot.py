import telebot
from telebot.types import Message
from dotenv import load_dotenv
import phonenumbers
from phonenumbers.phonenumberutil import NumberParseException
import os
from ip_track import get_info_by_ip, format_ip_info
from phone_tracker import phone_found, format_phone_info
from telebot import types
import re
from check_valid_ip import is_valid_ip_first
from database import add_info_in_database

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
phone_start_text = "⚠️ Номер вводите в формате: +71234567890 (без пробелов)"
ip_start_text = "🌐 Введите IP-адрес в формате 192.168.0.1"
invalid_number_text = (
    "❌ Неверный формат номера.\n"
    "Пожалуйста, введи номер в формате: +71234567890 (без пробелов и символов)."
)
invalid_ip_text = (
    "❌ Неверный формат IP-адреса.\n"
    "Пожалуйста, введите корректный IP-адрес, например: 192.168.1.1"
)


@bot.message_handler(commands=['start', 'START'])
def start(message: Message) -> None:
    # Обработка команды /start — отправка приветствия и отображение кнопок
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton('/ip')
    button_2 = types.KeyboardButton('/phone')
    markup.add(button_1, button_2)
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)


@bot.message_handler(commands=['help', 'HELP'])
def help(message: Message) -> None:
    # Обработка команды /help — вывод списка доступных команд
    bot.send_message(message.chat.id, help_text)


@bot.message_handler(commands=['phone', 'PHONE'])
def phone_message(message: Message) -> None:
    # Обработка команды /phone — запрос номера телефона у пользователя
    bot.send_message(message.chat.id, phone_start_text)
    bot.register_next_step_handler(message, phone_input_info)


def phone_input_info(message: Message) -> None:
    # Обработка номера телефона, проверка его корректности и вывод информации
    number = message.text.strip()
    number_re_check = re.fullmatch(r'\+\d{11}', number)

    try:
        parse_number = phonenumbers.parse(number)

        if phonenumbers.is_valid_number(parse_number) and number_re_check:
            # Сохраняем запрос в базу данных
            user_id = str(message.from_user.id)
            username = message.from_user.username
            user_request = number
            add_info_in_database(user_id, username, user_request)

            # Отправка отформатированной информации
            result_list_info = format_phone_info(phone_found(number))
            bot.send_message(message.chat.id, result_list_info)
        else:
            # Повторный запрос при неверном формате
            bot.send_message(message.chat.id, invalid_number_text)
            bot.register_next_step_handler(message, phone_input_info)

    except NumberParseException:
        # Ошибка при разборе номера
        bot.send_message(message.chat.id, invalid_number_text)
        bot.register_next_step_handler(message, phone_input_info)


@bot.message_handler(commands=['ip', 'IP'])
def ip_message(message: Message) -> None:
    # Обработка команды /ip — запрос IP-адреса у пользователя
    bot.send_message(message.chat.id, ip_start_text)
    bot.register_next_step_handler(message, ip_input_info)


def ip_input_info(message: Message) -> None:
    # Обработка IP-адреса, проверка и вывод информации + карта
    ip_address = message.text.strip()

    if is_valid_ip_first(ip_address):
        ip_info, map_url = get_info_by_ip(ip_address)

        if isinstance(ip_info, dict) and map_url:
            # Сохраняем запрос в базу данных
            user_id = str(message.from_user.id)
            username = message.from_user.username
            user_request = ip_address
            add_info_in_database(user_id, username, user_request)

            # Отправка информации и карты
            ip_info = format_ip_info(ip_info)
            bot.send_message(message.chat.id, ip_info)
            send_map_photo(message, map_url)
        else:
            # Ошибка или не найден IP
            bot.send_message(message.chat.id, ip_info)
            bot.register_next_step_handler(message, ip_input_info)
    else:
        # Неверный IP-адрес
        bot.send_message(message.chat.id, invalid_ip_text)
        bot.register_next_step_handler(message, ip_input_info)


def send_map_photo(message: Message, map_url: str) -> None:
    # Отправка изображения карты с координатами IP
    bot.send_photo(message.chat.id, map_url, caption="🗺️ Примерное местоположение по IP")


bot.set_my_commands(commands)
bot.polling(none_stop=True)
