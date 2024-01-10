from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Создаем объекты инлайн-кнопок
buttons_1 = [
    [
        InlineKeyboardButton(text="Рассылка всем пользователям бота", callback_data="distribution_bot")
    ],
    [
        InlineKeyboardButton(text='Вопросы', callback_data="send_questions")
    ],
    [
        InlineKeyboardButton(text='Прислать логи', callback_data="send_logs")
    ],
    [
        InlineKeyboardButton(text='Прислать все бд', callback_data="send_db")
    ],
]

buttons_2 = [
    [
        InlineKeyboardButton(text="Ответить пользователю", callback_data="send_answer")
    ],
    [
        InlineKeyboardButton(text="Потом", callback_data="not_now")
    ],
    [
        InlineKeyboardButton(text="Удалить вопрос", callback_data="delete_question")
    ],
]

# Создаем объект инлайн-клавиатуры
admin_keyboard = InlineKeyboardMarkup(inline_keyboard=buttons_1)
admin_answer = InlineKeyboardMarkup(inline_keyboard=buttons_2)
