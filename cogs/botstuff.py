import discord
from discord.ext import commands
import traceback
import random
import asyncio

class botstuff(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['PING', 'Ping'])
    async def ping(self, ctx):
        embed = discord.Embed(title=":ping_pong: Pong!", color=discord.Color.blue())
        embed.add_field(name="Ping/Latency",
                        value=f"{round(self.bot.latency * 1000)}ms")
        await ctx.send("This command has been **deprecated**. Please use the new /ping slash command instead. If slash commands are not functional, check permissions or reauthorise the bot with this link:\n> https://discord.com/oauth2/authorize?client_id=731807331796385812&permissions=1642824466295&scope=bot%20applications.commands", embed=embed)

    @commands.command(aliases=['VOTE', 'Vote'])
    async def vote(self, ctx):
        embed = discord.Embed(title="Vote for the bot!", description="[Click here!](https://top.gg/bot/731807331796385812/vote)", color=discord.Color.blue())
        await ctx.send("This command has been **deprecated**. Please use the new /vote slash command instead. If slash commands are not functional, check permissions or reauthorise the bot with this link:\n> https://discord.com/oauth2/authorize?client_id=731807331796385812&permissions=1642824466295&scope=bot%20applications.commands", embed=embed)

    @commands.command()
    @commands.is_owner()
    async def restart(self, ctx):
        embed = discord.Embed(title="Restart", description="The bot will be restarted in 5 seconds.", color=discord.Color.red)
        await ctx.send(embed=embed)
        await asyncio.sleep(5)
        await self.bot.close()


def setup(bot):
    bot.add_cog(botstuff(bot))
