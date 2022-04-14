import discord, json
from discord.ext import commands
from discord.commands import \
    slash_command, Option
from discord.ext.commands import check

class Premium(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(guild_ids=[736151845730385921])
    async def addpremiumguild(self, ctx, guild_id):
        if ctx.author.id != 702385226407608341: 
            return

        with open("premium_guilds.json") as f:
            premium_guilds_list = json.load(f)

        if guild_id not in premium_guilds_list:
            premium_guilds_list.append(guild_id)

        with open("premium_guilds.json", "w+") as f:
            json.dump(premium_guilds_list, f)

        e = discord.Embed(title="Success! :white_check_mark:", description=f"Guild ID `{guild_id}` has been added to the premium list!", color=discord.Color.green())
        await ctx.respond(embed=e)

    @commands.slash_command(guild_ids=[736151845730385921])
    async def removepremiumguild(self, ctx, guild_id):
        if ctx.author.id != 702385226407608341: 
            return

        with open("premium_guilds.json") as f:
            premium_guilds_list = json.load(f)

        if guild_id in premium_guilds_list:
            premium_guilds_list.remove(guild_id)
        else:
            await ctx.respond("That guild is not in the premium list!")
            return

        with open("premium_guilds.json", "w+") as f:
            json.dump(premium_guilds_list, f)

        e = discord.Embed(title="Success! :white_check_mark:", description=f"Guild ID `{guild_id}` has been removewd from the premium list!", color=discord.Color.green())
        await ctx.respond(embed=e)

    def check_if_guild_has_premium(ctx):
        with open("premium_guilds.json") as f:
            premium_guilds_list = json.load(f)
            if str(ctx.guild.id) not in premium_guilds_list:
                return False

        return True

    @commands.slash_command(guild_ids=[736151845730385921])
    async def addpremiumuser(self, ctx, user : discord.Member):
        if ctx.author.id != 702385226407608341: #put your user id on discord here
            return

        with open("premium_users.json") as f:
            premium_users_list = json.load(f)

        if user.id not in premium_users_list:
            premium_users_list.append(user.id)

        with open("premium_users.json", "w+") as f:
            json.dump(premium_users_list, f)

        await ctx.respond(f"{user.mention} has been added!")

    @commands.slash_command(guild_ids=[736151845730385921])
    async def removepremiumuser(self, ctx, user : discord.Member):
        if ctx.author.id != 702385226407608341: #put your user id on discord here
            return

        with open("premium_users.json") as f:
            premium_users_list = json.load(f)

        if user.id in premium_users_list:
            premium_users_list.remove(user.id)
        else:
            await ctx.respond(f"{user.mention} is not in the list, so they cannot be removed!")
            return

        with open("premium_users.json", "w+") as f:
            json.dump(premium_users_list, f)

        await ctx.respond(f"{user.mention} has been removed!")

    def check_if_user_has_premium(ctx):
        with open("premium_users.json") as f:
            premium_users_list = json.load(f)
            if ctx.author.id not in premium_users_list:
                return False

        return True

    @commands.slash_command(guild_ids=[736151845730385921])
    @check(check_if_guild_has_premium)
    async def test(self, ctx):
        await ctx.respond("You have premium!")

    @test.error
    async def test_error(self, ctx, error):
        await ctx.respond("This guild is not a premium guild!")

def setup(bot):
    bot.add_cog(Premium(bot))
