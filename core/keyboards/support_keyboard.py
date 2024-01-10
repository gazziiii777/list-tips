from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Создаем объекты инлайн-кнопок
buttons = [
    [
        InlineKeyboardButton(text="Отправить", callback_data="send_the_support")
    ],
    [
        InlineKeyboardButton(text='Переписать', callback_data="support")
    ],
]

# Создаем объект инлайн-клавиатуры
keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
