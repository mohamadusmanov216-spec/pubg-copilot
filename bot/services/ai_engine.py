import os
import aiohttp

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

SYSTEM_PROMPT = (
    "Ты — PUBG Copilot, умный игровой ассистент. "
    "Отвечай структурировано, дружелюбно и профессионально, как Microsoft Copilot. "
    "Ты эксперт по PUBG Mobile: оружие, карты, тактики, титулы, сенса, ротации, механики. "
    "Давай советы, основанные на реальных механиках игры. "
    "Не используй токсичность. Не пиши лишнего. "
    "Отвечай понятно и полезно."
)


async def ask_gemini(prompt: str) -> str:
    """
    Отправляет запрос в Google Gemini и возвращает ответ.
    """

    url = (
        "https://generativelanguage.googleapis.com/v1beta/models/"
        "gemini-pro:generateContent?key=" + GEMINI_API_KEY
    )

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": SYSTEM_PROMPT},
                    {"text": prompt}
                ]
            }
        ]
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=payload) as resp:
            data = await resp.json()

            # Ошибка API
            if "error" in data:
                return "⚠️ Ошибка при обращении к ИИ. Попробуй позже."

            # Ответ модели
            try:
                return data["candidates"][0]["content"]["parts"][0]["text"]
            except:
                return "⚠️ Не удалось получить ответ от ИИ."

