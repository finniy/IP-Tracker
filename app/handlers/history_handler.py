from telebot.types import Message
from app.database.take_db import take_user_history
from app.utils.format_requests import format_user_requests


def send_user_history_handler(bot, message: Message) -> None:
    user_id = str(message.from_user.id)
    username = message.from_user.username

    lst_with_requests = format_user_requests(take_user_history(user_id), username)
    bot.send_message(message.chat.id, lst_with_requests)
