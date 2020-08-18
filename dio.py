# IMPORT DISCORD.PY and os
import discord
import os
import asyncio

# Imports
from discord.ext import commands
from dotenv import load_dotenv

# LOADS THE .ENV FILE THAT RESIDES ON THE SAME LEVEL AS THE SCRIPT.
load_dotenv()

# GRAB THE API TOKEN FROM THE .ENV FILE.
#DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# GETS THE CLIENT OBJECT FROM DISCORD.PY. CLIENT IS SYNONYMOUS WITH BOT.
bot = discord.Client()

#Interpret !commands
bot = commands.Bot(command_prefix='!')


#Stats when bot is started
@bot.event
async def on_ready():
	# CREATES A COUNTER TO KEEP TRACK OF HOW MANY GUILDS / SERVERS THE BOT IS CONNECTED TO.
	guild_count = 0

	# LOOPS THROUGH ALL THE GUILD / SERVERS THAT THE BOT IS ASSOCIATED WITH.
	for guild in bot.guilds:
		# PRINT THE SERVER'S ID AND NAME.
		print(f"- {guild.id} (name: {guild.name})")

		# INCREMENTS THE GUILD COUNTER.
		guild_count = guild_count + 1

	# PRINTS HOW MANY GUILDS / SERVERS THE BOT IS IN.
	print("DIO is in " + str(guild_count) + " guilds.")
	

#Send a message when a member joins
@bot.event
async def on_member_join(Context, member):
	await Context.send("Welcome to Dio bot hell "+str(member))


#Sends a message when using the !summon command
@bot.command(name = 'summon', help = 'Summon Dio')
async def summonDio(Context):
	await Context.send("I have been summoned")
	
@bot.command(name = 'za-warudo', help = 'Sends channel into slow mode')
async def zaWarudo(Context):
	await Context.channel.edit(slowmode_delay=5)
	await Context.send(file=discord.File('warudo.jpg'))
	await Context.send("Za Warudo! Chat has been slowed for 20 seconds")
	await asyncio.sleep(20)
	await Context.channel.edit(slowmode_delay=0)

@bot.command(pass_context = True, help = 'Mutes a user for 20 seconds')
async def mute(Context, members: commands.Greedy[discord.Member]):

    if not members:
        await Context.send("You need to name someone to mute")
        return

    muted_role = discord.utils.find(lambda m: m.name == 'Muted', Context.guild.roles)

    for member in members:
        if bot.user == member: # what good is a muted bot?
            await Context.send("You can't mute me, I'm the almighty Dio Brando")
            continue
        await member.add_roles(muted_role, reason = "Dio has muted you")
        await Context.send(str(member)+" has been muted by Dio for "+str(Context.author))
    await asyncio.sleep(20)
    await member.remove_roles(muted_role)

# EXECUTES THE BOT WITH THE SPECIFIED TOKEN.
bot.run("NzQ0OTEwOTU3OTAxNTEyNzc1.XzqGZA.AH4Ju93e7rIVGjlrouD9jOZFgC0")


