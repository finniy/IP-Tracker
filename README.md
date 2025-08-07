# 🔍 IP-Tracker — Telegram бот для пробива IP и телефонов

**IP-Tracker** — это Telegram-бот, который позволяет быстро получить информацию об IP-адресе или номере телефона:
страна, город, провайдер и примерное местоположение на карте.

## 🚀 Возможности

- 📱 Пробив по номеру телефона:
    - Определение страны и региона
    - Название оператора
    - Проверка формата и корректности номера

- 🌐 Пробив по IP-адресу:
    - Страна и город
    - Название интернет-провайдера
    - Карта примерного местоположения

- 🗂️ Логирование запросов пользователей в SQLite базу данных

## 🛠️ Стек технологий

![Python](https://img.shields.io/badge/-Python-05122A?style=flat&logo=python)
![pyTelegramBotAPI](https://img.shields.io/badge/pyTelegramBotAPI-05122A?style=flat&logo=telegram)
![phonenumbers](https://img.shields.io/badge/%F0%9F%93%9E-phonenumbers-05122A?style=flat)
![python-dotenv](https://img.shields.io/badge/%F0%9F%8C%BF-python--dotenv-05122A?style=flat)
![requests](https://img.shields.io/badge/%F0%9F%8C%90-requests-05122A?style=flat&logo=requests)
![folium](https://img.shields.io/badge/%F0%9F%97%BA-folium-05122A?style=flat)
![sqlite3](https://img.shields.io/badge/-sqlite3-05122A?style=flat&logo=sqlite)

## 📦 Установка

```bash
git clone https://github.com/finniy/IP-Tracker.git
cd IP-Tracker
pip install -r requirements.txt
```

Создай файл `.env` в корне проекта и добавь в него:

```ini
API_KEY = твой_телеграм_токен
```

## ▶️ Запуск

```bash
python main.py
```

## 🧠 Структура проекта

```
IP-Tracker/
│
├── app/
│   ├── telegram_bot.py         # Основная логика Telegram-бота
│   ├── ip_track.py             # Запросы к IP-геолокации
│   ├── phone_tracker.py        # Обработка телефонных номеров
│   ├── check_valid_ip.py       # Проверка корректности IP
│   ├── database.py             # Работа с базой данных SQLite
│   └── user_requests.db        # База данных (автоматически создаётся)
│
├── main.py                     # Точка входа
├── .env
└── README.md
```

## 📸 Примеры работы бота

<img src="images/photo1.png" width="600" style="display: block; margin: auto;">

<img src="images/photo2.png" width="600" style="display: block; margin: auto;">

## 📄 Лицензия

Проект распространяется под лицензией MIT. Свободно используй, дорабатывай и распространяй с указанием авторства.

## 👤 Автор

- GitHub: [@finniy](https://github.com/finniy)
- Telegram: [@fjnnjk](https://t.me/fjnnjk)

💌 Не забудьте поставить звезду ⭐ на GitHub, если вам понравился бот! 😉