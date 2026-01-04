from aiogram import Router, types
from aiogram.filters import CommandStart

from bot.keyboards.main_menu import main_menu_keyboard

router = Router()


def register_start_handlers(dp):
    dp.include_router(router)


@router.message(CommandStart())
async def start_command(message: types.Message):
    await message.answer(
        "Привет! Я <b>PUBG Copilot</b> — твой игровой ассистент по PUBG.\n\n"
        "Используй меню ниже, чтобы выбрать раздел.",
        reply_markup=main_menu_keyboard(),
    )
