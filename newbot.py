import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix=".")

@bot.event
async def on_ready():
    print("Ready")


bot.load_extension("cogs.slashfun")

bot.run("NzM4NjQzODUwNTA3MDU5MjI0.XyO5sQ.GL1xaVNkrlYRfaXPh5U9pPsxzYg")