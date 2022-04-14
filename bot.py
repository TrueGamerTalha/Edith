from colorama import Fore, Back, Style
import pyfiglet
import datetime
import time
import pytz


ascii_text = pyfiglet.figlet_format("Edith")
print(Fore.YELLOW)
print(ascii_text)

current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata')) 
time.sleep(2)
print(Fore.YELLOW + f"[{current_time.month}/{current_time.day}/{current_time.year} {current_time.hour}:{current_time.minute}:{current_time.second}] " + Fore.BLUE + f"[INFO] Starting bot with version " + Fore.GREEN + "2.0.0b1")
current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
time.sleep(2)
print(Fore.YELLOW + f"[{current_time.month}/{current_time.day}/{current_time.year} {current_time.hour}:{current_time.minute}:{current_time.second}] " + Fore.BLUE + f"[LOADER] Loaded " + Fore.GREEN + f"7 " + Fore.BLUE + "events!")
current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata')) 
time.sleep(2)
print(Fore.YELLOW + f"[{current_time.month}/{current_time.day}/{current_time.year} {current_time.hour}:{current_time.minute}:{current_time.second}] " + Fore.BLUE + f"[LOADER] Loaded " + Fore.GREEN + f"36 " + Fore.BLUE + "commands!")
current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata')) 
time.sleep(1)
#print(Fore.YELLOW + f"[{current_time.month}/{current_time.day}/{current_time.year} {current_time.hour}:{current_time.minute}:{current_time.second}] " + Fore.BLUE + f"[LOADER] Loaded " + Fore.GREEN + f"36 " + Fore.BLUE + "commands!")
import discord
from discord.ext import commands, tasks
import os
import json
import ast
import dotenv
import asyncio
import humanize
from datetime import datetime, timedelta
from discord.commands import \
    slash_command
import topgg
from dotenv import load_dotenv
from dbl import dbl_token

load_dotenv()
token = os.getenv("token")
os.chdir("./")

intents = discord.Intents.all()
bot = commands.AutoShardedBot(shard_count = 5, command_prefix="", intents = intents)
bot.remove_command('help')

for filename in os.listdir('./cogs'):
	if filename.endswith(".py"):
		bot.load_extension(f'cogs.{filename[:-3]}')

owner_ids = [702385226407608341, 929270204222046249]
bot.blacklisted_users = []
bot.topggpy = topgg.DBLClient(bot, dbl_token, autopost=True, post_shard_count=True)

# @bot.event
# async def on_connect():
#     print('Connected to Discord')
#     await bot.change_presence(activity=discord.Activity(name=f"Bot is starting", url="https://www.twitch.tv/neilisop", type=discord.ActivityType.streaming))

@bot.event
async def on_autopost_success():
    print(f"{Fore.BLUE} Posted server count {Fore.GREEN}{bot.topggpy.guild_count}{Fore.BLUE}, shard count {Fore.GREEN}{bot.shard_count}{Fore.BLUE}")

@tasks.loop(hours=1)
async def syncguilds():
    with open("prefix.json", "r") as f:
        prefixes = json.load(f)
    for i in bot.guilds:
        if str(i.id) not in prefixes:
            prefixes[str(i.id)] = ">"
            current_time = datetime.now(pytz.timezone('Asia/Kolkata')) 
            print(Fore.YELLOW + f"[{current_time.month}/{current_time.day}/{current_time.year} {current_time.hour}:{current_time.minute}:{current_time.second}] " + Fore.BLUE + "[Non-prefixed guild checker] Detected a guild that is non-prefixed. Adding " + Fore.GREEN + f"{i}" + Fore.BLUE + " to prefix list.")
    with open("prefix.json", "w") as f:
        json.dump(prefixes, f, indent=4)

@bot.slash_command(name="botinfo", description="Shows info about Edith")
async def botinfo(ctx):
    guild_count = str(len(bot.guilds))
    total_member_count = 0
    ping = int(bot.latency * 1000)

    for guild in bot.guilds:
        total_member_count += guild.member_count
    now = datetime.now()
    uptime = launched_at - now
    humanized_time = humanize.precisedelta(uptime)
    shard_id = ctx.guild.shard_id
    shard_servers = len([guild for guild in bot.guilds if guild.shard_id == shard_id])

    embed = discord.Embed(title="Statistics:", 
    description=f"**Username:** Edith\n**Discriminator:** 1574\n**Servers:** {guild_count}\n**Users:** {total_member_count}\n**Bot Version:** 2.0 \n**Uptime:** {humanized_time}\n**Client Status:**`🟢 Online` - `{ping}`\n**Library:** Discord.py - `{discord.__version__}`\n\n**Shard info**\nShard ID: {shard_id}\nShard servers: {shard_servers}\n\n\n:warning: **We've shifted to Slash Commands! All Normal commands will not work from 1 March 12:00PM IST. If the Slash Commands don't appear, please reinvite the bot with this link: https://discord.com/oauth2/authorize?client_id=731807331796385812&permissions=1642824466295&scope=bot%20applications.commands. **",
    color=discord.Color.blue())
    embed.set_thumbnail(url=bot.user.avatar)
    await ctx.respond(embed=embed)

@bot.command()
async def botinfo(ctx):
    guild_count = str(len(bot.guilds))
    total_member_count = 0
    ping = int(bot.latency * 1000)

    for guild in bot.guilds:
        total_member_count += guild.member_count
    now = datetime.now()
    uptime = launched_at - now
    humanized_time = humanize.precisedelta(uptime)

    embed = discord.Embed(title="Statistics:", 
    description=f"**Username:** Edith\n**Discriminator:** 1574\n**Servers:** {guild_count}\n**Users:** {total_member_count}\n**Bot Version:** 2.0 \n**Uptime:** {humanized_time}\n**Client Status:**`🟢 Online` - `{ping}`\n**Library:** Discord.py - `{discord.__version__}`\n\n\n:warning: **We've shifted to Slash Commands! All Normal commands will not work from 1 March 12:00PM IST. If the Slash Commands don't appear, please reinvite the bot with this link: https://discord.com/oauth2/authorize?client_id=731807331796385812&permissions=1642824466295&scope=bot%20applications.commands. **",
    color=discord.Color.blue())
    embed.set_thumbnail(url=bot.user.avatar)
    await ctx.send(embed=embed)

@bot.command()
async def enable(ctx, extension):
    if ctx.author.id in owner_ids:
        bot.load_extension(f'cogs.{extension}')
        e = discord.Embed(title=f":white_check_mark: Succesfully enabled **{extension}**", color=discord.Color.green())
        await ctx.send(embed=e)
    else:
        e = discord.Embed(title=":x: You are not allowed to run this command!", color=discord.Color.red())
        await ctx.send(embed=e)

@bot.command()
async def disable(ctx, extension):
    if ctx.author.id in owner_ids:
        bot.unload_extension(f'cogs.{extension}')
        e = discord.Embed(title=f":white_check_mark: Succesfully disabled **{extension}**", color=discord.Color.green())
        await ctx.send(embed=e)
    else:
        e = discord.Embed(title=":x: You are not allowed to run this command!", color=discord.Color.red())
        await ctx.send(embed=e)

@bot.command()
async def reload(ctx, extension):
    if ctx.author.id in owner_ids:
        bot.unload_extension(f'cogs.{extension}')
        bot.load_extension(f'cogs.{extension}')
        e = discord.Embed(title=f":white_check_mark: Succesfully reloaded **{extension}**", color=discord.Color.green())
        await ctx.send(embed=e)
    else:
        e = discord.Embed(title=":x: You are not allowed to run this command!", color=discord.Color.red())
        await ctx.send(embed=e)

def insert_returns(body):
    # insert return stmt if the last expression is a expression statement
    if isinstance(body[-1], ast.Expr):
        body[-1] = ast.Return(body[-1].value)
        ast.fix_missing_locations(body[-1])

    # for if statements, we insert returns into the body and the orelse
    if isinstance(body[-1], ast.If):
        insert_returns(body[-1].body)
        insert_returns(body[-1].orelse)

    # for with blocks, again we insert returns into the body
    if isinstance(body[-1], ast.With):
        insert_returns(body[-1].body)

@bot.slash_command(name="blacklist", description="Blacklist a user from using the bot!")
async def blacklist(ctx, user: discord.Member):
    if ctx.author.id in owner_ids:
        bot.blacklisted_users.append(user.id)
        data = read_json(blacklist)
        data["blacklistedUsers"].append(user.id)
        write_json(data, "blacklist")
        e = discord.Embed(title="Success! :white_check_mark:", description=f"{ctx.author.name} has been blacklisted!", color=discord.Color.green())
        await ctx.respond(embed=e)
        channel = bot.get_channel(845180373612494889)
        embed = discord.Embed(title="Owner Command used!", color=ctx.author.color)
        embed.add_field(name="Command", value="blacklist", inline=False)
        embed.add_field(name="By", value=f" {ctx.author.name}", inline=False)
        embed.add_field(name="In guild", value=f" {ctx.guild.name}", inline=False)
        await channel.send(embed=embed)
    else:
        e = discord.Embed(title=":x: You are not allowed to run this command!", color=discord.Color.red())
        await ctx.respond(embed=e)

@bot.slash_command(name="unblacklist", description="UnBlacklist a member from using the bot!")
async def unblacklist(ctx, user: discord.Member):
    if ctx.author.id in owner_ids:
        bot.blacklisted_users.remove(user.id)
        data = read_json("blacklist")
        data["blacklistedUsers"].remove(user.id)
        write_json(data, "blacklist")
        e = discord.Embed(title="Success! :white_check_mark:", description=f"{ctx.author.name} has been unblacklisted!", color=discord.Color.green())
        await ctx.respond(embed=e)
        channel = bot.get_channel(845180373612494889)
        embed = discord.Embed(title="New Command used!", color=ctx.author.color)
        embed.add_field(name="Command", value="unblacklist", inline=False)
        embed.add_field(name="By", value=f" {ctx.author.name}", inline=False)
        embed.add_field(name="In guild", value=f" {ctx.guild.name}", inline=False)
        await channel.send(embed=embed)
    else:
        e = discord.Embed(title=":x: You are not allowed to run this command!", color=discord.Color.red())
        await ctx.respond(embed=e)

"""Custom Prefix stuff"""

@bot.event
async def on_guild_join(guild):
    channel = bot.get_channel(936237231436365834)
    e = discord.Embed(title="New Guild!")
    e.add_field(name="Guild Name", value=f"**{guild.name}**", inline=False)
    e.add_field(name="Guild ID", value=f"**{guild.id}**", inline=False)
    await channel.send(embed=e)

@bot.event
async def on_guild_remove(guild):
    channel = bot.get_channel(936237231436365834)
    e = discord.Embed(title="Left Guild!")
    e.add_field(name="Guild Name", value=f"**{guild.name}**")
    await channel.send(embed=e)

"""Blacklist Stuff"""

@bot.event
async def on_shard_ready(shard_id):
    current_time = datetime.now(pytz.timezone('Asia/Kolkata'))
    print(Fore.YELLOW + f"[{current_time.month}/{current_time.day}/{current_time.year} {current_time.hour}:{current_time.minute}:{current_time.second}] " + Fore.BLUE + f"[INFO] Shard" + Fore.YELLOW + f" {shard_id} " + Fore.BLUE + "has logged in!")
    data = read_json("blacklist")
    bot.blacklisted_users = data["blacklistedUsers"]
    global launched_at
    launched_at = datetime.now()
    print(Fore.RED)
    if shard_id == 0:
        syncguilds.start()
    else:
        pass

@bot.event
async def on_message(message):
    if message.author.id == bot.user.id:
        return
    if message.author.id in bot.blacklisted_users:
        return
	
    await bot.process_commands(message)

"""Error stuff"""

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        embed= discord.Embed(title="Slow Down :raised_back_of_hand:", color=discord.Color.red())
        embed.add_field(name="This command is on cooldown!", value="Use this command again in  {:.2f}s".format(error.retry_after), inline=False)
        await ctx.respond(embed=embed)
    elif isinstance(error,commands.CheckFailure):
        em = discord.Embed(title="No permission :x:", description="You don't have enough permission(s) to execute that command!", color=discord.Color.red())
        await ctx.respond(embed=em)
    else:
        print(error)

"""Helper Functions"""

@bot.command()
async def setstatus(ctx, type, *, status):
    if ctx.author.id in owner_ids:
        if type == "streaming":
            e = discord.Embed(title="Stopping auto-status change events", color=discord.Color.red())
            msg = await ctx.send(embed=e)
            await asyncio.sleep(3)
            bot.unload_extension("cogs.status")
            statusstopped = discord.Embed(title="Auto-Status change has been stopped!", color=discord.Color.orange())
            await msg.edit(embed=statusstopped)
            await asyncio.sleep(2)
            await bot.change_presence(activity=discord.Activity(name=f"{status}", url="https://www.twitch.tv/neilisop", type=discord.ActivityType.streaming))
            statuschanged = discord.Embed(title="Bot status has been changed!", color=discord.Color.green())
            await msg.edit(embed=statuschanged)
        elif type == "playing":
            e = discord.Embed(title="Stopping auto-status change events", color=discord.Color.red())
            msg = await ctx.send(embed=e)
            await asyncio.sleep(3)
            bot.unload_extension("cogs.status")
            statusstopped = discord.Embed(title="Auto-Status change has been stopped!", color=discord.Color.orange())
            await msg.edit(embed=statusstopped)
            await asyncio.sleep(2)
            await bot.change_presence(activity=discord.Activity(name=f"{status}", type=discord.ActivityType.playing))
            statuschanged = discord.Embed(title="Bot status has been changed!", color=discord.Color.green())
            await msg.edit(embed=statuschanged)
        elif type == "listening":
            e = discord.Embed(title="Stopping auto-status change events", color=discord.Color.red())
            msg = await ctx.send(embed=e)
            await asyncio.sleep(3)
            bot.unload_extension("cogs.status")
            statusstopped = discord.Embed(title="Auto-Status change has been stopped!", color=discord.Color.orange())
            await msg.edit(embed=statusstopped)
            await asyncio.sleep(2)
            await bot.change_presence(activity=discord.Activity(name=f"{status}", type=discord.ActivityType.listening))
            statuschanged = discord.Embed(title="Bot status has been changed!", color=discord.Color.green())
            await msg.edit(embed=statuschanged)
        elif type == "watching":
            e = discord.Embed(title="Stopping auto-status change events", color=discord.Color.red())
            msg = await ctx.send(embed=e)
            await asyncio.sleep(3)
            bot.unload_extension("cogs.status")
            statusstopped = discord.Embed(title="Auto-Status change has been stopped!", color=discord.Color.orange())
            await msg.edit(embed=statusstopped)
            await asyncio.sleep(2)
            await bot.change_presence(activity=discord.Activity(name=f"{status}", type=discord.ActivityType.watching))
            statuschanged = discord.Embed(title="Bot status has been changed!", color=discord.Color.green())
            await msg.edit(embed=statuschanged)
        else:
            error = discord.Embed(title=":x: Error!", description="You must provide a status type and status value.\n**Syntax**\n`>setstatus listening dua lipa`", color=discord.Color.red())
            await ctx.respond(embed=error)
    else:
        e = discord.Embed(title=":x: You are not allowed to run this command!", color=discord.Color.red())
        await ctx.respond(embed=e)

@bot.slash_command(name="setstatus", description="Set the bots status to something!")
async def setstatus(ctx, type, *, status):
    if ctx.author.id in owner_ids:
        if type == "streaming":
            e = discord.Embed(title="Stopping auto-status change events", color=discord.Color.red())
            msg = await ctx.respond(embed=e)
            await asyncio.sleep(3)
            bot.unload_extension("cogs.status")
            statusstopped = discord.Embed(title="Auto-Status change has been stopped!", color=discord.Color.orange())
            await msg.edit(embed=statusstopped)
            await asyncio.sleep(2)
            await bot.change_presence(activity=discord.Activity(name=f"{status}", url="https://www.twitch.tv/neilisop", type=discord.ActivityType.streaming))
            statuschanged = discord.Embed(title="Bot status has been changed!", color=discord.Color.green())
            await msg.edit(embed=statuschanged)
        elif type == "playing":
            e = discord.Embed(title="Stopping auto-status change events", color=discord.Color.red())
            msg = await ctx.respond(embed=e)
            await asyncio.sleep(3)
            bot.unload_extension("cogs.status")
            statusstopped = discord.Embed(title="Auto-Status change has been stopped!", color=discord.Color.orange())
            await msg.edit(embed=statusstopped)
            await asyncio.sleep(2)
            await bot.change_presence(activity=discord.Activity(name=f"{status}", type=discord.ActivityType.playing))
            statuschanged = discord.Embed(title="Bot status has been changed!", color=discord.Color.green())
            await msg.edit(embed=statuschanged)
        elif type == "listening":
            e = discord.Embed(title="Stopping auto-status change events", color=discord.Color.red())
            msg = await ctx.respond(embed=e)
            await asyncio.sleep(3)
            bot.unload_extension("cogs.status")
            statusstopped = discord.Embed(title="Auto-Status change has been stopped!", color=discord.Color.orange())
            await msg.edit(embed=statusstopped)
            await asyncio.sleep(2)
            await bot.change_presence(activity=discord.Activity(name=f"{status}", type=discord.ActivityType.listening))
            statuschanged = discord.Embed(title="Bot status has been changed!", color=discord.Color.green())
            await msg.edit(embed=statuschanged)
        elif type == "watching":
            e = discord.Embed(title="Stopping auto-status change events", color=discord.Color.red())
            msg = await ctx.respond(embed=e)
            await asyncio.sleep(3)
            bot.unload_extension("cogs.status")
            statusstopped = discord.Embed(title="Auto-Status change has been stopped!", color=discord.Color.orange())
            await msg.edit(embed=statusstopped)
            await asyncio.sleep(2)
            await bot.change_presence(activity=discord.Activity(name=f"{status}", type=discord.ActivityType.watching))
            statuschanged = discord.Embed(title="Bot status has been changed!", color=discord.Color.green())
            await msg.edit(embed=statuschanged)
        else:
            error = discord.Embed(title=":x: Error!", description="You must provide a status type and status value.\n**Syntax**\n`>setstatus listening dua lipa`", color=discord.Color.red())
            await ctx.respond(embed=error)
    else:
        e = discord.Embed(title=":x: You are not allowed to run this command!", color=discord.Color.red())
        await ctx.respond(embed=e)


def read_json(filename):
    with open(f"{filename}.json", "r") as f:
        data = json.load(f)
    return data

def write_json(data, filename):
    with open(f"{filename}.json", "w") as f:
        json.dump(data, f, indent=4)

bot.run(token)
