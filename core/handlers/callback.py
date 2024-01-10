from aiogram import F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state, State, StatesGroup
from aiogram.types import CallbackQuery, Message

from core.dispatcher import dp
from core.keyboards import main_menu_keyboard, disk_keyboard, my_photo_and_video_keyboard


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


@dp.callback_query(F.data == "disk")
async def disk(callback: CallbackQuery):
    # После нажатия на кнопку текст меняется
    await callback.message.edit_text(
        text="ривет если ты хочешь написать письмо адмиину указать свою проблему",
        reply_markup=disk_keyboard.keyboard
    )


@dp.callback_query(F.data == "my_photo_and_video")
async def disk(callback: CallbackQuery):
    # После нажатия на кнопку текст меняется
    await callback.message.edit_text(
        text="ривет если ты хочешь написать письмо адмиину указать свою проблему",
        reply_markup=my_photo_and_video_keyboard.carousel
    )


# Создаем "базу данных" пользователей
user_dict: dict[int, dict[str, str | int | bool]] = {}


# Cоздаем класс StatesGroup для нашей машины состояний
class FSMContact(StatesGroup):
    # Создаем экземпляры класса State, последовательно
    # перечисляя возможные состояния, в которых будет находиться
    # бот в разные моменты взаимодействия с пользователем
    message_for_admin = State()  # Состояние ожидания ввода имени


@dp.callback_query(F.data == "contact_the_admin")
async def contact_the_admin(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(
        text="Привет, тут ты можешь связаться с админом, для отмены напиши /cancel",
    )
    # Устанавливаем состояние ожидания ввода имени
    await state.set_state(FSMContact.message_for_admin)
