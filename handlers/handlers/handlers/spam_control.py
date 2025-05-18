python
from aiogram import Router, types, F
from aiogram.filters import ChatMemberUpdatedFilter, JOIN_TRANSITION
from loguru import logger
from utils.captcha import send_captcha, check_captcha_answer

def register_spam_handlers(router: Router):
    """
    Спам бақылау хэндлерлерін тіркеу
    """
    
    # Жаңа қатысушы қосылғанда
    @router.chat_member(ChatMemberUpdatedFilter(member_status_changed=JOIN_TRANSITION))
    async def on_user_join(event: types.ChatMemberUpdated):
        """
        Жаңа қатысушы топқа қосылғанда
        """
        chat_id = event.chat.id
        user_id = event.new_chat_member.user.id
        user_name = event.new_chat_member.user.full_name
        
        logger.info(f"Жаңа қатысушы топқа қосылды: {user_id} ({user_name}) - {chat_id}")
        
        # CAPTCHA жіберу
        await send_captcha(event.chat.id, user_id, user_name)
    
    # CAPTCHA жауабын тексеру
    @router.callback_query(F.data.startswith("captcha_"))
    async def captcha_callback(callback: types.CallbackQuery):
        """
        CAPTCHA түймесіне басқанда
        """
        await check_captcha_answer(callback)
    
    logger.info("Спам бақылау хэндлерлері тіркелді")
