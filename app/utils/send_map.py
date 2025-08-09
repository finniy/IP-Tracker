from telebot.types import Message
from app.bot_instance import bot
from app.messages.message_text import LOCATION_START_TEXT

def send_map_photo(message: Message, map_url: str) -> None:
    # Отправка изображения карты с координатами IP
    bot.send_photo(message.chat.id, map_url, caption=LOCATION_START_TEXT)
