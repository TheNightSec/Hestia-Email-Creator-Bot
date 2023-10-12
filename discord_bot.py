import discord
from panel_api import *

bot = discord.Bot()

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.slash_command()
async def addmail(ctx, username: str, password: str):
    """Add a email: Give username & pass like /addmail test @mypass123"""
    if username.lower() not in ["admin", "mrstark", "ravensworth"]:
        response = add_mail(username,password)
        if response == "":
            await ctx.respond(f"Sucessfully added {username}@m3ta.tech")
        else:
            await ctx.respond(response)
    else:
        await ctx.respond(f"Admin, Mrstark and Ravensworth cannot be added for security reasons. Also there already added.")

@bot.slash_command()
async def deletemail(ctx, username: str):
    """Delete a email: Give username like /deletemail test"""
    if username.lower() not in ["admin", "mrstark", "ravensworth"]:
        response = delete_mail(username)
        if response == "":
            await ctx.respond(f"Sucessfully deleted {username}@m3ta.tech")
        else:
            await ctx.respond(response)
    else:
        await ctx.respond(f"Admin, Mrstark and Ravensworth cannot be deleted for security reasons..")

@bot.slash_command()
async def changepass(ctx, username: str, password: str):
    """Change password: Give username & pass like /changepass test Another$%pass1234"""
    if username.lower() not in ["admin", "mrstark", "ravensworth"]:
        response = change_pass(username,password)
        if response == "":
            await ctx.respond(f"Sucessfully changed {username}@m3ta.tech password")
        else:
            await ctx.respond(response)
    else:
        await ctx.respond(f"Admin, Mrstark and Ravensworth passwords cannot be changed for security reasons.")

@bot.slash_command()
async def listmail(ctx):
    """List all email: No Input Required like /listmail"""
    response = list_mail()
    await ctx.respond(response)

@bot.slash_command()
@discord.default_permissions(administrator=True)
async def purge(ctx, limit: int):
    """Delete Specefic Amount Of Messages From A Channel"""
    await ctx.channel.purge(limit=limit)
    await ctx.respond('Cleared by {}'.format(ctx.author.mention), ephemeral=True)


bot.run("") # Add your discord Token here!
