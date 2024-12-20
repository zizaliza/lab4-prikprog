import asyncio
import os
from aiogram import F, Bot, Dispatcher
from aiogram.filters import CommandStart
from dotenv import load_dotenv

from core.api import CityAPI
from core.bot_handler import BotHandlers


load_dotenv()
TOKEN = os.getenv("TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN не найден в .env файле")

dp = Dispatcher()

async def main() -> None:

    bot = Bot(token=TOKEN)

    api = CityAPI()
    handlers = BotHandlers(bot, api)

    dp.message.register(handlers.start, CommandStart())
    dp.message.register(handlers.get_random_city, F.text == 'Случайный город')
    dp.message.register(handlers.get_city_or_country_info, F.text != 'Случайный город')

    await dp.start_polling(bot)

if __name__ == "__main__":
    print("bot started")
    asyncio.run(main())