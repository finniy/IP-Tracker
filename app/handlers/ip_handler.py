from telebot.types import Message
from app.messages.message_text import IP_START_TEXT, INVALID_IP_TEXT
from app.database.add_in_db import add_info_in_database
from app.trackers.ip_track import get_info_by_ip, format_ip_info
from app.utils.send_map import send_map_photo
from app.utils.check_valid_ip import is_valid_ip_first
from app.logger import logger


def ip_message_handler(bot, message: Message) -> None:
    # Запрос у пользователя ввести IP-адрес
    bot.send_message(message.chat.id, IP_START_TEXT)
    bot.register_next_step_handler(message, lambda m: ip_input_info(bot, m))


def ip_input_info(bot, message: Message) -> None:
    ip_address = message.text.strip()

    if is_valid_ip_first(ip_address):
        ip_info, map_url = get_info_by_ip(ip_address)

        if isinstance(ip_info, dict) and map_url:
            # Сохраняем запрос пользователя в базу данных
            user_id = str(message.from_user.id)
            username = message.from_user.username
            user_request = ip_address
            add_info_in_database(user_id, username, user_request)
            logger.info(f'{username} выполнил проверку ip')

            # Форматируем и отправляем информацию по IP, а также карту
            ip_info = format_ip_info(ip_info)
            bot.send_message(message.chat.id, ip_info)
            send_map_photo(message, map_url)
        else:
            # Ошибка при получении информации, повторный запрос
            bot.send_message(message.chat.id, ip_info)
            bot.register_next_step_handler(message, lambda m: ip_input_info(bot, m))
    else:
        # Неверный формат IP, повторный запрос
        bot.send_message(message.chat.id, INVALID_IP_TEXT)
        bot.register_next_step_handler(message, lambda m: ip_input_info(bot, m))
