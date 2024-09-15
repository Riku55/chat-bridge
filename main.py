import asyncio
from discord_bot import run_discord_bot
from telegram_bot import run_telegram_bot

async def main():

    discord_task = asyncio.create_task(run_discord_bot())
    telegram_task = asyncio.create_task(run_telegram_bot())
    
    await asyncio.gather(discord_task, telegram_task)

if __name__ == "__main__":
    asyncio.run(main())
