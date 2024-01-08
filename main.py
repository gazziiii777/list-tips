import asyncio
import logging
from aiogram import Bot, Dispatcher, types

BOT_TOKEN = ''

bot = Bot(token=BOT_TOKEN, parse_mode='HTML')

dp = Dispatcher()


async def start_bot():
    await bot.send_message(chat_id='', text='Бот запущен')


async def stop_bot():
    await bot.send_message(chat_id='', text='Бот остановлен')


async def main():
    logging.basicConfig(level=logging.INFO, filename="log.log", filemode="w",
                        format="%(asctime)s %(levelname)s %(message)s")

    dp.startup.register(start_bot)  # Отправляет сообщение админу когда бот запускается
    dp.shutdown.register(start_bot)  # Отправляет сообщение админу когда бот останавлявается
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())
