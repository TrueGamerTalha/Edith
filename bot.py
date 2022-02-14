
print("Starting boot-up process...")
import discord
from discord.ext import commands
import os
import json
import ast
import dotenv
from dotenv import load_dotenv
import asyncio
import humanize
from datetime import datetime, timedelta
from discord.commands import \
    slash_command

print("Loading envoirment variables")
load_dotenv()
token = os.getenv("TOKEN")
prefix = os.getenv("PREFIX")
print("Loaded envoirment variables")

os.chdir("./")

async def get_prefix(client, message):
    with open("prefix.json", "r") as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

print("Creating client")
bot = commands.Bot(command_prefix=prefix)
bot.remove_command('help')
print("Client created")

print("Loading cogs and commands")
for filename in os.listdir('./cogs'):
	if filename.endswith(".py"):
		bot.load_extension(f'cogs.{filename[:-3]}')
		print(f"\"{filename[:-3]}\" cog has been loaded.") 

owner_ids = [702385226407608341, 929270204222046249]
bot.blacklisted_users = []

# @bot.event
# async def on_connect():
#     print('Connected to Discord')
#     await bot.change_presence(activity=discord.Activity(name=f"Bot is starting", url="https://www.twitch.tv/neilisop", type=discord.ActivityType.streaming))

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

    embed = discord.Embed(title="Statistics:", 
    description=f"**Username:** Edith\n**Discriminator:** 1574\n**Servers:** {guild_count}\n**Users:** {total_member_count}\n**Bot Version:** 2.0 \n**Uptime:** {humanized_time}\n**Client Status:**`🟢 Online` - `{ping}`\n**Library:** Discord.py - `{discord.__version__}`\n\n\n:warning: **We've shifted to Slash Commands! All Normal commands will not work from 1 March 12:00PM IST. If the Slash Commands don't appear, please reinvite the bot with this link: https://discord.com/oauth2/authorize?client_id=731807331796385812&permissions=1642824466295&scope=bot%20applications.commands. **",
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

@bot.command()
@commands.has_permissions(administrator=True)
async def prefix(ctx, prefix):

    with open("prefix.json", "r") as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open("prefix.json", "w") as f:
        json.dump(prefixes,f)    

    e = discord.Embed(title=":white_check_mark: Success!", description=f"The prefix was changed to {prefix}", color=discord.Color.green())
    await ctx.send(embed=e)

@bot.event
async def on_guild_join(guild):
    with open("prefix.json", "r") as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = ">"
    
    with open("prefix.json", "w") as f:
        json.dump(prefixes, f, indent=4)
    channel = bot.get_channel(936237231436365834)
    e = discord.Embed(title="New Guild!")
    e.add_field(name="Guild Name", value=f"**{guild.name}**", inline=False)
    e.add_field(name="Guild ID", value=f"**{guild.id}**", inline=False)
    await channel.send(embed=e)

@bot.event
async def on_guild_remove(guild):
    with open("prefix.json", "r") as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))
    
    with open("prefix.json", "w") as f:
        json.dump(prefixes, f, indent=4)
    channel = bot.get_channel(936237231436365834)
    e = discord.Embed(title="Left Guild!")
    e.add_field(name="Guild Name", value=f"**{guild.name}**")
    await channel.send(embed=e)

"""Blacklist Stuff"""

ownerid1 = owner_ids[0]
ownerid2 = owner_ids[1]

@bot.event
async def on_ready():
    print("Bot is online!")
    data = read_json("blacklist")
    bot.blacklisted_users = data["blacklistedUsers"]
    channel = bot.get_channel(936669729777680404)
    e = discord.Embed(title="Bot is online!", description=f"Owners: <@{ownerid1}> and <@{ownerid2}>\nBlacklisted users = {bot.blacklisted_users}", color=discord.Color.green(), timestamp=datetime.utcnow())
    e.set_footer(text='\u200b',icon_url="https://cdn.discordapp.com/attachments/929652173682409482/936227655584452668/IMG_6767.png")
    await channel.send(embed=e)
    global launched_at
    launched_at = datetime.now()

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

"""HELP COMMANDS, DON'T SEE BELOW!"""

@bot.group(invoke_without_command=True)
async def help(ctx):
    embed = discord.Embed(title="Edith Help",
                          description="Do `>help <command>` for extended help for the command!", color=discord.Color.blue())
    embed.add_field(name="Moderation", value="kick, ban, mute, tempban, softban, warns, warn, removewarn, lock, unlock, clear, unmute, slowmode")
    embed.add_field(name="Fun", value="flip, say, emojify, ascii, count, password, uptime, info, ai, joke")
    embed.add_field(name="Music", value="play, skip, remove, summon, queue, join, stop, volume, leave")
    await ctx.send(embed=embed)

"""MODERATION"""

@help.command()
async def kick(ctx):
    embed = discord.Embed(
        title="Kick", description="Kicks a member from the guild!", color=discord.Color.blue())
    embed.add_field(name="**Syntax**", value=">kick <member> [reason]")
    await ctx.send(embed=embed)


@help.command()
async def ban(ctx):
    embed = discord.Embed(
        title="Ban", description="Bans a member from the guild!", color=discord.Color.blue())
    embed.add_field(name="**Syntax**", value=">ban <member> [reason]")
    await ctx.send(embed=embed)

@help.command()
async def mute(ctx):
    embed = discord.Embed(
        title="Mute", description="Mutes a member!", color=discord.Color.blue())
    embed.add_field(name="**Syntax**", value=">mute <member> <time> [reason]")
    await ctx.send(embed=embed)

@help.command()
async def tempban(ctx):
    embed = discord.Embed(
        title="Tempban", description="Temp bans a member from the guild!", color=discord.Color.blue())
    embed.add_field(name="**Syntax**", value=">tempban <member> <time> [reason]")
    await ctx.send(embed=embed)

@help.command()
async def clear(ctx):
    embed = discord.Embed(
        title="Clear", description="Clears a certain Amout of messages.", color=discord.Color.blue())
    embed.add_field(name="**Syntax**", value=">clear <amount>")
    await ctx.send(embed=embed)

@help.command()
async def sayembed(ctx):
    embed = discord.Embed(
        title="sayembed", description="Says what you said but in embed form.", color=discord.Color.blue())
    embed.add_field(name="**Syntax**", value=">sayembed <message>")
    await ctx.send(embed=embed)

@help.command()
async def lock(ctx):
    embed = discord.Embed(
        title="lock", description="Locks a Channel.", color=discord.Color.blue())
    embed.add_field(name="**Syntax**", value=">lock")
    await ctx.send(embed=embed)

@help.command()
async def unlock(ctx):
    embed = discord.Embed(
        title="unlock", description="UnLocks a Channel.", color=discord.Color.blue())
    embed.add_field(name="**Syntax**", value=">unlock")
    await ctx.send(embed=embed)

@help.command()
async def slowmode(ctx):
    embed = discord.Embed(
        title="Slowmode", description="Puts Slowmode on the channel.", color=discord.Color.blue())
    embed.add_field(name="**Syntax**", value=">slowmode")
    await ctx.send(embed=embed)

@help.command()
async def softban(ctx):
    embed = discord.Embed(
        title="Softban", description="Bans then Unbans the user(you can use kick instead of this command.", color=discord.Color.blue())
    embed.add_field(name="**Syntax**", value=">softban <member> [reason]")
    await ctx.send(embed=embed)

@help.command()
async def warns(ctx):
    embed = discord.Embed(
        title="Warns", description="Check warns for a user.", color=discord.Color.blue())
    embed.add_field(name="**Syntax**", value=">warns <member>")
    await ctx.send(embed=embed)

@help.command()
async def warn(ctx):
    embed = discord.Embed(
        title="Warn", description="Warn a member", color=discord.Color.blue())
    embed.add_field(name="**Syntax**", value=">warn <member> [reason]")
    await ctx.send(embed=embed)

@help.command()
async def removewarn(ctx):
    embed = discord.Embed(
        title="Remove warn", description="Removes a warn from a member", color=discord.Color.blue())
    embed.add_field(name="**Syntax**", value=">removewarn <member> <ID>")
    embed.set_footer(text="Warn ID can be found by doing >warns <member>")
    await ctx.send(embed=embed)

"""FUN"""

@help.command()
async def ai(ctx):
    embed = discord.Embed(
        title="AI", description="Talk with the AI", color=discord.Color.blue())
    embed.add_field(name="**Syntax**", value=">ai <input>")
    await ctx.send(embed=embed)

@help.command()
async def flip(ctx):
    embed = discord.Embed(
        title="Flip", description="Flip's a coin", color=discord.Color.blue())
    embed.add_field(name="**Syntax**", value=">flip")
    await ctx.send(embed=embed)

@help.command()
async def say(ctx):
    embed = discord.Embed(
        title="Say", description="Says your message", color=discord.Color.blue())
    embed.add_field(name="**Syntax**", value=">say <message>")
    await ctx.send(embed=embed)

@help.command()
async def emojify(ctx):
    embed = discord.Embed(
        title="Emojify", description="Turn a sentence into emojis", color=discord.Color.blue())
    embed.add_field(name="**Syntax**", value=">emojify <message>")
    await ctx.send(embed=embed)

@help.command()
async def ascii(ctx):
    embed = discord.Embed(
        title="Ascii", description="Turn a sentence into cool ASCII art", color=discord.Color.blue())
    embed.add_field(name="**Syntax**", value=">say <message>")
    await ctx.send(embed=embed)

@help.command()
async def count(ctx):
    embed = discord.Embed(
        title="Count", description="Count the messages given in the channel", color=discord.Color.blue())
    embed.add_field(name="**Syntax**", value=">count")
    await ctx.send(embed=embed)

@help.command()
async def password(ctx):
    embed = discord.Embed(
        title="Password", description="Get a random password in your DMs", color=discord.Color.blue())
    embed.add_field(name="**Syntax**", value=">count")
    await ctx.send(embed=embed)

@help.command()
async def info(ctx):
    embed = discord.Embed(
        title="Info", description="Get information about the bot", color=discord.Color.blue())
    embed.add_field(name="**Syntax**", value=">info")
    await ctx.send(embed=embed)

@help.command()
async def uptime(ctx):
    embed = discord.Embed(
        title="Count", description="Check the uptime of the bot", color=discord.Color.blue())
    embed.add_field(name="**Syntax**", value=">uptime")
    await ctx.send(embed=embed)

"""Music help"""

@help.command()
async def play(ctx):
    embed = discord.Embed(
        title="Play", description="Play a song", color=discord.Color.blue())
    embed.add_field(name="**Syntax**", value=">play <song name or URL>")
    await ctx.send(embed=embed)

@help.command()
async def skip(ctx):
    embed = discord.Embed(
        title="Skip", description="Skips the song or puts in your vote to skip the song(if more than 3 members)", color=discord.Color.blue())
    embed.add_field(name="**Syntax**", value=">skip")
    await ctx.send(embed=embed)

@help.command()
async def now(ctx):
    embed = discord.Embed(
        title="Now", description="Shows the current song.", color=discord.Color.blue())
    embed.add_field(name="**Syntax**", value=">now")
    await ctx.send(embed=embed)

@help.command()
async def remove(ctx):
    embed = discord.Embed(
        title="Remove", description="Removes the last song you requested from the queue, or a specific song if queue position specified.", color=discord.Color.blue())
    embed.add_field(name="**Syntax**", value=">remove")
    await ctx.send(embed=embed)

@help.command()
async def shuffle(ctx):
    embed = discord.Embed(
        title="Shuffle", description="Shuffle the songs in the queue!", color=discord.Color.blue())
    embed.add_field(name="**Syntax**", value=">shuffle")
    await ctx.send(embed=embed)

@help.command()
async def queue(ctx):
    embed = discord.Embed(
        title="Queue", description="Prints out a specified page of the music queue, defaults to first page.", color=discord.Color.blue())
    embed.add_field(name="**Syntax**", value=">uptime")
    await ctx.send(embed=embed)

@help.command()
async def leave(ctx):
    embed = discord.Embed(
        title="Leave", description="Clears the queue and leaves the voice channel.", color=discord.Color.blue())
    embed.add_field(name="**Syntax**", value=">leave")
    await ctx.send(embed=embed)

@help.command()
async def summon(ctx):
    embed = discord.Embed(
        title="Summon", description="Summons the bot to a voice channel. If no channel was specified, it joins your channel.", color=discord.Color.blue())
    embed.add_field(name="**Syntax**", value=">summon [channel]")
    await ctx.send(embed=embed)

@help.command()
async def join(ctx):
    embed = discord.Embed(
        title="Join", description="Joins a voice channel.", color=discord.Color.blue())
    embed.add_field(name="**Syntax**", value=">join")
    await ctx.send(embed=embed)

@help.command()
async def volume(ctx):
    embed = discord.Embed(
        title="Join", description="Sets the volume.", color=discord.Color.blue())
    embed.add_field(name="**Syntax**", value=">volume [0-5 Number]")
    await ctx.send(embed=embed)

@help.command()
async def joke(ctx):
    embed = discord.Embed(
    	title="Joke", description="Tells you a joke.", color=discord.Color.blue())
    embed.add_field(name="**Syntax**", value=">joke")
    await ctx.send(embed=embed)

print("Connecting to Discord")
bot.run(token)