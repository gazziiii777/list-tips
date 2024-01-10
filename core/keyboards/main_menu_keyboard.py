from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Создаем объекты инлайн-кнопок
buttons_1 = [
    [
        InlineKeyboardButton(text='Мой диск', callback_data='disk')
    ],
    [
        InlineKeyboardButton(text='Документация Telegram Bot API', url='https://core.telegram.org/bots/api')
    ],
    [
        InlineKeyboardButton(text='Работа', callback_data='work')
    ],
    [
        InlineKeyboardButton(text='Связь с админом', callback_data='contact_the_admin')
    ],
]

buttons_2 = [
    [
        InlineKeyboardButton(text='Назад', callback_data='main_menu')
    ],
]

# Создаем объект инлайн-клавиатуры
keyboard = InlineKeyboardMarkup(inline_keyboard=buttons_1)
back = InlineKeyboardMarkup(inline_keyboard=buttons_2)
