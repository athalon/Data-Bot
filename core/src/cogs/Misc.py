from discord.ext import commands
from core.src.helperFunctions.helperFunctions import *


class MiscCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command
    async def invite(self, ctx):
        await ctx.send("https://discord.com/api/oauth2/authorize?client_id=818981250068774942&permissions=67226624&scope=bot")


def setup(bot):
    bot.add_cog(MiscCommands(bot))