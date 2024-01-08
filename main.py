import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from core.handlers.basic import get_start
from core.settings import settings

bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')

dp = Dispatcher()


async def start_bot():
    await bot.send_message(chat_id=settings.bots.admin_id, text='Бот запущен')


async def stop_bot():
    await bot.send_message(chat_id=settings.bots.admin_id, text='Бот остановлен')


async def main():
    logging.basicConfig(level=logging.INFO, filename="log.log", filemode="w",
                        format="%(asctime)s %(levelname)s %(message)s")

    dp.startup.register(start_bot)  # Отправляет сообщение админу когда бот запускается
    dp.shutdown.register(stop_bot)  # Отправляет сообщение админу когда бот останавлявается
    dp.message.register(get_start)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())
