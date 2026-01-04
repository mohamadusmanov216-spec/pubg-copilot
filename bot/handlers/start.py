from aiogram import Router, types
from aiogram.filters import CommandStart

from bot.keyboards.main_menu import main_menu_keyboard

router = Router()


def register_start_handlers(dp):
    dp.include_router(router)


@router.message(CommandStart())
async def start_command(message: types.Message):
    text = (
        "Привет! Я <b>PUBG Copilot</b> — твой умный игровой ассистент.\n\n"
        "Помогу подобрать оружие, объясню тактики, разберу стиль игры и найду идеального тиммейта.\n"
        "Готов начать?"
    )

    await message.answer(text, reply_markup=main_menu_keyboard())

