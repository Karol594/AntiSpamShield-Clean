python
from aiogram import Router, types
from aiogram.filters import Command
from loguru import logger

def register_start_handlers(router: Router):
    """
    /start командасы үшін хэндлер тіркеу
    """
    
    @router.message(Command("start"))
    async def cmd_start(message: types.Message):
        """
        /start командасын өңдеу
        """
        if message.chat.type == "private":
            # Жеке чатта
            await message.answer(
                "Сәлем! Мен AntiSpamShield ботымын. "
                "Мені топқа қосып, админ етіп тағайындаңыз. "
                "Мен топта спам жіберушілерден қорғаймын."
            )
            logger.info(f"Жеке чатта /start командасы: {message.from_user.id}")
        else:
            # Топта
            await message.answer(
                "AntiSpamShield боты іске қосылды! "
                "Мен топтағы спам жіберушілерді тексеруге дайынмын."
            )
            logger.info(f"Топта /start командасы: {message.chat.id}")
    
    logger.info("Start хэндлерлері тіркелді")
