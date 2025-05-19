import os
from telegram.ext import ApplicationBuilder

BOT_TOKEN = os.getenv("BOT_TOKEN")  # ENV ішинен оқыйды

application = ApplicationBuilder().token(BOT_TOKEN).build()
