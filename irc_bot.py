import asyncio
import irc.bot
import irc.strings
import config
import threading
from context import context
from message_handler import irc_message_handler

class MyIRCBot(irc.bot.SingleServerIRCBot):
    def __init__(self, server, port, channel, nickname, loop):
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port)], nickname, nickname)
        self.channel = channel
        self.loop = loop

    def on_welcome(self, connection, event):
        print(f"IRC bot is connected")
        connection.join(self.channel)

    def on_pubmsg(self, connection, event):
        self.handle_message(event, self.loop)

    def handle_message(self, event, loop):

        if event.target != config.IRC_CHANNEL:
            return

        author = event.source.nick
        message = event.arguments[0]

        asyncio.run_coroutine_threadsafe(irc_message_handler(author, message), loop)


    def send_message(self, message):
        self.connection.privmsg(self.channel, message)

def run_irc_bot(loop):

    server = config.IRC_SERVER
    port = config.IRC_PORT
    channel = config.IRC_CHANNEL
    nickname = "chat_bridge"

    bot = MyIRCBot(server, port, channel, nickname, loop)
    context.set_irc_bot(bot)
    bot.start()

def start_irc_in_thread(loop):
    irc_thread = threading.Thread(target=run_irc_bot, args=(loop,), daemon=True)
    irc_thread.start()