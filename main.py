python
import asyncio
import logging
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from bot import setup_bot
from loguru import logger

# Логгер орнату
logger.add("bot.log", rotation="1 MB", level="INFO")
logging.basicConfig(level=logging.INFO)

async def main():
    # Бот инициализациясы
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    
    # Хэндлерлерді тіркеу
    setup_bot(dp)
    
    # Бот стартын логтау
    logger.info("AntiSpamShield бот іске қосылды!")
    
    # Бот запуск
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
