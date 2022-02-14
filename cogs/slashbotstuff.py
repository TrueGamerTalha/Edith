import discord
from discord.ext import commands
from discord.commands import \
    slash_command
import traceback
import random
import asyncio

class SlashBotStuff(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="ping", description="Check the bots ping")
    async def ping(self, ctx):
        embed = discord.Embed(title=":ping_pong: Pong!", color=discord.Color.blue())
        embed.add_field(name="Ping/Latency",
                        value=f"{round(self.bot.latency * 1000)}ms")
        await ctx.send(embed=embed)

    @commands.slash_command(name="vote", description="Vote for the bot")
    async def vote(self, ctx):
        embed = discord.Embed(title="Vote for the bot!", description="[Click here!](https://top.gg/bot/731807331796385812/vote)", color=discord.Color.blue())
        await ctx.send(embed=embed)

    # @commands.command()
    # @commands.is_owner()
    # async def restart(self, ctx):
    #     embed = discord.Embed(title="Restart", description="The bot will be restarted in 5 seconds.", color=discord.Color.red)
    #     await ctx.send(embed=embed)
    #     await asyncio.sleep(5)
    #     await self.bot.close()


def setup(bot):
    bot.add_cog(SlashBotStuff(bot))
