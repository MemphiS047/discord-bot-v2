import discord
import configparse
from discord.ext import commands
from load import load_conf

class Hal(commands.Bot):
    """
    This class contains MAIN parts to raise the bot up and running
    """
    conf = {}
    
    def __init__(self):
        """
        On init cogs are loaded  from ./cogs dir. and 
        config loaded as well. super() initialization done 
        """
        self.conf = load_conf()    
        super().__init__(command_prefix=self.prefix, case_insensitive=True)

    def run(self):
        """
        Loads conf then runs the bot
        """        
        TOKEN = self.conf["TOKEN"]
        print("Running bot...")
        super().run(TOKEN, reconnect=True)

    async def on_ready(self):
        """
        On Bot ready this function fires with intializing
        client id to self
        """
        self.client_id = (await self.application_info()).id
        print(f"Bot ready. {self.client_id}")

    async def prefix(self, bot, msg): 
        """
        Command prefix to invoke cogs (commands)
        """
        return commands.when_mentioned_or("!")(bot, msg)

    async def process_commands(self, msg): 
        ctx = await self.get_context(msg, cls=commands.Context)
        if ctx.command is not None:
            await self.invoke(ctx)

    async def on_message(self, msg):
        if not msg.author.bot:
            await self.process_commands(msg)