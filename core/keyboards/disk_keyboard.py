from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Создаем объекты инлайн-кнопок
buttons = [
    [
        InlineKeyboardButton(text='Файлы', callback_data='my_files')
    ],
    [
        InlineKeyboardButton(text='Фото и видео', callback_data='my_photo_and_video')
    ],
    [
        InlineKeyboardButton(text='Ссылки', callback_data='my_links')
    ],
    [
        InlineKeyboardButton(text='Уведомления', callback_data='my_notifications')
    ],
    [
        InlineKeyboardButton(text='Дни рождения', callback_data='hb_days')
    ],
    [
        InlineKeyboardButton(text='Назад', callback_data='main_menu')
    ],
]

# Создаем объект инлайн-клавиатуры
keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
