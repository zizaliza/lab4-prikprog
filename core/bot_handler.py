from aiogram import Bot
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup

from core.api import CityAPI

class BotHandlers:

    def __init__(self, bot: Bot, api: CityAPI):
        self.bot = bot
        self.api = api  

    async def start(self, message: Message):
        keyboard = [
            [KeyboardButton(text='Случайный город'), ]
        ]
        markup = ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True) 
        await message.answer(
            "Напишите название любого города, чтобы получить информацию!",
            reply_markup=markup
        )

    async def get_random_city(self, message: Message):
        city_info = self.api.fetch_random_city()
        if city_info:
            await message.answer(
                f"🏙 Город {city_info.name}!\n\n"
                f"🌍 Этот город расположен в стране {city_info.country}.\n\n"
                f"👀 \n[🌐 Карта города]({city_info.maps_url})\n\n"
                f"📚 Важность: {city_info.importance} 🚀",
                disable_web_page_preview=False
            )
        else:
            await message.answer("Не удалось получить информацию о случайном городе. Попробуйте позже.")

    async def get_city_or_country_info(self, message: Message):
        city_name = message.text
        city_info = self.api.fetch_city_info(city_name)
        if city_info:
            await message.answer(
                f"🌆 Город {city_info.name}!\n\n"
                f"🌍 Это один из городов страны {city_info.country}.\n\n"
                f"🗺 Карта города, чтобы узнать, где он находится:\n[🌐 Карта города]({city_info.maps_url})\n\n"
                f"📚 Важность: {city_info.importance} 🚀",
                disable_web_page_preview=False
            )
        else:
            await message.answer("Не удалось найти информацию о городе. Проверьте написание и попробуйте снова.")
