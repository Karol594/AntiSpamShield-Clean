import os
from telegram.ext import ApplicationBuilder
from handlers.start import register_start_handlers

BOT_TOKEN = os.environ.get("BOT_TOKEN")

application = ApplicationBuilder().token(BOT_TOKEN).build()

# Барлық хендлерлерди тіркеў
register_start_handlers(application)

# Ботты іске қосыў
application.run_polling()
