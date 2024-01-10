from core.dispatcher import dp
from aiogram.filters import Command
from aiogram.types import Message
from core.settings import settings
from core.admin_panel.keyboard_admin import admin_keyboard  # Клавиатура для администратора


@dp.message(Command('admin'))
async def cmd_admin(message: Message):
    if message.from_user.id == settings.bots.admin_id:
        await message.answer(
            "Админ панель",
            reply_markup=admin_keyboard,
        )
