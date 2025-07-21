import sqlite3

# Подключаемся к базе данных (создается, если не существует)
db = sqlite3.connect('user_requests.db')
cursor = db.cursor()

# Создаем таблицу пользователей, если она еще не создана
cursor.execute('''
CREATE TABLE IF NOT EXISTS users_names (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nickname TEXT,
    chat_id TEXT NOT NULL
)
''')

# Создаем таблицу с запросами пользователей, если она еще не создана
cursor.execute('''
CREATE TABLE IF NOT EXISTS request (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    user_request TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users_names (id)
)
''')

db.commit()


def add_info_in_database(chat_id_in: str, nickname: str, user_request: str) -> None:
    """
    Добавляет информацию о пользователе и его запросе в базу данных.
    Если пользователь с данным chat_id еще не существует — добавляет его.
    Затем добавляет новый запрос, связанный с этим пользователем.
    """
    db = sqlite3.connect('user_requests.db')
    cursor = db.cursor()

    # Вставляем нового пользователя, если такого chat_id еще нет в таблице
    cursor.execute('''
    INSERT INTO users_names (nickname, chat_id)
    SELECT ?, ?
    WHERE NOT EXISTS (
        SELECT 1 FROM users_names WHERE chat_id = ?
    );
    ''', (nickname, chat_id_in, chat_id_in))

    # Получаем id пользователя по chat_id
    cursor.execute('''
    SELECT id
    FROM users_names
    WHERE chat_id = ?
    ''', (chat_id_in,))

    user_id_row = cursor.fetchone()
    if user_id_row:
        user_id = user_id_row[0]
    else:
        user_id = None

    # Если пользователь найден, добавляем его запрос в таблицу request
    if user_id is not None:
        cursor.execute('''
        INSERT INTO request (user_id, user_request)
        VALUES (?, ?)
        ''', (user_id, user_request))
        db.commit()


def take_user_history(user_id: str) -> list:
    # Возвращает список с запросами пользователя
    db = sqlite3.connect('user_requests.db')
    cursor = db.cursor()

    cursor.execute('''
    SELECT user_request
    FROM request JOIN users_names ON request.user_id = users_names.id
    WHERE chat_id = ?''', (user_id,))

    rows = cursor.fetchall()
    db.close()

    lst_with_requests = [row[0] for row in rows]
    return lst_with_requests


def format_user_requests(requests: list, username: str) -> str:
    # Формирует строку с пронумерованным списком запросов для отправки одним сообщением
    if not requests:
        return f"История запросов {username} пуста."

    lines = [f"{i}. {req}" for i, req in enumerate(requests, start=1)]
    return f"История запросов {username}:\n" + "\n".join(lines)
