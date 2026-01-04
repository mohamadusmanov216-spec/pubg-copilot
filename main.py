import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from config import BOT_TOKEN

# Импортируем хендлеры
from bot.handlers.start import register_start_handlers
from bot.handlers.menu import register_menu_handlers
from bot.handlers.advice import register_advice_handlers
from bot.handlers.weapons import register_weapon_handlers
from bot.handlers.maps import register_map_handlers
from bot.handlers.ai_chat import register_ai_handlers
from bot.handlers.matchmaking import register_matchmaking_handlers
from bot.handlers.nicknames import register_nickname_handlers


async def main():
    bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()

    # Регистрируем хендлеры
    register_start_handlers(dp)
    register_menu_handlers(dp)
    register_advice_handlers(dp)
    register_weapon_handlers(dp)
    register_map_handlers(dp)
    register_ai_handlers(dp)
    register_matchmaking_handlers(dp)
    register_nickname_handlers(dp)

    print("Bot started...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

