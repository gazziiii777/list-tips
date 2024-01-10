import asyncio
import logging
from core.handlers.basic import get_start
from core.settings import settings
from core.dispatcher import bot
from core.admin_panel.commands_admin import cmd_admin  # Подключение админ панели
from core.admin_panel.callback_admin import not_now
from core.handlers.commands import *  # Ипорт всех команд


async def start_bot():
    await bot.send_message(chat_id=settings.bots.admin_id, text='Бот запущен')


async def stop_bot():
    await bot.send_message(chat_id=settings.bots.admin_id, text='Бот остановлен')


async def main():
    logging.basicConfig(level=logging.INFO, filename="bot_log.log", filemode="w",
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
