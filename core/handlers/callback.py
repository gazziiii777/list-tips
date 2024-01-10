from aiogram import F
from aiogram.types import CallbackQuery
from core.dispatcher import dp
from core.keyboards import main_menu_keyboard, contact_the_admin_keyboard


@dp.callback_query(F.data == "main_menu")
async def main_menu(callback: CallbackQuery):
    # Высплывающее окошко
    await callback.answer(
        text="кайфарик марик тут типо тоже текст",
        show_alert=True
    )
    # После нажатия на кнопку текст меняется
    await callback.message.edit_text(
        text="типо главное меню",
        reply_markup=main_menu_keyboard.keyboard
    )


@dp.callback_query(F.data == "contact_the_admin")
async def contact_the_admin(callback: CallbackQuery):
    # После нажатия на кнопку текст меняется
    await callback.message.edit_text(
        text="ривет если ты хочешь написать письмо адмиину указать свою проблему",
        reply_markup=contact_the_admin_keyboard.keyboard
    )
