import config

from discord.ext import commands

DESCRIPTION = '''Blitzcrank Bot is a Discord bot written by Frosty ☃#5263 to pull various statsitics
               from Riot's API for a given summoner. All commands should be prefixed with 'b!'
               (for example, b!search)'''

STARTUP_EXTENSIONS = ['utilities', 'summoner_stats', 'static_data', 'default_regions', 'reload',
                      'events']


class BlitzcrankBot(commands.AutoShardedBot):
    """Main"""

    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned_or('b!'), description=DESCRIPTION)
        self.bot_token = config.TOKEN
        self.api_key = config.API

        for extension in STARTUP_EXTENSIONS:
            try:
                self.load_extension(extension)
            except Exception as exception:
                exc = '{}: {}'.format(type(exception).__name__, exception)
                print('Failed to load extension {}\n{}'.format(extension, exc))

    async def on_message(self, message):
        pass

    def run(self):
        super().run(self.bot_token, reconnect=True)


if __name__ == '__main__':
    BlitzcrankBot().run()

# Base finished
