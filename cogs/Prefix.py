from discord.ext import commands
from core.src.helperFunctions.helperFunctions import *


class PrefixCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def prefix(self, ctx, prefix=None):
        if prefix is not None and ctx.author.guild_permissions.administrator:
            writeToDb(ctx.guild.id, prefix)
            em = createStandardEmbed(ctx, f"The prefix was successfully changed to `{prefix}`", "Prefix")
            await ctx.send(embed=em)
        else:
            em = createStandardEmbed(ctx, f"The current prefix for this server is `{getPrefix(client = self.bot, ctx = ctx)}`\nYou can change the prefix like this: `{getPrefix(client = self.bot, ctx = ctx)}prefix [new_prefix]`", "Current Server Prefix")
            await ctx.send(embed=em)
    
    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        deleteDbEntry(guild.id)


def setup(bot):
    bot.add_cog(PrefixCommands(bot))
