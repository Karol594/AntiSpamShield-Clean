from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

def register_start_handlers(app):
    async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
        if update.effective_chat.type == "private":
            await update.message.reply_text(
                "Сәлем! Мен AntiSpamShield ботымын. Мени топқа қосып, админ етип тағайындаңыз."
            )
        else:
            await update.message.reply_text(
                "AntiSpamShield боты іске қосылды!\nМен топтағы спам жиберүүлерди тексеруге дайынмын."
            )

    app.add_handler(CommandHandler("start", start))
