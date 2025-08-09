import re
import phonenumbers
from phonenumbers.phonenumberutil import NumberParseException
from telebot.types import Message

from app.messages.message_text import PHONE_START_TEXT, INVALID_NUMBER_TEXT
from app.database.add_in_db import add_info_in_database
from app.trackers.phone_track import phone_found, format_phone_info
from app.logger import logger


def phone_message_handler(bot, message: Message) -> None:
    """Обработка команды /phone — запрос номера телефона у пользователя"""
    bot.send_message(message.chat.id, PHONE_START_TEXT)
    # Регистрируем следующий шаг — ввод номера телефона
    bot.register_next_step_handler(message, lambda m: phone_input_info(bot, m))


def phone_input_info(bot, message: Message) -> None:
    """Обработка номера телефона, проверка корректности и вывод информации"""
    number = message.text.strip()
    # Проверяем, что номер соответствует шаблону + и 11 цифр подряд
    number_re_check = re.fullmatch(r'\+\d{11}', number)

    try:
        # Парсим номер с помощью phonenumbers
        parse_number = phonenumbers.parse(number)

        # Проверяем валидность номера и совпадение с регуляркой
        if phonenumbers.is_valid_number(parse_number) and number_re_check:
            # Сохраняем запрос пользователя в базу данных
            user_id = str(message.from_user.id)
            username = message.from_user.username
            add_info_in_database(user_id, username, number)
            logger.info(f'{username} выполнил проверку номера')

            # Получаем и форматируем информацию по номеру
            result_list_info = format_phone_info(phone_found(number))
            bot.send_message(message.chat.id, result_list_info)
        else:
            # При неверном формате — сообщение об ошибке и повторный запрос
            bot.send_message(message.chat.id, INVALID_NUMBER_TEXT)
            bot.register_next_step_handler(message, lambda m: phone_input_info(bot, m))

    except NumberParseException:
        # При ошибке разбора номера — сообщение об ошибке и повторный запрос
        bot.send_message(message.chat.id, INVALID_NUMBER_TEXT)
        bot.register_next_step_handler(message, lambda m: phone_input_info(bot, m))
