import random
from aiogram.filters import Command
from aiogram.types import Message
from core.dispatcher import dp
from core.keyboards import start_keyboard
from core.admin_panel.admin_commands import cmd_admin  # Подключение админ панели
from core.handlers.callback import main_menu  # Подключил callback`и


@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer_sticker('CAACAgIAAxkBAAECxlllndCLYnENOYhrsQrmhxcx842mHgACJxYAAoJHGEhG_o_W8MthbjQE')
    await message.answer(
        "Приветсвенное сообщение",
        reply_markup=start_keyboard.keyboard,
    )


@dp.message()
async def send_echo(message: Message):
    await message.answer(
        text='Я даже представить себе не могу, '
             'что ты имеешь в виду :(\n\n'
             'Чтобы получить какую-нибудь шутку - '
             'отправь команду /joke'
    )
