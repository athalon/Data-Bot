from discord.ext import commands
from core.src.helperFunctions.helperFunctions import *
from replit import db

class DevCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    async def cog_check(self, ctx):
        # Check if user is the dev (ath, aka. me)
        return ctx.author.id == 615608898279309312
    
    @commands.command()
    async def db_dump(self, ctx):
        msg = ""
        for key in db.keys():
            msg += db[key]
        await ctx.send(msg)
    
    @commands.command()
    async def db_del(self, ctx, key):
        deleteDbEntry(key)
        await ctx.send(f"Key `{key}` has been deleted!")


def setup(bot):
    bot.add_cog(DevCommands(bot))