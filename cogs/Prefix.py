from discord.ext import commands
from core.src.helperFunctions.helperFunctions import *


class PrefixCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def prefix(self, ctx, prefix=None): # Change or view the current prefix for the server
        if prefix is not None and ctx.author.guild_permissions.administrator: # Checks if the user has passed in a prefix and if theyre an admin
            if prefix == default_prefix: 
                deleteDbEntry(ctx.guild.id) # Check if the prefix is the default prefix. If it is, delete the db entry (for storage optimization)
            else:
                writeToDb(ctx.guild.id, prefix) # Write the new prefix to the db with the guild id as the key
            em = createStandardEmbed(ctx, f"The prefix was successfully changed to `{prefix}`", "Prefix")
            await ctx.send(embed=em)
        else:
            em = createStandardEmbed(ctx, f"The current prefix for this server is `{getPrefix(client = self.bot, ctx = ctx)}`\nYou can change the prefix like this: `{getPrefix(client = self.bot, ctx = ctx)}prefix [new_prefix]`", "Current Server Prefix")
            await ctx.send(embed=em)
    
    @commands.Cog.listener()
    async def on_guild_remove(self, guild): # If the bot gets removed (kicked/banned) from a server, then delete the db entry for that server (for storage optimization)
        deleteDbEntry(guild.id)


def setup(bot):
    bot.add_cog(PrefixCommands(bot))
