import discord
from replit import db
import os

default_prefix = 'd!'


def createStandardEmbed(ctx, description, title):
    embed = discord.Embed(
        description=description,
        color=0xd303fc,
        timestamp=ctx.message.created_at
    )
    embed.set_author(
        name=title, icon_url='https://cdn.discordapp.com/attachments/790920201217769513/818984229722652722/Robot_Head.jpg')
    embed.set_footer(text=ctx.bot.user.name)
    return embed


def getPrefix(client, ctx): # Get the prefix for the current guild from the db
    try:
        prefix = str(db[str(ctx.guild.id)]) # Get the prefix from the db by using the guild id as the key
    except KeyError:
        prefix = default_prefix # If the db entry isnt found, switch to the default prefix
    return prefix


def writeToDb(key, value): # Write to the replit db using a key and value pair
    db[str(key)] = str(value)


def deleteDbEntry(key): # Delete a db entry
    try:
        del db[str(key)] # Delete the entry from the replit db by using the key
    except KeyError: 
        return # If the db entry isnt found, do nothing


def createHelpEmbed(ctx, client, name, description, params, req_perms, aliases):
    embed = createStandardEmbed(ctx, description, name + " help")
    prefix = getPrefix(client, ctx)
    embed.add_field(name="Syntax", value=prefix+name+" "+params, inline=False)
    embed.add_field(name="Required Permissions", value=req_perms, inline=False)
    embed.add_field(name="Aliases", value=aliases, inline=False)

    return embed


def getMember(client, arg): # Safe way of getting a member object
    if isinstance(arg, int):
        return client.get_user(arg) # If the argument is an int and thus an id, get the member object from that id
    elif isinstance(arg, discord.Member):
        return arg # If its a member object already, just return it normally
    else:
        raise discord.InvalidArgument # If its neither an id or a discord.Member object, raise an error


def uppath(_path, n): return os.sep.join(_path.split(os.sep)[:-n]) # Return the parent directory (n defines the times that you want to go up)
