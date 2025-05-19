from aiogram import Dispatcher, Router
from loguru import logger
from handlers.start import register_start_handlers
from handlers.spam_control import register_spam_handlers

def setup_bot(dp: Dispatcher):
    """
    Барлық хэндлерлерді тіркеу
    """
    # Бос роутер жасау
    router = Router()
    
    # Хэндлерлерді тіркеу
    register_start_handlers(router)
    register_spam_handlers(router)
    
    # Роутерді диспетчерге қосу
    dp.include_router(router)
    
    logger.info("Бот хэндлерлері тіркелді")
    
    return dp
