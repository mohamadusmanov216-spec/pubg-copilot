from aiogram import Router, types
from bot.services.ai_engine import ask_gemini

router = Router()


def register_ai_handlers(dp):
    dp.include_router(router)


@router.message()
async def ai_chat(message: types.Message):
    user_text = message.text

    # Отправляем запрос в внешний ИИ (Gemini)
    try:
        answer = await ask_gemini(user_text)
    except Exception as e:
        return await message.answer(
            "⚠️ Произошла ошибка при обращении к ИИ.\n"
            "Попробуй ещё раз через пару секунд."
        )

    await message.answer(answer)

