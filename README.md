# 🔍 IP-Tracker — Telegram бот для пробива IP и телефонов

**IP-Tracker** — это Telegram-бот, который позволяет быстро получить информацию об IP-адресе или номере телефона:
страна, город, провайдер и примерное местоположение на карте.

---

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

---

## 🛠️ Стек технологий

![Python](https://img.shields.io/badge/-Python-05122A?style=flat&logo=python)
![sqlite3](https://img.shields.io/badge/-sqlite3-05122A?style=flat&logo=sqlite)
![requests](https://img.shields.io/badge/%F0%9F%8C%90-requests-05122A?style=flat&logo=requests)
![pyTelegramBotAPI](https://img.shields.io/badge/pyTelegramBotAPI-05122A?style=flat&logo=telegram)
![phonenumbers](https://img.shields.io/badge/%F0%9F%93%9E-phonenumbers-05122A?style=flat)
![folium](https://img.shields.io/badge/%F0%9F%97%BA-folium-05122A?style=flat)
![logger](https://img.shields.io/badge/%E2%9A%A0-logger-05122A?style=flat&logo=logging)
![python-dotenv](https://img.shields.io/badge/%F0%9F%8C%BF-python--dotenv-05122A?style=flat)

---

## 📦 Установка

### 1. Клонирование репозитория

```bash
git clone https://https://github.com/finniy/IP-Tracker.git
cd IP-Tracker
```

### 2. Создание виртуального окружения (рекомендуется)

```bash
python -m venv venv
```

### 3. Активация виртуального окружения

**Windows:**

```bash
venv\Scripts\activate
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

### 4. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 5. Запуск бота

```bash
python app/main.py
```

---

## 🧠 Структура проекта

```
IP-Tracker/
├── .env.template
├── main.py
├── requirements.txt
│
├── app/
│ ├── init.py
│ ├── bot_instance.py
│ ├── config.py
│ ├── logger.py
│ ├── telegram_bot.py
│
│ ├── database/
│ │ ├── init.py
│ │ ├── add_in_db.py
│ │ ├── create_db.py
│ │ └── take_db.py
│
│ ├── handlers/
│ │ ├── init.py
│ │ ├── history_handler.py
│ │ ├── ip_handler.py
│ │ ├── phone_handler.py
│ │ └── start_handler.py
│
│ ├── messages/
│ │ ├── init.py
│ │ └── message_text.py
│
│ ├── trackers/
│ │ ├── init.py
│ │ ├── ip_track.py
│ │ └── phone_track.py
│
│ ├── utils/
│ │ ├── init.py
│ │ ├── check_valid_ip.py
│ │ ├── format_requests.py
│ │ ├── send_map.py
│ │ ├── work_with_json.py
│ │ └── phone_codes.json
│
├── images/
│ ├── Photo1.png
│ └── Photo2.png

```

## 📸 Примеры работы бота

<img src="images/Photo1.png" width="600" style="display: block; margin: auto;">

<img src="images/Photo2.png" width="600" style="display: block; margin: auto;">

## 📄 Лицензия

Проект распространяется под лицензией MIT. Свободно используй, дорабатывай и распространяй с указанием авторства.

---

## 👤 Автор

- GitHub: [@finniy](https://github.com/finniy)
- Telegram: [@fjnnjk](https://t.me/fjnnjk)

💌 Не забудьте поставить звезду ⭐ на GitHub, если вам понравился бот! 😉