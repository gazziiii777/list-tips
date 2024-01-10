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





# Создаем объект инлайн-клавиатуры
admin_keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
