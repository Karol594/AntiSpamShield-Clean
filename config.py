import os
from dotenv import load_dotenv

# .env файлынан токенді оқу
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN табылмады. .env файлын тексеріңіз немесе Fly.io secrets орнатыңыз.")

# Бот параметрлері
ADMIN_IDS = [  # Өзіңіздің telegram ID-іңізді қосыңыз
    # 123456789,
]

# Captcha параметрлері
CAPTCHA_TIMEOUT = 60  # секунд
