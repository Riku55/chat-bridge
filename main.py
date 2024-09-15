import asyncio
from discord_bot import run_discord_bot
from telegram_bot import run_telegram_bot
from irc_bot import start_irc_in_thread

async def main():

    loop = asyncio.get_running_loop()

    discord_task = asyncio.create_task(run_discord_bot())
    telegram_task = asyncio.create_task(run_telegram_bot())

    start_irc_in_thread(loop)
    
    await asyncio.gather(discord_task, telegram_task)

if __name__ == "__main__":
    asyncio.run(main())
