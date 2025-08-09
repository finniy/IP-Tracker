from telebot import types
from telebot.types import Message
from app.messages.message_text import WELCOME_TEXT


def start_handler(bot, message: Message) -> None:
    # Кнопки
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        types.KeyboardButton('/ip'),
        types.KeyboardButton('/phone'),
        types.KeyboardButton('/history')
    )

    bot.send_message(message.chat.id, WELCOME_TEXT, reply_markup=markup)
