import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound
import random

class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    ## command error feedback
    @commands.Cog.listener()
    async def on_command_error(self, ctx, ex):
        if isinstance(ex, CommandNotFound):
            await ctx.send("Unfortunately we failed to find your command please refer to !help")
        elif hasattr(ex,"original"):
            raise ex.original
        else : 
            raise ex
        # await ctx.send(f'What do you mean by {ex.original} ? \nPlease check with !help, or on the manual at trucGithub.com')

    @commands.command(name='repeat', aliases=['mimic', 'copy'])
    async def say(self, ctx, *, inp: str):
        """A simple command which repeats your input!
        Parameters
        ------------
        inp: str
            The input you wish to repeat.
        """
        await ctx.send(inp)
        
    @say.error
    async def say_handler(self, ctx, error):
        """A local Error Handler for our command do_repeat.
        This will only listen for errors in do_repeat.
        The global on_command_error will still be invoked after.
        """

        if isinstance(error, commands.MissingRequiredArgument):
            if error.param.name == 'inp':
                await ctx.send("You forgot to give me input to repeat!")

    @commands.command(brief="Create an invite")
    async def invite(self, ctx):
        link = await ctx.channel.create_invite(max_age=1)
        await ctx.send(link)

    @commands.Cog.listener("on_message")
    async def detect(self, message):
        if message.author.bot:
            pass
        else :
            x = message.content.split()
            print(x)
            #Possible greetings from user
            Cheers = ["Hi", "hi", "Hello", "hello","bonjour","salut","coucou","ciao","Hey","Yo","Sup","sup","yo","hey"]
            unCheers= ["bye", "Bye", "cya", "cu","ciao","aurevoir","Aurevoir","a+","A+","++",]
            #Possible greetings from bot
            happy_emoji = [":grinning:",":smiley:",":smile:",":grin:",":laughing:",":slight_smile:",":sunglasses:"]
            RCheers = ["Hi", "Hello","Bonjour","Salut","Coucou","It’s good to see you.","Hey","Hey there","What’s up?","Yo!","Sup?","Waddap"]
            RunCheers= ["Bye", "cya", "cu","ciao","Aurevoir","a+","Goodbye","Bye bye!","Take it easy","Take care","Later","See you soon","I hope to see you soon"]
            if any(word in x for word in Cheers):
                    msg = f'{random.choice(RCheers)} {message.author.mention} {random.choice(happy_emoji)}'
                    await message.channel.send(msg)
            elif any(word in x for word in unCheers):
                    msg = f'{random.choice(RunCheers)} {message.author.mention} {random.choice(happy_emoji)}'
                    await message.channel.send(msg)

def setup(bot):
    bot.add_cog(Basic(bot))

# # https://stackoverflow.com/questions/65062365/discord-py-cog-problem-with-on-message-event-dont-work