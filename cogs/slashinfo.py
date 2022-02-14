from unicodedata import name
import discord
import traceback
import random
import datetime
from discord.ext import commands
from discord.commands import \
    slash_command

class SlashInfo(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.slash_command(name="avatar", description="Check a users avatar")
    async def avatar(self, ctx, *,  member: discord.Member):
        userAvatarUrl = member.avatar
        embed=discord.Embed(title=f'{member} avatar!')
        embed.set_image(url=member.avatar)
        await ctx.respond(embed=embed)
        print(member.avatar.url)

    @commands.slash_command(name="channelinfo", description="Get info about a channel")
    async def channelinfo(self,ctx,channel:discord.TextChannel):
        nsfw = self.bot.get_channel(channel.id).is_nsfw()
        embed = discord.Embed(title = 'Channel Infromation: ' + str(channel),
        colour = discord.Colour.from_rgb(54, 151, 255))
        embed.add_field(name = 'Channel Name: ', value = str(channel.name))
        embed.add_field(name = "Channel's NSFW Status: ", value = str(nsfw))
        embed.add_field(name = "Channel's id: " , value = str(channel.id))
        embed.add_field(name = 'Channel Created At: ', value = str(channel.created_at.strftime("%a, %d %B %Y, %I:%M %p UTC")))
        embed.add_field(name = 'Channel Type: ', value = str(channel.type))
        await ctx.respond(embed = embed)

    @commands.slash_command(name="serverinfo", description="Get info about a server")
    async def serverinfo(self, ctx):
            findbots = sum(1 for member in ctx.guild.members if member.bot)
            embed = discord.Embed(title = 'Infomation about ' + ctx.guild.name + '.', colour = discord.Colour.from_rgb(54,151,255))
            embed.set_thumbnail(url = str(ctx.guild.icon))
            embed.add_field(name = "Guild's name: ", value = ctx.guild.name)
            embed.add_field(name = "Guild's owner: ", value = str(ctx.guild.owner))
            embed.add_field(name = "Guild's verification level: ", value = str(ctx.guild.verification_level))
            embed.add_field(name = "Guild's id: ", value = str(ctx.guild.id))
            embed.add_field(name = "Guild's member count: ", value = str(ctx.guild.member_count))
            embed.add_field(name="Bots", value=findbots, inline=True)
            embed.add_field(name = "Guild created at: ", value = str(ctx.guild.created_at.strftime("%a, %d %B %Y, %I:%M %p UTC")))
            await ctx.respond(embed =  embed)

    @commands.slash_command(name="userinfo", description="Get info about a user")
    async def userinfo(self,ctx, member: discord.Member):
        roles = [role for role in member.roles]
        embed = discord.Embed(color=member.color, timestamp=datetime.datetime.utcnow())
        embed.set_author(name=f"{member}", icon_url=member.avatar.url)
        embed.set_thumbnail(url=member.avatar.url)
        embed.add_field(name="Joined at:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p"))
        embed.add_field(name='Registered at:', value=member.created_at.strftime('%a, %#d %B %Y, %I:%M %p'))
        embed.add_field(name='Bot?', value=f'{member.bot}')
        embed.add_field(name='Status?', value=f'{member.status}')
        embed.add_field(name='Top Role?', value=f'{member.top_role}')
        embed.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles[:1]]))
        embed.set_footer(icon_url=member.avatar.url, text=f'Requested By: {ctx.author.name}')
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(SlashInfo(bot))