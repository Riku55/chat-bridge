class Context:
    def __init__(self):
        self.telegram_bot = None
        self.discord_bot = None

    def set_telegram_bot(self, telegram_bot_instance):
        self.telegram_bot = telegram_bot_instance
    
    def get_telegram_bot(self):
        return self.telegram_bot
    
    def set_discord_bot(self, discord_bot_instance):
        self.discord_bot = discord_bot_instance

    def get_discord_bot(self):
        return self.discord_bot

context = Context()