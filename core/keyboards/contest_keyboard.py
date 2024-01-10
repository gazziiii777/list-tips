from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Создаем объекты инлайн-кнопок
buttons = [
    [
        InlineKeyboardButton(text="Учасвсвую", callback_data="contest")
    ],
    [
        InlineKeyboardButton(text='Документация Telegram Bot API', url='https://core.telegram.org/bots/api')
    ],
]

# Создаем объект инлайн-клавиатуры
keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
