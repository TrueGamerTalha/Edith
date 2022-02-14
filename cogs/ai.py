import requests
import discord
from discord.ext import commands

class AI(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    url = "https://random-stuff-api.p.rapidapi.com/ai"
    headers = { 
        'authorization': "vaEeVV60U00j",
        'x-rapidapi-host': "random-stuff-api.p.rapidapi.com",
        'x-rapidapi-key': "b240475e27msh56ecb8e8108cd78p1d1060jsna60e72eee0bc"
    }

    @commands.command()
    async def ai(self, ctx, *, msg):
        querystring = {"msg":f"{msg}","bot_name":"Edith","bot_gender":"Male","bot_master":"ItsNeil","bot_age":"18","bot_company":"Neil Development","bot_location":"India","bot_email":"hello@neildevolopment.ml","bot_build":"Private","bot_birth_year":"2003","bot_birth_date":"1st January, 2002","bot_birth_place":"India","bot_favorite_color":"Blue","bot_favorite_book":"Harry Potter","bot_favorite_band":"Imagine Doggos","bot_favorite_artist":"Dua Lipa","bot_favorite_actress":"Emma Watson","bot_favorite_actor":"Jim Carrey","id":"For customised response for each user"}
        request = requests.get(url=self.url, params=querystring, headers=self.headers)
        res = request.json()
        stuff = res['AIResponse']
        await ctx.reply(res['AIResponse'])
        channel = self.bot.get_channel(869245476304736317)
        e = discord.Embed(title="AI Command used!", color=discord.Color.blue())
        e.add_field(name="Input", value=f"```{msg}```", inline=False)
        e.add_field(name="Output", value=f"```{stuff}```", inline=False)
        e.add_field(name="Response time", value=f"```normal```", inline=False)
        e.add_field(name="Used by", value=f"```{ctx.author}```", inline=False)
        await channel.send(embed=e)

def setup(bot):
    bot.add_cog(AI(bot))