import asyncio
import config
from context import context

async def discord_message_handler(author, message):
    print(f"Received discord message from {author}: {message}")
    new_message = f"Discord/{author}: {message}"
    await asyncio.gather(send_telegram_message(new_message), send_irc_message(new_message))

async def telegram_message_handler(author, message):
    print(f"Received telegram message from {author}: {message}")
    new_message = f"Telegram/{author}: {message}"
    await asyncio.gather(send_discord_message(new_message), send_irc_message(new_message))

async def irc_message_handler(author, message):
    print(f"Received irc message from {author}: {message}")
    new_message = f"IRC/{author}: {message}"
    await asyncio.gather(send_telegram_message(new_message), send_discord_message(new_message))


async def send_discord_message(message):
    channel = context.get_discord_bot().get_channel(config.DISCORD_CHANNEL_ID)
    await channel.send(message)

async def send_telegram_message(message):
    await context.get_telegram_bot().send_message(config.TELEGRAM_GROUP_CHAT_ID, message)

async def send_irc_message(message):
    context.get_irc_bot().send_message(message)
