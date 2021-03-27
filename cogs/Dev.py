from discord.ext import commands
from core.src.helperFunctions.helperFunctions import *
from replit import db

class DevCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    async def cog_check(self, ctx): # This acts as a check for every command in this cog
        # Check if user is the dev (ath, aka. me)
        return ctx.author.id == 615608898279309312
    
    @commands.command()
    async def db_dump(self, ctx): # Dump all replit database contents
        msg = "Database contents:\n"
        for key in db.keys(): # Cycle through every key in the replit db
            msg += f'"{key}": "{db[key]}"\n' # Append the key and its value to the final message
        await ctx.send(msg)
    
    @commands.command()
    async def db_del(self, ctx, key): # Delete a db entry by key
        deleteDbEntry(key)
        await ctx.send(f"Key `{key}` has been deleted!")


def setup(bot):
    bot.add_cog(DevCommands(bot))