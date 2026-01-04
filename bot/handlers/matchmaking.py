from aiogram import Router, types
from aiogram import F

from bot.keyboards.matchmaking_menu import matchmaking_keyboard
from bot.database.matchmaking import (
    create_profile,
    get_profile,
    update_profile,
    add_to_queue,
    remove_from_queue,
    find_match
)

router = Router()


def register_matchmaking_handlers(dp):
    dp.include_router(router)


# Открыть меню матчмейкинга
@router.message(F.text == "👥 Поиск тиммейтов")
async def open_matchmaking(message: types.Message):
    await message.answer(
        "👥 <b>Поиск тиммейтов</b>\n\n"
        "Заполни профиль и начни поиск.",
        reply_markup=matchmaking_keyboard()
    )


# Заполнить профиль
@router.message(F.text == "📝 Заполнить профиль")
async def fill_profile(message: types.Message):
    await message.answer(
        "📝 Введи свой игровой стиль, ранг, устройство и уровень игры.\n\n"
        "Пример:\n"
        "Агрессивный, Ас, iPhone 13, опыт 3 года"
    )
    message.bot['awaiting_profile'] = message.from_user.id


# Обработка профиля
@router.message()
async def save_profile(message: types.Message):
    bot_state = message.bot.get('awaiting_profile')

    if bot_state == message.from_user.id:
        text = message.text

        if get_profile(message.from_user.id):
            update_profile(message.from_user.id, text)
        else:
            create_profile(message.from_user.id, text)

        message.bot['awaiting_profile'] = None

        return await message.answer(
            "✅ Профиль сохранён!\n"
            "Теперь можешь начать поиск.",
            reply_markup=matchmaking_keyboard()
        )


# Начать поиск
@router.message(F.text == "🔍 Начать поиск")
async def start_search(message: types.Message):
    profile = get_profile(message.from_user.id)

    if not profile:
        return await message.answer(
            "⚠️ Сначала заполни профиль.",
            reply_markup=matchmaking_keyboard()
        )

    add_to_queue(message.from_user.id)

    await message.answer("⏳ Ищу подходящего тиммейта…")

    match = find_match(message.from_user.id)

    if match:
        user1, user2 = match

        remove_from_queue(user1)
        remove_from_queue(user2)

        await message.bot.send_message(
            user1,
            f"🎉 <b>Тиммейт найден!</b>\n\n"
            f"ID: <code>{user2}</code>\n"
            f"Напиши ему!"
        )

        await message.bot.send_message(
            user2,
            f"🎉 <b>Тиммейт найден!</b>\n\n"
            f"ID: <code>{user1}</code>\n"
            f"Напиши ему!"
        )


# Остановить поиск
@router.message(F.text == "⛔ Остановить поиск")
async def stop_search(message: types.Message):
    remove_from_queue(message.from_user.id)
    await message.answer("⛔ Поиск остановлен.", reply_markup=matchmaking_keyboard())


# Мой профиль
@router.message(F.text == "👤 Мой профиль")
async def my_profile(message: types.Message):
    profile = get_profile(message.from_user.id)

    if not profile:
        return await message.answer("У тебя ещё нет профиля.")

    await message.answer(
        f"👤 <b>Твой профиль:</b>\n\n{profile}"
    )

