from aiogram import Bot, types


async def get_start(message: types.Message, bot: Bot):
    print(message.chat.id)
    await bot.send_message(message.chat.id, text=message.text)
    # await bot.send_message(chat_id=585296404, text=message.text)
    # await message.answer(text=message.text)
