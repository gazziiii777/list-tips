from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state, State, StatesGroup
from aiogram.types import CallbackQuery

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


# Cоздаем класс StatesGroup для нашей машины состояний
class FSMFillForm(StatesGroup):
    # Создаем экземпляры класса State, последовательно
    # перечисляя возможные состояния, в которых будет находиться
    # бот в разные моменты взаимодействия с пользователем
    fill_name = State()  # Состояние ожидания ввода имени
    fill_age = State()  # Состояние ожидания ввода возраста
    fill_gender = State()  # Состояние ожидания выбора пола
    upload_photo = State()  # Состояние ожидания загрузки фото
    fill_education = State()  # Состояние ожидания выбора образования
    fill_wish_news = State()  # Состояние ожидания выбора получать ли новости


@dp.callback_query(F.data == "contact_the_admin")
async def contact_the_admin(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(
        text="ривет если ты хочешь написать письмо адмиину указать свою проблему",
    )
    # Устанавливаем состояние ожидания ввода имени
    await state.set_state(FSMFillForm.fill_name)
