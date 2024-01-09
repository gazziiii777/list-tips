from aiogram import Bot, Dispatcher
from core.settings import settings

bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')
dp = Dispatcher()
