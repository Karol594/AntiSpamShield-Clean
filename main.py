import os
from telegram.ext import ApplicationBuilder

BOT_TOKEN = os.environ.get("BOT_TOKEN")

application = ApplicationBuilder().token(BOT_TOKEN).build()

application.run_polling()
