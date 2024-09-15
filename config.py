import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_API_ID = os.getenv('TELEGRAM_API_ID')
TELEGRAM_API_HASH = os.getenv('TELEGRAM_API_HASH')
TELEGRAM_BOT_TOKEN = os.getenv('BOTFATHER_TELEGTRAM_TOKEN')
TELEGRAM_GROUP_CHAT_ID = int(os.getenv('TELEGRAM_GROUP_CHAT_ID'))

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
DISCORD_CHANNEL_ID = int(os.getenv('DISCORD_CHANNEL_ID'))
