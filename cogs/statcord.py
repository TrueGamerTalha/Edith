from discord.ext import commands
import statcord
import os

statcordkey = os.getenv("STAT_CORD_KEY")

class StatCord(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.key = statcordkey
        self.api = statcord.Client(self.bot,self.key)
        self.api.start_loop()

    @commands.Cog.listener()
    async def on_command(self,ctx):
        self.api.command_run(ctx)

def setup(bot):
    bot.add_cog(StatCord(bot))