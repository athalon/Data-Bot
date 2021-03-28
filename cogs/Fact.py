from discord.errors import InvalidArgument
from discord.ext import commands
from core.src.helperFunctions.helperFunctions import *

class FactCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def animal(self, ctx, animal):
        allowed_animals = ['dog', 'cat', 'panda', 'fox', 'bird', 'koala']
        if animal.lower() in allowed_animals:
            await ctx.send(embed=createStandardEmbed(ctx, fetchFactApi(animal), f'Random {animal} fact'))
        else:
            raise InvalidArgument("There are no facts about the animal " + animal)
    

def setup(bot):
    bot.add_cog(FactCommands(bot))