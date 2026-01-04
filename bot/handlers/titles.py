from aiogram import Router, types
from aiogram.filters import Text

from bot.services.titles_engine import get_title_info

router = Router()


def register_titles_handlers(dp):
    dp.include_router(router)


@router.message(Text("🏆 Титулы PUBG"))
async def titles_start(message: types.Message):
    await message.answer(
        "🏆 <b>Титулы PUBG</b>\n\n"
        "Напиши название титула, и я объясню:\n"
        "• условия получения\n"
        "• скрытые требования\n"
        "• советы\n"
        "• быстрые способы выполнения\n\n"
        "Примеры:\n"
        "• Weapon Master\n"
        "• Commando\n"
        "• Overachiever\n"
        "• Collector\n"
        "• Sharpshooter\n"
        "• Maxed Out\n"
    )


@router.message()
async def title_info(message: types.Message):
    title_name = message.text.strip()

    info = get_title_info(title_name)

    if not info:
        return await message.answer(
            "❓ Я не нашёл такой титул.\n"
            "Попробуй написать точнее.\n\n"
            "Например:\n"
            "• Weapon Master\n"
            "• Commando\n"
            "• Collector\n"
            "• Sharpshooter\n"
        )

    await message.answer(info)

