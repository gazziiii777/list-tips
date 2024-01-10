from aiogram import F

from core.dispatcher import dp
from aiogram.types import CallbackQuery


@dp.callback_query(F.data == "not_now")
async def not_now(callback: CallbackQuery):
    # Высплывающее окошко
    await callback.answer()
    await callback.message.delete()
