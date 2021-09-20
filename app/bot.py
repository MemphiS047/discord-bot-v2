import discord
import configparser
from discord.ext import commands
from pathlib import Path
from cogs.test import Greetings

class Hal(commands.Bot):
    """
    This class contains MAIN parts to raise the bot up and running
    """
    _conf = {}
    
    def __init__(self):
      """
      On init cogs are loaded  from ./cogs dir. and 
      config loaded as well. super() initialization done 
      """
      self.load_config()    
      self.setup()
      super().__init__(command_prefix=self.prefix, case_insensitive=True)

    def load_config(self):
      """
      Loads configs for credentials and other things...
      """
      print("Loading config...")
      cfg = configparser.ConfigParser()
      cfg.read("../dontneedit.ini")
      self._conf["TOKEN"] = cfg["Discord"]["TOKEN"]
    
    def setup(self):
      """
      Loads cogs to bot
      """
      self.load_extension("cogs.test")

    def run(self):
      """
      Loads conf then runs the bot
      """        
      TOKEN = self._conf["TOKEN"]
      print("Running bot...")
      super().run(TOKEN, reconnect=True)
    
    async def shutdown(self):
      """
      Closing bot 
      """
      print("Closing connection...")
      await super().close
    
    async def close(self):
      """
      Closing but on keyboard interrupt
      """
      print("Closing on keyboard interrupt...")
      await self.shutdown()
    
    async def on_connect(self):
      """
      Information about connection trigered on connection
      """
      print(f"\n\nConnected to Discord (latency: {self.latency*1000:,.0f} ms.)")
    
    async def on_resume(self):
      """
      Trigered on resume prints a message about current status
      """
      print("Bot resumed.")
    
    async def on_disconnect(self):
      """
      Fired on bot disconnect print message about status
      """
      print("Bot disconnect.")
    
    async def on_ready(self):
      """
      On Bot ready this function fires with intializing
      client id to self
      """
      print(f'Logged in as: {self.user.name} - {self.user.id}\nVersion: {discord.__version__}\n')

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
          print(msg.content)