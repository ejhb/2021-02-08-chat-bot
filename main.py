
import discord
from discord.ext import commands
from tokenkey import tokenkey

description = str("IneedAHomie Use must use the prefix ( ! ) to uses commands.")
bot = commands.Bot(command_prefix = "!", description = description)

@bot.event
async def on_ready():
	print("Ready !")

@bot.command()
async def coucou(ctx):
	await ctx.send("Coucou !")

@bot.command()
async def dan(ctx):
	await ctx.send("Dan a un boss", tts=True)

@bot.command()
async def bouffon(ctx):
	await ctx.send("So young to be a buffoon.", tts=True)

@bot.command()
async def dan_hobbie(ctx):
	await ctx.send("Dan est un adorateur du mal...  ", tts=True)

@bot.command()
async def hello(ctx):
	await ctx.send("Hello :)", tts=True)

@bot.command()
async def goodbye(ctx):
	await ctx.send("GoodBye :'(", tts=True)

@bot.command()
async def serverInfo(ctx):
	server = ctx.guild
	numberOfTextChannels = len(server.text_channels)
	numberOfVoiceChannels = len(server.voice_channels)
	serverDescription = server.description
	numberOfPerson = server.member_count
	serverName = server.name
	message = f"Le serveur **{serverName}** contient *{numberOfPerson}* personnes ! \nLa description du serveur est {serverDescription}. \nCe serveur possède {numberOfTextChannels} salons écrit et {numberOfVoiceChannels} salon vocaux."
	await ctx.send(message)

bot.run("tokenkey") #Ceci est le token de mon bot. Changez le avec celui de votre bot