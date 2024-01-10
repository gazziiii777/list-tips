from core.db.questions.settings_db import *


async def questions_add_db(data_message_for_admin):
    # Создание таблицы, если она не существует
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS your_table_name (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            message_text TEXT,
            username TEXT,
            answer BOOLEAN
        )
    ''')

    # Сохранение изменений в базе данных
    conn.commit()

    # Получение данных из state
    user_id = data_message_for_admin.get('id')
    message_text = data_message_for_admin.get('text')
    username = data_message_for_admin.get('username')
    answer = data_message_for_admin.get('answer')

    if user_id is not None and message_text is not None:
        # Вставка данных в базу данных
        cursor.execute('''
            INSERT INTO your_table_name (user_id, message_text, username, answer)
            VALUES (?, ?, ?, ?)
        ''', (user_id, message_text, username, answer))

        # Сохранение изменений в базе данных
        conn.commit()

    conn.close()
