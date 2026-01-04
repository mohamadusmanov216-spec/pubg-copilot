from aiogram import Router, types
from aiogram.filters import Text

from bot.services.nickname_engine import generate_nicknames

router = Router()


def register_nickname_handlers(dp):
    dp.include_router(router)


@router.message(Text("🎭 Генератор никнеймов"))
async def nickname_start(message: types.Message):
    await message.answer(
        "🎭 <b>Генератор никнеймов</b>\n\n"
        "Напиши тему или стиль ника.\n"
        "Примеры:\n"
        "• агрессивный\n"
        "• аниме\n"
        "• PUBG стиль\n"
        "• минимализм\n"
        "• арабский стиль\n"
        "• киберспорт\n"
    )


@router.message()
async def nickname_generate(message: types.Message):
    style = message.text

    # Генерация 10 вариантов
    nicknames = generate_nicknames(style)

    formatted = "\n".join([f"• {n}" for n in nicknames])

    await message.answer(
        f"🎭 <b>Никнеймы в стиле:</b> {style}\n\n{formatted}\n\n"
        "Хочешь ещё? Напиши новый стиль."
    )

