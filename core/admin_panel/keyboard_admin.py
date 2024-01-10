from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Создаем объекты инлайн-кнопок
buttons_1 = [
    [
        InlineKeyboardButton(text="Рассылка всем пользователям бота", callback_data="distribution_bot")
    ],
    [
        InlineKeyboardButton(text='Документация Telegram Bot API', url='https://core.telegram.org/bots/api')
    ],
]

buttons_2 = [
    [
        InlineKeyboardButton(text="Ответить пользователю", callback_data="send_answer")
    ],
    [
        InlineKeyboardButton(text="Потом", callback_data="not_now")
    ],
]

# Создаем объект инлайн-клавиатуры
admin_keyboard = InlineKeyboardMarkup(inline_keyboard=buttons_1)
admin_answer = InlineKeyboardMarkup(inline_keyboard=buttons_2)
