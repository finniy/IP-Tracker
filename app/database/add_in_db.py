import sqlite3


def add_info_in_database(chat_id_in: str, nickname: str, user_request: str) -> None:
    """
    Добавляет информацию о пользователе и его запросе в базу данных.
    Если пользователь с данным chat_id еще не существует — добавляет его.
    Затем добавляет новый запрос, связанный с этим пользователем.
    """
    db = sqlite3.connect('../user_requests.db')
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
