import discord
import json
import os
import datetime
import traceback
import random
import asyncio
from discord.ext import commands

class Mod(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['Lock', "LOCK"])
    @commands.has_permissions(manage_channels=True)
    async def lock(self, ctx, amount=1):
        await ctx.channel.purge(limit=amount)
        await ctx.message.channel.set_permissions(ctx.guild.default_role, send_messages=False)
        embed = discord.Embed(title=f"{ctx.channel.name} has been locked!", description="You will gain access again once the lockdown is lifted.", color=discord.Color.dark_red())
        await ctx.send("This command has been **deprecated**. There is no slash command for this command. If slash commands are not functional, check permissions or reauthorise the bot with this link:\n> https://discord.com/oauth2/authorize?client_id=731807331796385812&permissions=1642824466295&scope=bot%20applications.commands", embed=embed)
    
    @commands.command(aliases=['Unlock', 'UNLOCK'])
    @commands.has_permissions(manage_channels=True)
    async def unlock(self, ctx, amount=1):
        await ctx.channel.purge(limit=amount)
        await ctx.message.channel.set_permissions(ctx.guild.default_role, send_messages=True)
        embed = discord.Embed(title=f"{ctx.channel.name} has been unlocked!", description="Everyone now has access to this channel.", color=discord.Color.green())
        await ctx.send("This command has been **deprecated**. There is no slash command for this command. If slash commands are not functional, check permissions or reauthorise the bot with this link:\n> https://discord.com/oauth2/authorize?client_id=731807331796385812&permissions=1642824466295&scope=bot%20applications.commands", embed=embed)

    @commands.command(aliases=['Clear', 'CLEAR'])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        await ctx.message.delete()
        await ctx.channel.purge(limit=amount)
        e = discord.Embed(title=f"{amount} message have been cleared! :white_check_mark:", color=discord.Color.green())
        await ctx.send("This command has been **deprecated**. Please use the new /clear slash command instead. If slash commands are not functional, check permissions or reauthorise the bot with this link:\n> https://discord.com/oauth2/authorize?client_id=731807331796385812&permissions=1642824466295&scope=bot%20applications.commands", embed=e, delete_after=5)

    @commands.command(aliases=['Slowmode', 'SlowMode', 'SLOWMODE'])
    async def slowmode(self, ctx, time: int):
        try:
            if time == 0:
                embed = discord.Embed(title='Slowmode turned off', color=discord.Color.green())
                await ctx.send("This command has been **deprecated**. Please use the new /slowmode slash command instead. If slash commands are not functional, check permissions or reauthorise the bot with this link:\n> https://discord.com/oauth2/authorize?client_id=731807331796385812&permissions=1642824466295&scope=bot%20applications.commands", embed=embed)
                await ctx.channel.edit(slowmode_delay=0)
            elif time > 21600:
                embed = discord.Embed(
                    title='You cannot have a slowmode above 6hrs.', color=discord.Color.red())
                await ctx.send("This command has been **deprecated**. Please use the new /slowmode slash command instead. If slash commands are not functional, check permissions or reauthorise the bot with this link:\n> https://discord.com/oauth2/authorize?client_id=731807331796385812&permissions=1642824466295&scope=bot%20applications.commands", embed=embed)
            else:
                await ctx.channel.edit(slowmode_delay=time)
                embed = discord.Embed(title=f'Slowmode set to {time} seconds.', color=discord.Color.green())
                await ctx.send("This command has been **deprecated**. Please use the new /slowmode slash command instead. If slash commands are not functional, check permissions or reauthorise the bot with this link:\n> https://discord.com/oauth2/authorize?client_id=731807331796385812&permissions=1642824466295&scope=bot%20applications.commands", embed=embed)
        except Exception:
            traceback.print_exc()

    @commands.command(aliases=['Softban', 'SOFTBAN'])
    async def softban(self, ctx, member: discord.Member, *, reason='No reason provided'):
        await member.ban(reason=reason)
        await member.unban(reason=reason)
        embed = discord.Embed(title=f':white_check_mark: Successfully softbanned {member}!', color=discord.Color.green())
        await ctx.send(embed=embed)

    @commands.command(aliases=['Ban', 'BAN'])
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason):
        await member.ban(reason=reason)
        em = discord.Embed(title=f'{member} has been banned!', color=discord.Color.green())
        await ctx.send("This command has been **deprecated**. Please use the new /ban slash command instead. If slash commands are not functional, check permissions or reauthorise the bot with this link:\n> https://discord.com/oauth2/authorize?client_id=731807331796385812&permissions=1642824466295&scope=bot%20applications.commands", embed=em)

        embed = discord.Embed(
            title=f'You have been banned from {ctx.guild.name}', description=f'Banned by {member}', color=discord.Color.red())
        embed.add_field(name='Reason:', value=f'{reason}')
        await member.send(embed=embed)

    @commands.command(aliases=['Unban', 'UNBAN'])
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                em = discord.Embed(title=f':white_check_mark: {user.mention} has been unbanned!', color=discord.Color.green())
                await ctx.send("This command has been **deprecated**. Please use the new /unban slash command instead. If slash commands are not functional, check permissions or reauthorise the bot with this link:\n> https://discord.com/oauth2/authorize?client_id=731807331796385812&permissions=1642824466295&scope=bot%20applications.commands", embed=em)
                return

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member = None, *, reason='No reason provided'):
        if not member:
            em = discord.Embed(title=':x: Please specify a member.', color=discord.Color.red())
            await ctx.send(embed=em)
            return
        await member.kick()
        em = discord.Embed(title=f':white_check_mark: {member} has been kicked!', color=discord.Color.green())
        await ctx.send(embed=em)
        embed = discord.Embed(
            title=f'You have been kicked from {ctx.guild.name}', description=f'Kicked by {member}', color=discord.Color.red())
        embed.add_field(name='Reason:', value=f'{reason}')
        await member.send("This command has been **deprecated**. Please use the new /kick slash command instead. If slash commands are not functional, check permissions or reauthorise the bot with this link:\n> https://discord.com/oauth2/authorize?client_id=731807331796385812&permissions=1642824466295&scope=bot%20applications.commands", embed=embed)

    @commands.command(aliases=['Warn', 'WARN'])
    @commands.has_permissions(kick_members=True)
    async def warn(self, ctx, member: discord.Member, *, reason="No reason Provided"):
        with open('warnings.json', 'r') as f:
            warns = json.load(f)
        if str(ctx.guild.id) not in warns:
            warns[str(ctx.guild.id)] = {}
        if str(member.id) not in warns[str(ctx.guild.id)]:
            warns[str(ctx.guild.id)][str(member.id)] = {}
            warns[str(ctx.guild.id)][str(member.id)]["warns"] = 1
            warns[str(ctx.guild.id)][str(member.id)]["warnings"] = [reason]
        else:
            warns[str(ctx.guild.id)][str(member.id)]["warnings"].append(reason)
        with open('warnings.json', 'w') as f:
            json.dump(warns, f)
            e = discord.Embed(title=f":white_check_mark: {member} has been warned for {reason}!", color=discord.Color.green())
            await ctx.send(embed=e)
            embed = discord.Embed(
                title=f'You have been warned in {ctx.guild.name} ', description=f'You received a warning from {ctx.author}', color=discord.Color.red())
            embed.add_field(name='Reason:', value=f'{reason}')
            await member.send("This command has been **deprecated**. Please use the new /warn slash command instead. If slash commands are not functional, check permissions or reauthorise the bot with this link:\n> https://discord.com/oauth2/authorize?client_id=731807331796385812&permissions=1642824466295&scope=bot%20applications.commands", embed=embed)

    @commands.command()
    @commands.has_permissions(manage_guild=True)
    async def removewarn(self, ctx, member: discord.Member, num: int, *, reason='No reason provided.'):
        with open('warnings.json', 'r') as f:
            warns = json.load(f)

        num -= 1
        warns[str(ctx.guild.id)][str(member.id)]["warns"] -= 1
        warns[str(ctx.guild.id)][str(member.id)]["warnings"].pop(num)
        with open('warnings.json', 'w') as f:
            json.dump(warns, f)
            e = discord.Embed(title=f":white_check_mark: Warn for {member} has been removed!", color=discord.Color.green())
            await ctx.send(embed=e)
            embed = discord.Embed(
                title=f'Your warn in {ctx.guild.name} been removed', description=f'Your warning was removed by {ctx.author}', color=discord.Color.green())
            await member.send("This command has been **deprecated**. Please use the new /removewarn slash command instead. If slash commands are not functional, check permissions or reauthorise the bot with this link:\n> https://discord.com/oauth2/authorize?client_id=731807331796385812&permissions=1642824466295&scope=bot%20applications.commands", embed=embed)

    @commands.command(aliases=['Warns', 'WARNS'])
    @commands.has_permissions(manage_messages=True)
    async def warns(self, ctx, member: discord.Member):
        with open('warnings.json', 'r') as f:
            warns = json.load(f)

        num = 1
        warnings = discord.Embed(title=f"{member}\'s warns", color=discord.Color.green())
        for warn in warns[str(ctx.guild.id)][str(member.id)]["warnings"]:
            warnings.add_field(name=f"Warn {num}", value=warn)
            num += 1
        await ctx.send("This command has been **deprecated**. Please use the new /warns slash command instead. If slash commands are not functional, check permissions or reauthorise the bot with this link:\n> https://discord.com/oauth2/authorize?client_id=731807331796385812&permissions=1642824466295&scope=bot%20applications.commands", embed=warnings)

def setup(bot):
    bot.add_cog(Mod(bot))
