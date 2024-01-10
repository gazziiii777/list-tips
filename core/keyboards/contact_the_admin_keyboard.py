from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Создаем объекты инлайн-кнопок
buttons = [
    [
        InlineKeyboardButton(text="Отправить", callback_data="send_the_admin")
    ],
    [
        InlineKeyboardButton(text='Переписать', callback_data="contact_the_admin")
    ],
]

# Создаем объект инлайн-клавиатуры
keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
