from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Создаем объекты инлайн-кнопок
buttons_1 = [
    [
        InlineKeyboardButton(text='◀️', callback_data='disk'),
        InlineKeyboardButton(text='▶️', url='https://core.telegram.org/bots/api')

    ],
    [
        InlineKeyboardButton(text='Назад', callback_data='disk')
    ],
]

# Создаем объект инлайн-клавиатуры
carousel = InlineKeyboardMarkup(inline_keyboard=buttons_1)
