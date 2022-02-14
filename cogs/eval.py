from time import time
from discord.ext import commands
from inspect import getsource
import discord
import asyncio
import os

class Eval(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    def resolve_variable(self, variable):
        if hasattr(variable, "__iter__"):
            var_length = len(list(variable))
            if (var_length > 100) and (not isinstance(variable, str)):
                return f"<a {type(variable).__name__} iterable with more than 100 values ({var_length})>"
            elif (not var_length):
                return f"<an empty {type(variable).__name__} iterable>"
        
        if (not variable) and (not isinstance(variable, bool)):
            return f"<an empty {type(variable).__name__} object>"
        return (variable if (len(f"{variable}") <= 1000) else f"<a long {type(variable).__name__} object with the length of {len(f'{variable}'):,}>")
    
    def prepare(self, string):
        arr = string.strip("```").replace("py\n", "").replace("python\n", "").split("\n")
        if not arr[::-1][0].replace(" ", "").startswith("return"):
            arr[len(arr) - 1] = "return " + arr[::-1][0]
        return "".join(f"\n\t{i}" for i in arr)
    
    @commands.command(pass_context=True, aliases=['eval', 'exec', 'evaluate'])
    async def _eval(self, ctx, *, code: str):
        owner_ids = [702385226407608341, 929270204222046249]
        if ctx.author.id in owner_ids:
            await ctx.message.delete()
            silent = ("-s" in code)

            code = self.prepare(code.replace("-s", ""))
            args = {
                "discord": discord,
                "self": self,
                "ctx": ctx,
                "asyncio": asyncio,
                "os": os
            }

            try:
                exec(f"async def func():{code}", args)
                a = time()
                response = await eval("func()", args)
                if silent or (response is None) or isinstance(response, discord.Message):
                    e = discord.Embed(title="Evaluated.", color=discord.Color.blue())
                    e.add_field(name="Code:", value=f"```py\n{code}```", inline=False)
                    e.add_field(name="Language:", value="```Python```", inline=False)
                    e.add_field(name="Executed by:", value=f"```{ctx.author}```", inline=False)
                    await ctx.send(embed=e, delete_after=30)
                    del args, code
                    return

            except Exception as e:
                await ctx.send(f"Error occurred:```\n{type(e).__name__}: {str(e)}```")

            del args, code, silent
        else:
            e = discord.Embed(title=":x: You are not allowed to run this command!", color=discord.Color.red())
            await ctx.send(embed=e)

def setup(bot):
    bot.add_cog(Eval(bot))