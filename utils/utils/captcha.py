from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder
import random
from loguru import logger
from config import CAPTCHA_TIMEOUT

# CAPTCHA жауаптарын уақытша сақтау
captcha_answers = {}

async def send_captcha(chat_id: int, user_id: int, user_name: str, bot: types.Bot):
    """
    Қатысушыға CAPTCHA жіберу
    """
    # CAPTCHA генерациясы (қарапайым мысал)
    answers = ["🍎", "🍐", "🍊", "🍋", "🍌", "🍉", "🍇", "🍓"]
    correct_answer = random.choice(answers)

    # CAPTCHA жауабын сақтау
    captcha_answers[user_id] = correct_answer

    # CAPTCHA түймелерін жасау
    builder = InlineKeyboardBuilder()
    options = random.sample(answers, 4)
    if correct_answer not in options:
        options[0] = correct_answer
        random.shuffle(options)

    for option in options:
        builder.button(text=option, callback_data=f"captcha_{option}")
    builder.adjust(2, 2)

    # CAPTCHA хабарламасын жіберу
    await bot.send_message(
        chat_id,
        f"Сәлем, {user_name}! Роботтар бізге керек емес.\n"
        f"Төмендегі жемістер ішінен {correct_answer} таңдаңыз. "
        f"Сізде {CAPTCHA_TIMEOUT} секунд бар.",
        reply_markup=builder.as_markup()
    )

    logger.info(f"Қатысушыға CAPTCHA жіберілді: {user_id} - {correct_answer}")

async def check_captcha_answer(callback: types.CallbackQuery):
    """
    CAPTCHA жауабын тексеру
    """
    user_id = callback.from_user.id
    selected_option = callback.data.split("_")[1]

    if user_id not in captcha_answers:
        await callback.answer("CAPTCHA табылмады немесе мерзімі өтті.", show_alert=True)
        return

    correct_answer = captcha_answers[user_id]

    if selected_option == correct_answer:
        # Дұрыс жауап
        await callback.message.edit_text(
            f"CAPTCHA сәтті өтті! Қош келдіңіз, {callback.from_user.full_name}!"
        )
        logger.info(f"Қатысушы CAPTCHA-ны дұрыс шешті: {user_id}")
    else:
        # Қате жауап
        await callback.message.edit_text("Қате жауап. Сіз блокталдыңыз.")

        # Қатысушыны топтан шығару
        chat_id = callback.message.chat.id
        bot = callback.bot
        await bot.ban_chat_member(chat_id, user_id)

        logger.warning(f"Қатысушы CAPTCHA-дан өте алмады: {user_id}")

    # CAPTCHA жауабын тазалау
    del captcha_answers[user_id]

    await callback.answer()