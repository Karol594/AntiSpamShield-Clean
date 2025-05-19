import asyncio
import logging
import os
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from bot import setup_bot
from loguru import logger
from aiohttp import web

# Логгер орнату
logger.add("bot.log", rotation="1 MB", level="INFO")
logging.basicConfig(level=logging.INFO)

async def main():
    # Бот инициализациясы
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    
    # Хэндлерлерді тіркеу
    setup_bot(dp)
    
    # Веб-сервер инициализациясы для Fly.io
    app = web.Application()
    
    async def health_check(request):
        return web.Response(text="Bot is running")
    
    app.router.add_get("/", health_check)
    
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', 8080)
    await site.start()
    
    logger.info("AntiSpamShield бот іске қосылды!")
    logger.info("Веб-сервер іске қосылды: http://0.0.0.0:8080")
    
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
