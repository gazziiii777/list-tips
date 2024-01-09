from aiogram.filters import Command
from aiogram.types import Message
from core.dispatcher import dp


@dp.message(Command("hello"))
async def cmd_hello(message: Message):
    await message.answer(
        f"Hello, <b>{message.from_user.full_name}</b>",
    )
