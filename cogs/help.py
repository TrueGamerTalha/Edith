import email
import discord
import traceback
import random
from discord.ext import commands

class Dropdown(discord.ui.Select):
    def __init__(self):

        options = [
            discord.SelectOption(
                label="Moderation", description="Commands to uphold the peace and integrity of the server", emoji="<a:helpmod:821086944079380500>"
            ),
            discord.SelectOption(
                label="Fun", description="Commands to have some fun and relieve stress (or induce it)", emoji="<a:helpsettings:826501079797202964>"
            ),
            discord.SelectOption(
                label="Bot Commands", description="Commands related to the bot, such as it's information etc", emoji="<a:edithhelp:821086587277410335>"
            ),
        ]


        super().__init__(
            placeholder="Select a Category",
            min_values=1,
            max_values=1,
            options=options,
        )

    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "Moderation":
            e = discord.Embed(title="Moderation Commands", color=discord.Color.blue(), description="**Clear**(`/clear`)\nClears messages in a channel\n\n**Slowmode**(`/slowmode`)\nAdd slowmode delay in the current channel\n\n**Ban**(`/ban`)\nPermanently remove a person from the server\n\n**Unban**(`/unban`)\nUnban a person from the server\n\n**Kick**(`/kick`)\nRemove a person from the server\n\n**Warn**(`/warn`)\nWarn a member for doing something they weren't supposed to\n\n**Warns**(`/warns`)\nCheck warns for a user\n\n**Remove Warn**(`/removewarn`)\nRemove a warn from a member")
            await interaction.response.send_message(embed=e, ephemeral=True)
        if self.values[0] == "Fun":
            e = discord.Embed(title="Fun Commands", color=discord.Color.blue(), description="**Flip**(`/coinflip`)\nFlip a coin\n\n**Emojify**(`/emojify`)\nTurn a sentence into emojis\n\n**Password**(`/password`)\nGenerate a password\n\n**AI**(`/ai`)\nAsk the AI a question!\n\n**Joke**(`/joke`)\nGives you a joke\n\n**ASCII**(`/ascii`)\nTurn a sentence into cool ASCII art\n\n**8Ball**(`/8ball`)\nCall upon the powers of the all knowning magic 8Ball")
            await interaction.response.send_message(embed=e, ephemeral=True)
        if self.values[0] == "Bot Commands":
            e = discord.Embed(title="Bot Commands", color=discord.Color.blue(), description="**Bot Information**(`/botinfo`)\nShows information about Edith\n\n**Uptime**(`/uptime`)\nShows the time the bot has been online for\n\n**Ping**(`/ping`)\nCheck the bots ping\n\n**Invite**(`/invite`)\nGives you a link to invite Edith\n\n**Vote**(`/vote`)\nGives you a link to vote for the bot(please do it!)")
            await interaction.response.send_message(embed=e, ephemeral=True)

class DropdownView(discord.ui.View):
    def __init__(self):
        super().__init__()

        # Adds the dropdown to our view object.
        self.add_item(Dropdown())

class Help(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.slash_command()
    async def help(self, ctx):
        e = discord.Embed(title="Edith help", description="I'm a cool multi-purpose to help you manage your server better...", color=discord.Color.blue())
        e.add_field(name="1) Moderation", value="Commands to uphold the peace and integrity of the server")
        e.add_field(name="2) Fun", value="Commands to have some fun and relieve stress (or induce it)")
        e.add_field(name="3) Bot commands", value="Commands related to the bot, such as it's information etc")
        await ctx.respond(embed=e, view=DropdownView())

    @commands.command()
    async def helpmusic(self, ctx):
        embed = discord.Embed(title="Music")
        embed.add_field(name="play", value="Plays the video URL or the name of the song in the voice channel you're in!", inline=False)
        embed.add_field(name="skip", value="Skips the song or puts in your vote to skip the song(if more than 3 members)", inline=False)
        embed.add_field(name="fskip", value="Force skips the current song.", inline=False)
        embed.add_field(name="remove", value="Removes the last song you requested from the queue, or a specific song if queue position specified.", inline=False)
        embed.add_field(name="fremove", value="Admin command to forcibly remove a song from the queue by it's position.", inline=False)
        embed.add_field(name="queue", value="Prints out a specified page of the music queue, defaults to first page.", inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def Helpmusic(self, ctx):
        embed = discord.Embed(title="Music")
        embed.add_field(name="play", value="Plays the video URL or the name of the song in the voice channel you're in!", inline=False)
        embed.add_field(name="skip", value="Skips the song or puts in your vote to skip the song(if more than 3 members)", inline=False)
        embed.add_field(name="fskip", value="Force skips the current song.", inline=False)
        embed.add_field(name="remove", value="Removes the last song you requested from the queue, or a specific song if queue position specified.", inline=False)
        embed.add_field(name="fremove", value="Admin command to forcibly remove a song from the queue by it's position.", inline=False)
        embed.add_field(name="queue", value="Prints out a specified page of the music queue, defaults to first page.", inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def helpMusic(self, ctx):
        embed = discord.Embed(title="Music")
        embed.add_field(name="play", value="Plays the video URL or the name of the song in the voice channel you're in!", inline=False)
        embed.add_field(name="skip", value="Skips the song or puts in your vote to skip the song(if more than 3 members)", inline=False)
        embed.add_field(name="fskip", value="Force skips the current song.", inline=False)
        embed.add_field(name="remove", value="Removes the last song you requested from the queue, or a specific song if queue position specified.", inline=False)
        embed.add_field(name="fremove", value="Admin command to forcibly remove a song from the queue by it's position.", inline=False)
        embed.add_field(name="queue", value="Prints out a specified page of the music queue, defaults to first page.", inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def HELPMUSIC(self, ctx):
        embed = discord.Embed(title="Music")
        embed.add_field(name="play", value="Plays the video URL or the name of the song in the voice channel you're in!", inline=False)
        embed.add_field(name="skip", value="Skips the song or puts in your vote to skip the song(if more than 3 members)", inline=False)
        embed.add_field(name="fskip", value="Force skips the current song.", inline=False)
        embed.add_field(name="remove", value="Removes the last song you requested from the queue, or a specific song if queue position specified.", inline=False)
        embed.add_field(name="fremove", value="Admin command to forcibly remove a song from the queue by it's position.", inline=False)
        embed.add_field(name="queue", value="Prints out a specified page of the music queue, defaults to first page.", inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def helpadmin(self, ctx):
        embed = discord.Embed(title="Moderation", description="----------------------------------------------------------------------------")
        embed.add_field(name="Kick ", value="Kicks a member.", inline=False )
        embed.add_field(name="Ban ", value="Bans a member.", inline=False )
        embed.add_field(name="Mute", value="Mutes a member", inline=False )
        embed.add_field(name="UnMute", value="Unmutes a member", inline=False )
        embed.add_field(name="Clear", value="Clears a certain Amout of messages.", inline=False )
        embed.add_field(name="Sayembed", value="Says  what you said but in embed form", inline=False)
        embed.add_field(name="Lock", value="Locks a Channel", inline=False)
        embed.add_field(name="Unlock", value="Unlocks a channel", inline=False)
        embed.add_field(name="Slowmode", value="Puts Slowmode on the channel", inline=False)
        embed.add_field(name="Softban", value="Bans then Unbans the user(you can use kick instead of this command)", inline=False)
        embed.add_field(name="Temmpban", value="Tempbans A user from the server", inline=False)
        embed.add_field(name="Warns", value="Check Warns for a user", inline=False)
        await ctx.send(embed=embed)
        
    @commands.command()
    async def helpfun(self, ctx):
        embed = discord.Embed(title="Fun Commands", description="---------------------------")
        embed.add_field(name="Hi", value="Says hi back", inline=False)
        embed.add_field(name="Info", value="Give's bot info", inline=False)
        embed.add_field(name="Flip", value="Flip's a coin", inline=False)
        embed.add_field(name="Say", value="Says That you said")
        embed.add_field(name="Skin", value="Get a Minecraft Player's Skin")
        await ctx.send(embed=embed)
        print("helpfun")

    @commands.command()
    async def Helpfun(self, ctx):
        embed = discord.Embed(title="Fun Commands", description="---------------------------")
        embed.add_field(name="Hi", value="Says hi back", inline=False)
        embed.add_field(name="Info", value="Give's bot info", inline=False)
        embed.add_field(name="Flip", value="Flip's a coin", inline=False)
        embed.add_field(name="Say", value="Says That you said")
        embed.add_field(name="Skin", value="Get a Minecraft Player's Skin")
        await ctx.send(embed=embed)
        print("Helpfun")

    @commands.command()
    async def HelpFun(self, ctx):
        embed = discord.Embed(title="Fun Commands", description="---------------------------")
        embed.add_field(name="Hi", value="Says hi back", inline=False)
        embed.add_field(name="Info", value="Give's bot info", inline=False)
        embed.add_field(name="Flip", value="Flip's a coin", inline=False)
        embed.add_field(name="Say", value="Says That you said")
        embed.add_field(name="Skin", value="Get a Minecraft Player's Skin")
        await ctx.send(embed=embed)
        print("HelpFun")

    @commands.command()
    async def helpFun(self, ctx):
        embed = discord.Embed(title="Fun Commands", description="---------------------------")
        embed.add_field(name="Hi", value="Says hi back", inline=False)
        embed.add_field(name="Info", value="Give's bot info", inline=False)
        embed.add_field(name="Flip", value="Flip's a coin", inline=False)
        embed.add_field(name="Prefix", value="Get's Bot Prefix", inline=False)
        embed.add_field(name="Say", value="Says That you said", inline=False)
        embed.add_field(name="Skin", value="Get a Minecraft Player's Skin", inline=False)
        await ctx.send(embed=embed)        
        
    @commands.command()
    async def HELPFUN(self, ctx):
        embed = discord.Embed(title="Fun Commands", description="---------------------------")
        embed.add_field(name="Hi", value="Says hi back", inline=False)
        embed.add_field(name="Info", value="Give's bot info", inline=False)
        embed.add_field(name="Flip", value="Flip's a coin", inline=False)
        embed.add_field(name="Say", value="Says That you said", inline=False)
        embed.add_field(name="Skin", value="Get a Minecraft Player's Skin", inline=False)
        await ctx.send(embed=embed)
        print("HELPFUN")
    

def setup(bot):
    bot.add_cog(Help(bot))