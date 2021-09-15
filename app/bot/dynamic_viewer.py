import discord
from discord.ext import commands

class LolCogs(commands.Cogs):
  def __init__(self, bot):
    self.bot = bot
  
  @commands.command(name="lolbuild")
  async def lolbuild_command(self, ctx):
    channel = ctx.message.channel
    messages = await channel.history(limit=1).flatten()
    print(messages)