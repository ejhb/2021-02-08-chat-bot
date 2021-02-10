import discord
from discord.ext import commands
import random

class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #command error feedback
    @commands.Cog.listener()
    async def on_command_error(self, ctx, ex):
        print(ex)
        await ctx.send("Please check with !help, or on the manual at trucGithub.com")

    @commands.command(brief="Repeating sentence")
    async def say(self, ctx, *args):
        if len(args) > 0 :
            await ctx.send(" ".join(args))
        else : 
            await ctx.send("It need arguments")

    @commands.command(brief="Create an invite")
    async def invite(self, ctx):
        link = await ctx.channel.create_invite(max_age=1)
        await ctx.send(link)

    @commands.Cog.listener("on_message")
    async def detect(self, message):
        x = message.content.split()
        #Possible greetings from user
        Cheers = ["Hi", "hi", "Hello", "hello","bonjour","salut","coucou","ciao","Hey","Yo","Sup","sup","yo","hey"]
        unCheers= ["bye", "Bye", "cya", "cu","ciao","aurevoir","Aurevoir","a+","A+","++",]
        #Possible greetings from bot
        happy_emoji = [":grinning:",":smiley:",":smile:",":grin:",":laughing:",":slight_smile:",":sunglasses:"]
        RCheers = ["Hi", "Hello","Bonjour","Salut","Coucou","It’s good to see you.","Hey","Hey there","What’s up?","Yo!","Sup?","Waddap"]
        RunCheers= ["Bye", "cya", "cu","ciao","Aurevoir","a+","Goodbye","Bye bye!","Take it easy","Take care","Later","See you soon","I hope to see you soon"]
        print(x)
        if any(word in x for word in Cheers):
            if message.author.bot:
                return
            else : 
                msg = f'{random.choice(RCheers)} {message.author.mention} {random.choice(happy_emoji)}'
                await message.channel.send(msg)
        elif any(word in x for word in unCheers):
            if message.author.bot:
                return
            else : 
                msg = f'{random.choice(RunCheers)} {message.author.mention} {random.choice(happy_emoji)}'
                await message.channel.send(msg)


def setup(bot):
    bot.add_cog(Basic(bot))


# # https://stackoverflow.com/questions/65062365/discord-py-cog-problem-with-on-message-event-dont-work