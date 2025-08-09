from telebot.types import Message
from telebot import types

from app.bot_instance import bot
from app.messages.message_text import HELP_TEXT, GITHUB_LINK_TEXT
from app.handlers.start_handler import start_handler
from app.handlers.phone_handler import phone_message_handler
from app.handlers.ip_handler import ip_message_handler
from app.handlers.history_handler import send_user_history_handler

# Список доступных команд, который будет отображаться в интерфейсе Telegram
commands = [
    types.BotCommand('start', 'Запуск бота'),
    types.BotCommand('phone', 'Пробив по номеру телефона'),
    types.BotCommand('ip', 'Пробив по IP-адресу'),
    types.BotCommand('history', 'История ваших запросов'),
    types.BotCommand('help', 'Список команд'),
    types.BotCommand('github', 'Ссылка на GitHub проекта')
]


# Обработчик команды /start
@bot.message_handler(func=lambda m: m.text and m.text.lower().startswith('/start'))
def start(message: Message) -> None:
    start_handler(bot, message)


# Обработчик команды /help — отправляет пользователю список команд
@bot.message_handler(func=lambda m: m.text and m.text.lower().startswith('/help'))
def help_command(message: Message) -> None:
    bot.send_message(message.chat.id, HELP_TEXT)


# Обработчик команды /phone — пробив по номеру телефона
@bot.message_handler(func=lambda m: m.text and m.text.lower().startswith('/phone'))
def phone_message(message: Message) -> None:
    phone_message_handler(bot, message)


# Обработчик команды /ip — пробив по IP-адресу
@bot.message_handler(func=lambda m: m.text and m.text.lower().startswith('/ip'))
def ip_message(message: Message) -> None:
    ip_message_handler(bot, message)


# Обработчик команды /history — вывод истории запросов пользователя
@bot.message_handler(func=lambda m: m.text and m.text.lower().startswith('/history'))
def send_user_history(message: Message) -> None:
    send_user_history_handler(bot, message)


# Обработчик команды /github — отправляет ссылку на GitHub проекта
@bot.message_handler(func=lambda m: m.text and m.text.lower().startswith('/github'))
def send_my_github(message: Message) -> None:
    bot.send_message(message.chat.id, GITHUB_LINK_TEXT)


# Точка входа в приложение
def main() -> None:
    # Устанавливаем список команд для удобства
    bot.set_my_commands(commands)

    # Запускаем бота в режиме постоянного прослушивания
    bot.polling(none_stop=True)
