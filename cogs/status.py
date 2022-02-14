import asyncio
import discord
from discord.ext import commands, tasks


class Status(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.theme_color = discord.Color.purple()
        self.status_msgs = [
            (discord.ActivityType.watching, "[guild_count] servers | >help"),
            (discord.ActivityType.listening, "Dua Lipa | >help"),
            (discord.ActivityType.watching, "Edith Revamped | >help"),
            (discord.ActivityType.watching, "for >help"),
        ]
        self.status_index = 0

    @commands.command(aliases=['enablestatus', "statusenable", 'startstatus', 'startautostatus', 'statuschange'])
    async def autostatus(self, ctx):
        owner_ids = [702385226407608341, 929270204222046249]
        if ctx.author.id in owner_ids:
            self.status_task.start()
            e = discord.Embed(title=":white_check_mark: Success!", description="Auto status change has been enabled!", color=discord.Color.green())
            await ctx.send(embed=e)
        else:
            e = discord.Embed(title=":x: You are not allowed to run this command!", color=discord.Color.red())
            await ctx.send(embed=e)

    @commands.Cog.listener()
    async def on_ready(self):
        self.status_task.start()

    def cog_unload(self):
        self.status_task.cancel()

    @tasks.loop(seconds=120)
    async def status_task(self):
        activity = self.status_msgs[self.status_index]
        activ_type = activity[0]
        activ_msg = activity[1]

        if "[guild_count]" in activ_msg:
            guild_count = len(self.bot.guilds)
            activ_msg = activ_msg.replace("[guild_count]", str(guild_count))

        activ = discord.Activity(type=activ_type, name=activ_msg)
        await self.bot.change_presence(activity=activ)

        self.status_index += 1
        if self.status_index >= len(self.status_msgs):
            self.status_index = 0

def setup(bot):
    bot.add_cog(Status(bot))