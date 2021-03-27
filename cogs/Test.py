from discord.ext import commands
from core.src.helperFunctions.helperFunctions import *


class TestCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test(self, ctx):
        await ctx.send(createStandardEmbed(ctx, "", "Test successful!"))


def setup(bot):
    bot.add_cog(TestCommands(bot))
