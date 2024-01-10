from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Создаем объекты инлайн-кнопок
buttons = [
    [
        InlineKeyboardButton(text='Прочитал', callback_data="main_menu")
    ],
]

# Создаем объект инлайн-клавиатуры
keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)