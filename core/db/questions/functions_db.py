import sqlite3


async def questions_add_db(data_message_for_admin):
    conn = sqlite3.connect('core/db/databases/questions.db')
    cursor = conn.cursor()

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


async def delete_question_from_db(question_info):
    # Подключение к базе данных SQLite
    conn = sqlite3.connect('core/db/databases/questions.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM your_table_name WHERE user_id = ? AND message_text = ?',
                   (question_info.get('id'), question_info.get('text')))

    # Сохранение изменений в базе данных
    conn.commit()

    conn.close()
