from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_menu_keyboard():
    keyboard = [
        [KeyboardButton(text="🎮 Советы по PUBG")],
        [KeyboardButton(text="🔫 Подбор оружия")],
        [KeyboardButton(text="🗺 Тактики по картам")],
        [KeyboardButton(text="🤖 ИИ-чат")],
        [KeyboardButton(text="👥 Поиск тиммейтов")],
        [KeyboardButton(text="🎭 Генератор никнеймов")],
    ]

    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
        input_field_placeholder="Выбери действие…"
    )

