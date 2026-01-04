from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def matchmaking_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📝 Заполнить профиль")],
            [KeyboardButton(text="🔍 Начать поиск")],
            [KeyboardButton(text="⛔ Остановить поиск")],
            [KeyboardButton(text="👤 Мой профиль")],
        ],
        resize_keyboard=True
    )
